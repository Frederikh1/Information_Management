//3.3 Ontobridge-label trigger
CALL apoc.trigger.add('ontobridge_label',
  'UNWIND $createdNodes AS node
  WITH node
  WHERE node.uri CONTAINS "http://www.semanticweb.org/information_management/ontobridge#"
  SET node:OntoBridge
  RETURN count(*)',
  {phase:'before'})