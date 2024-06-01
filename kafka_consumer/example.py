from kafka import KafkaConsumer
from neo4j import GraphDatabase
import json

class Bridge:
    def __init__(self, bridge_uri, super_bridge_uri, cim_path, iec_path, cim_prop_name, iec_prop_name=None):
        self.bridge_uri = bridge_uri
        self.super_bridge_uri = super_bridge_uri
        self.cim_path=cim_path
        self.iec_path = iec_path
        self.cim_prop_name = cim_prop_name
        self.iec_prop_name= iec_prop_name if iec_prop_name is not None else cim_prop_name
    
    def get_cim(self):
        return self.__create_path(self.cim_path)
    
    def get_iec(self):
        return self.__create_path(self.iec_path)
    
    def get_super_bridge(self):
        return self.super_bridge_uri
    
    def __create_path(self, path, prefix=""):
        if path is None:
            return "-[relation]-"
        cipher_path = ''
        for i in range(len(path) - 1):
            cipher_path += f"-[:{path[i]}]-({prefix}node{i})"
        cipher_path += f"-[:{path[-1]}]-"
        return cipher_path

class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
    
    def query(self, query, parameters=None):
        records, summary, keys = self.__driver.execute_query(query_=query, parameters_=parameters)
        return records
    
    def execute_query(self, query, parameters=None):
        with self.__driver.session() as session:
            result = session.write_transaction(self.__execute_query, query, parameters)
            return result

    @staticmethod
    def __execute_query(tx, query, parameters=None):
        result = tx.run(query, parameters)
        return [record for record in result]

neo4j_conn = Neo4jConnection("bolt://neo4j:7687", "neo4j", "password")

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def find_relation(iec_candidates, cim_candidates, compare_method):
    iec_length = len(iec_candidates)
    cim_length = len(cim_candidates)
    maxLength = iec_length if iec_length > cim_length else cim_length
    for i in range(maxLength):
        iec = iec_candidates[i%iec_length]
        cim = cim_candidates[i%cim_length]
        match = compare_method(iec,cim)
        if match:
            return iec, cim
    return None


def get_candidates(class_uri, bridge_uri):
    query = '''
        MATCH (node)-[:IN_CAT]->(class:Class)--(bridge:OntoBridge)
        WHERE class.uri = $class_uri
        AND bridge.uri = $bridge_uri
        AND NOT EXISTS { 
            MATCH (node)-[rel]->() 
            WHERE type(rel) = bridge.label 
        }
        RETURN node
    '''
    params = {
        "class_uri": class_uri,
        "bridge_uri": bridge_uri
    }
    
    result = neo4j_conn.query(query, params)
    return result

substation_bridge = Bridge("http://www.semanticweb.org/information_management/ontobridge#Substation.tSubstation", None, None, None, "name")
bay_bridge = Bridge("http://www.semanticweb.org/information_management/ontobridge#Bay.tBay", "http://www.semanticweb.org/information_management/ontobridge#VoltageLevel.tVoltageLevel", ["VoltageLevel"], ["Bay"], "name")
voltage_level_bridge = Bridge("http://www.semanticweb.org/information_management/ontobridge#VoltageLevel.tVoltageLevel", "http://www.semanticweb.org/information_management/ontobridge#Substation.tSubstation", ["Substation"], ["VoltageLevel"], "name")
base_voltage_bridge = Bridge("http://www.semanticweb.org/information_management/ontobridge#BaseVoltage.tVoltage", "http://www.semanticweb.org/information_management/ontobridge#VoltageLevel.tVoltageLevel", ["BaseVoltage"], ["Voltage"], "nominalVoltage", "value")

bridges = {substation_bridge.bridge_uri: substation_bridge, bay_bridge.bridge_uri:bay_bridge, voltage_level_bridge.bridge_uri:voltage_level_bridge, base_voltage_bridge.bridge_uri:base_voltage_bridge}

def get_structural_candidates(json_object):
    bridge_uri = get_bridge_uri(json_object)
    bridge = bridges[bridge_uri]
    is_cim_object = is_cim(json_object)
    prop_name = bridge.cim_prop_name if is_cim_object else bridge.iec_prop_name
    node_candidates = "cim_node"
    node = "iec_node"
    if(is_cim_object):
        node, node_candidates = switch_pointers(node, node_candidates)
    node_identifier= json_object["node"][prop_name]
    query = f'''
        MATCH (onbridge:OntoBridge{'{'}uri:$bridge{'}'})
        MATCH (super:OntoBridge{'{'}uri:$super_bridge{'}'}),
            (sub:CIM)--(super)--(iec_sub:IEC61850),
            (cim_super)-[:IN_CAT]->(sub),
            (iec_super)-[:IN_CAT]->(iec_sub),
            (cim_node){bridge.get_cim()}(cim_super)-[bridge]-(iec_super),
            (iec_node){bridge.get_iec()}(iec_super)
                Where {node}.{prop_name}=$identifier AND type(bridge)=super.label AND NOT EXISTS {'{'} 
                    MATCH (cim_node)-[rel]->(),
                        (iec_node)-[rel1]->()
                    WHERE type(rel) = onbridge.label OR type(rel1)=onbridge.label
                {'}'}
        RETURN {node_candidates} as node
    '''
    params = {"identifier": node_identifier, "bridge":bridge_uri, "super_bridge":bridge.super_bridge_uri}
    result = neo4j_conn.query(query, params)
    return result

def process_result(result):
    if(not any(result)):
        return None
    candidates = []
    for candidate in result:
        candidates.append(convert_candidate(candidate))
    return candidates

