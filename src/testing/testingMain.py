import unittest, argparse, os, glob, io, sys, time
from unittest.mock import patch
from ..Data_Integration.Python_Scripts import main
from neo4j import GraphDatabase

class Neo4j_Base_Test_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))
        cls.clear_database()  
        cls.remove_constraints()  
        cls.database_config() 

    @classmethod
    def clear_database(cls):
        with cls.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    @classmethod
    def remove_constraints(cls):
        with cls.driver.session() as session:
            try:
                result = session.run("SHOW CONSTRAINTS")
                constraints = result.data()
                for constraint in constraints:
                    if "n10s_unique_uri" in constraint['name']:
                        session.run(f"DROP CONSTRAINT {constraint['name']}")
            except Exception as e:
                print(f"Failed to remove constraints: {e}")

    @classmethod
    def database_config(cls):
        query_folder_path = "./src/testing/CypherQueries/"
        cypher_files = sorted(glob.glob(os.path.join(query_folder_path, '*.cypher')))
        with cls.driver.session() as session:
            for file_path in cypher_files:
                try:
                    with open(file_path, 'r') as file:
                        query = file.read()
                        session.run(query)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    @classmethod
    def tearDownClass(cls):
        cls.clear_database() 
        cls.driver.close()

class DataIngestionUtility:
    @staticmethod
    def setUpImporter(config_path):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch('argparse.ArgumentParser.parse_args') as mock_args:
                mock_args.return_value = argparse.Namespace(config=config_path)
                return main.mainFunc()

    @staticmethod
    def run_integration_test(driver, config_path):
        DataIngestionUtility.setUpImporter(config_path)
        with driver.session() as session:
            result = session.run("MATCH (n) RETURN count(n) as count")
            count = result.single()["count"]
            assert count > 0, "No nodes created after ingestion."

