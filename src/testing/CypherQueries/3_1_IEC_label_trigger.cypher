//3.1 IEC-label trigger
CALL apoc.trigger.add('addIEC61850Label',
  'UNWIND $createdNodes AS node
  WITH node
  WHERE node.uri CONTAINS "http://www.semanticweb.org/information-management/mapping-cutout/iec-61850#"
  SET node:IEC61850
  RETURN count(*)',
  {phase:'before'})
