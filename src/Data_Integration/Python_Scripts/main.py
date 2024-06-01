import rdflib, time
import pandas as pd
from src.Data_Integration.Python_Scripts.CimMappings import loadCIMMapping
from src.Data_Integration.Python_Scripts.IECMappings import loadIEC61850Mapping
import argparse
import json
from neo4j import GraphDatabase, basic_auth

def mainFunc():
  parser = argparse.ArgumentParser(description='Process an ontology based on the given configuration.')
  parser.add_argument('--config', required=True, help='Path to the configuration file')
  args = parser.parse_args()

  with open(args.config, 'r') as config_file:
      config = json.load(config_file)

  ontology_url = config['ontology_url']
  ontology_format = config['ontology_format']
  mappingStandard = config['mapping_file']

  def getLocalPart(uri):
      pos = -1
      pos = uri.rfind('#')
      if pos < 0:
          pos = uri.rfind('/')
      if pos < 0:
          pos = uri.rindex(':')

      localPart = uri[pos+1:]

      dotPos = localPart.rfind('.')
      if dotPos != -1:
          return localPart[dotPos+1:]
      else:
          return localPart

  def getNamespacePart(uri):
    pos = -1
    pos = uri.rfind('#')
    if pos < 0 :
      pos = uri.rfind('/')
    if pos < 0 :
      pos = uri.rindex(':')
    return uri[0:pos+1]

  def getRelation(uri):
      pos = -1
      pos = uri.rfind('#')
      if pos < 0 :
        pos = uri.rfind('/')
      if pos < 0 :
        pos = uri.rindex(':')
      return uri[pos+1:]

  g = rdflib.Graph()
  g.parse(ontology_url, format=ontology_format)

  simple_query = """
  prefix owl: <http://www.w3.org/2002/07/owl#>
  prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

  SELECT DISTINCT ?c
    WHERE {
      ?c rdf:type owl:Class .
    } """

  if (mappingStandard == "CIM"):
    OntoMappings = loadCIMMapping()
  else:
    OntoMappings = loadIEC61850Mapping()

  def getLoadersFromOnto(onto, rdf_format, mappings):
    g = rdflib.Graph()
    g.parse(onto, format= rdf_format)

    classes_and_props_query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT DISTINCT ?curi (GROUP_CONCAT(DISTINCT COALESCE(?propTypePair, ""); SEPARATOR=",") AS ?props)
    WHERE {
      ?curi rdf:type owl:Class .
      
      OPTIONAL {
        ?curi rdfs:subClassOf* ?superclass .
        ?prop rdfs:domain ?superclass ;
              a owl:DatatypeProperty ;
              rdfs:range ?range .
        BIND (CONCAT(STR(?prop), ";", STR(?range)) AS ?propTypePair)
      }
    } GROUP BY ?curi
    """
  
    cypher_import = {}
    export_ns = set()
    export_mappings = {}

    for row in g.query(classes_and_props_query):
      if getLocalPart(row.curi) not in mappings:
          continue

      export_ns.add(getNamespacePart(row.curi))
      export_mappings[getLocalPart(row.curi)] = str(row.curi)
      cypher = []
      cypher.append("unwind $records AS record")
      cypher.append(f"merge (n:{getLocalPart(row.curi)} {{ `{mappings[getLocalPart(row.curi)]['@uniqueId']}`: record.`{mappings[getLocalPart(row.curi)][mappings[getLocalPart(row.curi)]['@uniqueId']]}` }})")
      cypher.append('WITH n, record')
      cypher.append("MATCH (cat:Class)")
      cypher.append(f'WHERE cat.uri = "{str(row.curi)}"')
      cypher.append('WITH n, record, cat')
      for pair in row.props.split(","):
          split_pair = pair.split(";")
          if len(split_pair) >= 2:
              propName, propType = split_pair
              export_ns.add(getNamespacePart(propName))
              export_mappings[getLocalPart(propName)] = propName
              if getLocalPart(propName) in mappings[getLocalPart(row.curi)] and getLocalPart(propName) != mappings[getLocalPart(row.curi)]['@uniqueId']:
                  cypher.append(f"set n.`{getLocalPart(propName)}` = record.`{mappings[getLocalPart(row.curi)][getLocalPart(propName)]}`")
      cypher.append("merge (n)-[:IN_CAT]->(cat)")
      cypher.append("return count(*) as total")
      cypher_import[getLocalPart(row.curi)] = ' \n'.join(cypher)


    rels_query = """
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT DISTINCT ?rel ?dom ?ran #(GROUP_CONCAT(DISTINCT ?relTriplet ; SEPARATOR=",") AS ?rels)
    WHERE {
        ?rel a ?propertyClass .
        filter(?propertyClass in (rdf:Property, owl:ObjectProperty, owl:FunctionalProperty, owl:AsymmetricProperty,
              owl:InverseFunctionalProperty, owl:IrreflexiveProperty, owl:ReflexiveProperty, owl:SymmetricProperty, owl:TransitiveProperty))

        ?rel rdfs:domain ?dom ;
          rdfs:range ?ran .

        #BIND (concat(str(?rel),';',str(?dom),';',str(?range)) AS ?relTriplet)

      }"""

    for row in g.query(rels_query):

      if getLocalPart(row.dom) not in mappings or getLocalPart(row.ran) not in mappings or getRelation(row.rel) not in mappings:
          continue
      
      export_ns.add(getNamespacePart(row.rel))
      export_mappings[getLocalPart(row.rel)] = str(row.rel)

      cypher = []
      cypher.append("unwind $records AS record")
      cypher.append('CALL n10s.inference.nodesLabelled("' + getLocalPart(row.dom) +'", { catLabel:"Class"})')
      cypher.append("YIELD node as dom")
      cypher.append("WHERE dom." + mappings[getLocalPart(row.dom)]["@uniqueId"] + " = " + "record.`" + mappings[getRelation(row.rel)]["@range"] + "`")
      cypher.append("WITH dom, record")
      cypher.append('CALL n10s.inference.nodesLabelled("' + getLocalPart(row.ran) +'", {  catLabel:"Class" })')
      cypher.append("YIELD node as ran")
      cypher.append("WHERE ran." + mappings[getLocalPart(row.ran)]["@uniqueId"] + " = " + "record.`" + mappings[getRelation(row.rel)]["@domain"] + "`")
      cypher.append("WITH dom, ran")
      cypher.append("MERGE (dom)-[r:`"+ getLocalPart(row.rel) +"`]->(ran)")
      cypher.append("return count(*) as total")
      cypher_import[getRelation(row.rel)] = ' \n'.join(cypher)
    
    nscount = 0
    mapping_export_cypher = []
    
    for ns in export_ns:
      mapping_export_cypher.append("call n10s.nsprefixes.add('" + mappingStandard + "','" + ns + "');")
      nscount+=1
    
    for k in export_mappings.keys():
      mapping_export_cypher.append("call n10s.mapping.add('" + export_mappings[k] + "','" + k + "');")

    return cypher_import ,  mapping_export_cypher

  cypher_import , mapping_defs = getLoadersFromOnto(ontology_url,ontology_format, OntoMappings)

  def insert_data(session, query, frame, batch_size = 300):
      total = 0
      batch = 0
      start = time.time()
      result = None

      while batch * batch_size < len(frame):
          res = session.execute_write( lambda tx: tx.run(query,
            parameters = {'records': frame[batch*batch_size:(batch+1)*batch_size].to_dict('records')}).data())

          total += res[0]['total']
          batch += 1
          result = {"total":total,
                    "batches":batch,
                    "time":time.time()-start}

      return result, total

  uri = "bolt://127.0.0.1:7687"
  user = "neo4j"
  password = "password"
  driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))
  try:
    with driver.session(database="neo4j") as session:
      cypher_import, mapping_defs = getLoadersFromOnto(ontology_url, ontology_format, OntoMappings)

      for q in cypher_import.keys():
        print(f"about to import {q} from file {OntoMappings[q]['@fileName']}")
        df = pd.read_csv(OntoMappings[q]["@fileName"])
        result = insert_data(session, cypher_import[q], df, batch_size=300)
        print(result)

      for md in mapping_defs:
        session.run(md)

  except Exception as e:
    print("Error connecting to Neo4j:", e)
  finally:
    driver.close()
  
if __name__ == "__main__":
    mainFunc() 
    
