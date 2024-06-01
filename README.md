# Information_Management

## Docker Compose commands
### compose up
```bash
docker compose up --build -d
```
### compose down
```bash
docker compose down --remove-orphans
```

# Data Integration commands
## run from root 
``` bash
cd .\Information_Management\
```
## Install Requirements - VScode
```bash
python installRequirements.py
```
## Install Requirements - Ubuntu Terminal
``` bash
python3 installRequirements.py
```

## IEC61850 Data ingestion 
### VScode
``` bash
python -m src.Data_Integration.Python_Scripts.main --config src/Data_Integration/Python_Scripts/config_iec.json
```
### Ubuntu Terminal
``` bash
python3 -m src.Data_Integration.Python_Scripts.main --config src/Data_Integration/Python_Scripts/config_iec.json
```

## CIM Data ingestion 
### VScode
``` bash
python -m src.Data_Integration.Python_Scripts.main --config src/Data_Integration/Python_Scripts/config_cim.json
```
### Ubuntu Terminal
``` bash
python3 -m src.Data_Integration.Python_Scripts.main --config src/Data_Integration/Python_Scripts/config_cim.json
```

## Quick Neo4j Database Clean up script 
### VScode
``` bash
python .\CleanUpNeo4jGraphDatabase.py
```
### Ubuntu Terminal
``` bash
python3 CleanUpNeo4jGraphDatabase.py
```

## Unittesting Commands
### VSCode
``` bash
python -m src.testing.testingMain -v
```
### Ubuntu Terminal
``` bash
python3 -m src.testing.testingMain -v
```


## Inference kafka consumer
### Build
```
docker build . -t node_consumer:latest
```

### Run
```
docker run --rm -e ENABLE_INIT_DAEMON=false --network information_management_neo4j-net node_consumer
```