class Test_Creation_and_Relationships(Neo4j_Base_Test_Case):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        DataIngestionUtility.run_integration_test(cls.driver, 'src/Data_Integration/Python_Scripts/config_iec.json')
        DataIngestionUtility.run_integration_test(cls.driver, 'src/Data_Integration/Python_Scripts/config_cim.json')        
      
    def test_01_substation_relation(self): 
        """
        01. Test the automatic assignment of the 'SameAs' relationship between Substation and tSubstation.
        """
        with self.driver.session() as session:
            create_cim_substation = """
                Merge (t:Substation {name:"aarup"})
                    with t
                    Match (c:Class) WHERE c.uri="http://iec.ch/TC57/CIM-generic#Substation"
                    with t, c
                    MERGE (t)-[:IN_CAT]->(c)
            """
            
            session.run(create_cim_substation)
            
            create_iec_substation = """
                Merge (t:tSubstation {name:"årup"})
                    with t
                    Match (c:Class) WHERE c.uri="http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#tSubstation"
                    with t, c
                    MERGE (t)-[:IN_CAT]->(c)
            """
            
            session.run(create_iec_substation)
            time.sleep(5)
            query = """
            MATCH (cim:Substation{name:"aarup"})-[rel:SameAs]-() return cim, rel as ontobridge
            """
            result = session.run(query)
            relationships = list(result)
            
            self.assertTrue(relationships, "No 'SameAs' relationships found between 'Bay' and 'tBay'")
            
            for relationship in relationships:
                self.assertEqual(relationship["ontobridge"].type, 'SameAs', "The relationship type is not 'SameAs'")
                
    def test_02_voltagelevel_relation(self): 
        """
        02. Test the automatic assignment of the 'SameAs' relationship between VoltageLevel and tVoltageLevel.
        """
        with self.driver.session() as session:
            create_cim_voltagelevel = """
                Merge (t:VoltageLevel {name:"aarup_volt", highVoltageLimit:325, lowVoltageLimit:100, mRID:randomUUID()})
                    with t
                    Match (c:Class) WHERE c.uri="http://iec.ch/TC57/CIM-generic#VoltageLevel"
                    Match (super:Substation{name:"aarup"})
                    with t, c, super
                    MERGE (t)-[:IN_CAT]->(c)
                    Merge (super)<-[:Substation]-(t)
            """
            
            session.run(create_cim_voltagelevel)
            
            create_iec_tvoltagelevel= """
                Merge (t:tVoltageLevel {name:"årup_volt", desc:"voltagelevel in sønderborg"})
                    with t
                    Match (c:Class) WHERE c.uri="http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#tVoltageLevel"
                    Match (super:tSubstation{name:"årup"})
                    with t, c, super
                    MERGE (t)-[:IN_CAT]->(c)
                    Merge (super)-[:VoltageLevel]->(t)
            """
            
            session.run(create_iec_tvoltagelevel)
            time.sleep(5)
            query = """
            MATCH (cim:VoltageLevel{name:"aarup_volt"})-[rel:SameAs]-() return cim, rel as ontobridge
            """
            result = session.run(query)
            relationships = list(result)
            
            self.assertTrue(relationships, "No 'SameAs' relationships found between 'Bay' and 'tBay'")
            
            for relationship in relationships:
                self.assertEqual(relationship["ontobridge"].type, 'SameAs', "The relationship type is not 'SameAs'")
                
    def test_06_voltagelevel_relation(self): 
        """
        06. Tests that voltagelevel candidates are semantically relevant. Therefore no 'SameAs' relation must be found
        """
        with self.driver.session() as session:
            create_cim_voltagelevel = """
                Merge (t:VoltageLevel {name:"candidate_aa", highVoltageLimit:325, lowVoltageLimit:100, mRID:randomUUID()})
                    with t
                    Match (c:Class) WHERE c.uri="http://iec.ch/TC57/CIM-generic#VoltageLevel"
                    Match (super:Substation{name:"Aarhus"})
                    with t, c, super
                    MERGE (t)-[:IN_CAT]->(c)
                    Merge (super)<-[:Substation]-(t)
            """
            
            session.run(create_cim_voltagelevel)
            
            create_iec_tvoltagelevel= """
                Merge (t:tVoltageLevel {name:"candidate_å", desc:"voltagelevel in sønderborg"})
                    with t
                    Match (c:Class) WHERE c.uri="http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#tVoltageLevel"
                    Match (super:tSubstation{name:"årup"})
                    with t, c, super
                    MERGE (t)-[:IN_CAT]->(c)
                    Merge (super)-[:VoltageLevel]->(t)
            """
            
            session.run(create_iec_tvoltagelevel)
            time.sleep(5)
            query = """
            MATCH (cim:VoltageLevel{name:"candidate_aa"})-[rel:SameAs]-() return cim, rel as ontobridge
            """
            result = session.run(query)
            relationships = list(result)
            
            self.assertFalse(relationships, "'SameAs' relationships found between unrelated voltagelevel and tvoltagelevel'")
            
            for relationship in relationships:
                self.assertEqual(relationship["ontobridge"].type, 'SameAs', "The relationship type is not 'SameAs'")
                
    def test_03_bays_relation(self): 
        """
        03. Test the automatic assignment of the 'SameAs' relationship between Bay and tBay.
        """
        with self.driver.session() as session:
            create_query = """
            MERGE (t:Bay {
                mRID: "1234-5678-9876-5432", 
                aliasName: "newTaest", 
                description: "Taest", 
                name: "HovedTaest", 
                bayEnergyMeasFlag: true, 
                bayPowerMeasFlag: true
            })
            WITH t
            MATCH (c:Class) WHERE c.uri="http://iec.ch/TC57/CIM-generic#Bay"
            MATCH (super:VoltageLevel{name:"aarup_volt"})
            MATCH (super)-[:Substation]-(sub)
            WITH t, c, super, sub
            MERGE (t)-[:IN_CAT]->(c)
            MERGE (super)<-[:VoltageLevel]-(t)
            MERGE (t)<-[:Bays]-(super)
            MERGE (sub)<-[:Substation]-(t)
            MERGE (sub)-[:Bays]->(t)
            RETURN t, c, super, sub
            """
            create_result = session.run(create_query)
            created_data = create_result.single()
            self.assertIsNotNone(created_data, "Failed to create Bay and its relationships")
            
            create_query = """
            MERGE (t:tBay {
                desc: "Tæst", 
                name: "HovedTæst", 
                tConductingEquipmentId: "StrømførendeUdstyr1"
            })
            WITH t
            MATCH (c:Class) WHERE c.uri="http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#tBay"
            MATCH (super:tVoltageLevel{name:"årup_volt"})
            WITH t, c, super
            MERGE (t)-[:IN_CAT]->(c)
            MERGE (super)-[:Bay]->(t)
            RETURN t, c, super
            """
            created_data = session.run(create_query).single()
            self.assertIsNotNone(created_data, "Failed to create tBay and its relationships")
            
            time.sleep(5)
            query = """
            MATCH (cim:Bay{name:"HovedTaest"})-[rel:SameAs]-() return cim, rel as ontobridge
            """
            result = session.run(query)
            relationships = list(result)
            
            self.assertTrue(relationships, "No 'SameAs' relationships found between 'Bay' and 'tBay'")
            
            for relationship in relationships:
                self.assertEqual(relationship["ontobridge"].type, 'SameAs', "The relationship type is not 'SameAs'")
                
    def test_04_basevoltage_relation(self): 
        """
        04. Test the automatic assignment of the 'SameAs' relationship between BaseVoltage and tVoltage.
        """
        with self.driver.session() as session:
            create_cim_basevoltage = """
                Merge (node:BaseVoltage{name: "basevolt_aarup", aliasName: "Oozz", description: "Tetany", nominalVoltage: "11000v", mRID:randomUUID()})
                    with node
                    Match (super:CIM{uri:"http://iec.ch/TC57/CIM-generic#BaseVoltage"})
                    Match (v:VoltageLevel{name:"aarup_volt"})
                    with node, super, v
                    MERGE (node)-[:IN_CAT]->(super)
                    MERGE (node)-[:VoltageLevel]->(v)
                    MERGE (node)<-[:BaseVoltage]-(v)
            """
            
            session.run(create_cim_basevoltage)
            
            create_iec_tvoltage= """
                MERGE (node:tVoltage{value:"11kV"})
                    with node
                    Match (super:IEC61850{uri:"http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#tVoltage"})
                    Match (v:tVoltageLevel{name:"årup_volt"})
                    with node, super, v
                    MERGE (node)-[:IN_CAT]->(super)
                    MERGE (node)<-[:Voltage]-(v)
            """
            
            session.run(create_iec_tvoltage)
            time.sleep(5)
            query = """
            MATCH (cim:BaseVoltage{name:"basevolt_aarup"})-[rel:SameAs]-() return cim, rel as ontobridge
            """
            result = session.run(query)
            relationships = list(result)
            
            self.assertTrue(relationships, "No 'SameAs' relationships found between 'Bay' and 'tBay'")
            
            for relationship in relationships:
                self.assertEqual(relationship["ontobridge"].type, 'SameAs', "The relationship type is not 'SameAs'")
    
    def test_05_redundancy_relation(self): 
        """
        05. Tests automatic assignment of "SameAs" for Substation and VoltageLevel. Validates that ingestion order is irrelevant
        """
        with self.driver.session() as session:
            create_cim_voltagelevel = """
                Merge (t:VoltageLevel {name:"soenderborg_volt", highVoltageLimit:325, lowVoltageLimit:100, mRID:randomUUID()})
                    with t
                    Match (c:Class) WHERE c.uri="http://iec.ch/TC57/CIM-generic#VoltageLevel"
                    with t, c
                    MERGE (t)-[:IN_CAT]->(c)
            """
            
            session.run(create_cim_voltagelevel)
            
            create_iec_tvoltagelevel= """
                Merge (t:tVoltageLevel {name:"sønderborg_volt", desc:"voltagelevel in sønderborg"})
                    with t
                    Match (c:Class) WHERE c.uri="http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#tVoltageLevel"
                    with t, c
                    MERGE (t)-[:IN_CAT]->(c)
            """
            
            session.run(create_iec_tvoltagelevel)
            time.sleep(5)
            query = """
                MATCH (cim:VoltageLevel{name:"soenderborg_volt"})-[rel:SameAs]-() return cim, rel as ontobridge
            """
            result = session.run(query)
            relationships = list(result)
            
            self.assertFalse(relationships, "Relationship found between 'VoltageLevel' and 'tVoltageLevel'")
            
            create_cim_substation = """
                Merge (t:Substation {name:"taest"})
                    with t
                    Match (c:Class) WHERE c.uri="http://iec.ch/TC57/CIM-generic#Substation"
                    with t, c
                    MERGE (t)-[:IN_CAT]->(c)
            """
            
            session.run(create_cim_substation)
            
            create_iec_substation = """
                Merge (t:tSubstation {name:"tæst"})
                    with t
                    Match (c:Class) WHERE c.uri="http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#tSubstation"
                    with t, c
                    MERGE (t)-[:IN_CAT]->(c)
            """
            
            session.run(create_iec_substation)
            
            add_voltage_substation_relation_cim = """
            MATCH (t:VoltageLevel {name:"soenderborg_volt"})
            Match (super:Substation{name:"taest"})
            with t, super
            Merge (super)<-[:Substation]-(t)
            """
            session.run(add_voltage_substation_relation_cim)
            
            add_tvoltage_substation_iec = """
            MATCH (t:tVoltageLevel {name:"sønderborg_volt"})
            Match (super:tSubstation{name:"tæst"})
            with t, super
            Merge (super)-[:VoltageLevel]->(t)
            """
            session.run(add_tvoltage_substation_iec)
            time.sleep(10)
            query = """
            MATCH (cim:VoltageLevel{name:"soenderborg_volt"})-[rel:SameAs]-() return cim, rel as ontobridge
            """
            result = session.run(query)
            relationships = list(result)
            
            self.assertTrue(relationships, "No 'SameAs' relationships found between 'VoltageLevel' and 'tVoltageLevel'")
            
            for relationship in relationships:
                self.assertEqual(relationship["ontobridge"].type, 'SameAs', "The relationship type is not 'SameAs'")


        
if __name__ == '__main__':
    
    runner = unittest.TextTestRunner()
    combined_test_suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(Test_Creation_and_Relationships)
    ])
    runner.run(combined_test_suite)

