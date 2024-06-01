//3.2 CIM-label trigger
CALL apoc.trigger.add('CIM_label',
  'UNWIND $createdNodes AS node
  WITH node
  WHERE node.uri CONTAINS "http://iec.ch/TC57/CIM-generic#"
  SET node:CIM
  RETURN count(*)',
  {phase:'before'})