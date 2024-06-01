docker build . -t node_consumer:latest 
docker run --rm -e ENABLE_INIT_DAEMON=false --network neo4j-net --name node_consumer node_consumer