def get_substation_candidates(json_object):
    results = get_candidates(json_object["compare"]["uri"], get_bridge_uri(json_object))
    return results

def convert_candidate(candidate):
    node = candidate.data("node")["node"]
    labels = {"labels": list(candidate["node"].labels)}
    merged_candidate = Merge(node, labels)
    return merged_candidate

def convert_nordic_chars(input_str):
    translation_table = str.maketrans({
        'æ': 'ae', 'Æ': 'Ae',
        'ø': 'oe', 'Ø': 'Oe',
        'å': 'aa', 'Å': 'Aa'
    })
    return input_str.translate(translation_table)

def compare_names(iec61850, cim):
    return convert_nordic_chars(iec61850["name"]) == cim["name"]

def parse_voltage(value):
    numeric_value = float(''.join(filter(lambda x: x.isdigit() or x == '.', value)))
    unit = ''.join(filter(str.isalpha, value))

    if unit.lower() == 'kv':
        return numeric_value * 1000
    return numeric_value

def compare_voltage(iec61850, cim):
    return parse_voltage(iec61850["value"]) == parse_voltage(cim["nominalVoltage"])

def clean_message(json_object):
    json_object['node']['labels'] = json_object['node'].pop('<labels>')
    return json_object

def align_nodes_with_domains(result, json_object):
    iec = [json_object["node"]]
    cim = result
    if is_cim(json_object):
        iec, cim = switch_pointers(iec, cim)
    return iec, cim

def switch_pointers(left, right):
    return right, left

def is_cim(json_object):
    return 'CIM' in json_object["category"]['<labels>']

def get_uris(json_object):
    iec_uri = json_object["category"]["uri"]
    cim_uri = json_object["compare"]["uri"]
    if is_cim(json_object):
        iec_uri, cim_uri = switch_pointers(iec_uri, cim_uri)
    return iec_uri, cim_uri    

def get_bridge_uri(json_object):
    return json_object["rel"]["uri"]

def get_bridge_method(json_object):
    match (get_bridge_uri(json_object)):
        case "http://www.semanticweb.org/information_management/ontobridge#Substation.tSubstation":
            return get_substation_candidates, compare_names
        case "http://www.semanticweb.org/information_management/ontobridge#VoltageLevel.tVoltageLevel":
            return get_structural_candidates, compare_names
        case "http://www.semanticweb.org/information_management/ontobridge#Bay.tBay":
            return get_structural_candidates, compare_names
        case "http://www.semanticweb.org/information_management/ontobridge#BaseVoltage.tVoltage":
            return get_structural_candidates, compare_voltage

def process_node(json_object):
    bridge_uri = get_bridge_uri(json_object)
    bridge = bridges[bridge_uri]
    candidate_method, compare_method = get_bridge_method(json_object)
    query_result = candidate_method(json_object)
    results = process_result(query_result)
    if results is None:
        return None
    iec, cim = align_nodes_with_domains(results, json_object)
    result = find_relation(iec, cim, compare_method)
    if result is not None:
        iec_uri, cim_uri = get_uris(json_object)
        iec, cim = result
        query = f'''
            MATCH (iec{'{'}{bridge.iec_prop_name}:$iec_name{'}'})-[:IN_CAT]->(i:IEC61850)
            MATCH (cim{'{'}{bridge.cim_prop_name}:$cim_name{'}'})-[:IN_CAT]->(c:CIM)
            WHERE i.uri=$iec_uri AND c.uri=$cim_uri
            CALL apoc.create.relationship(iec, $bridge, {'{}'}, cim) YIELD rel as rel1
            CALL apoc.create.relationship(cim, $bridge, {'{}'}, iec) YIELD rel
            RETURN rel1, rel
        '''
        params={"iec_name": iec[bridge.iec_prop_name], "cim_name":cim[bridge.cim_prop_name],"iec_uri":iec_uri, "cim_uri":cim_uri, "bridge":json_object["rel"]["label"]}
        print(neo4j_conn.execute_query(query, params))
        return cim
    
def reset_candidates(cim):
    bridge_uri = get_bridge_uri(json_object)
    current_bridge = bridges[bridge_uri]
    dependent_bridges = [bridge for bridge in bridges.values() if bridge.super_bridge_uri == bridge_uri]
    for bridge in dependent_bridges:
        query= f'''
                match (ontoBridge:OntoBridge)--(class:CIM)<-[:IN_CAT]-(nodes){bridge.get_cim()}(node)-[:IN_CAT]->(super_class:CIM)--(super_onto_bridge)
                    WHERE ontoBridge.uri = $bridge AND node.{current_bridge.cim_prop_name}=$identifier AND super_onto_bridge.uri=$super_uri AND
                    NOT EXISTS {'{'}
                        MATCH (nodes)-[rel]->()
                        WHERE type(rel) = ontoBridge.label
                    {'}'}
                    set nodes.`_lastModified`=timestamp()
            '''
        params = {"bridge":bridge.bridge_uri, "identifier": cim[current_bridge.cim_prop_name], "super_uri":bridge.super_bridge_uri}
        print(neo4j_conn.execute_query(query, params))
    return True
    
consumer = KafkaConsumer('test_topic', bootstrap_servers=['kafka:9092'], group_id='group1', auto_offset_reset="earliest")
for msg in consumer:
    value = msg.value.decode('utf-8')
    json_object = json.loads(value)
    json_object = clean_message(json_object)
    cim_object = process_node(json_object)
    if cim_object is not None:
        print("Created relation")
        reset_candidates(cim_object)
    