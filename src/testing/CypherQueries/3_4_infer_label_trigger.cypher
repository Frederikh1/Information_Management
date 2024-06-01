//3.4 infer label trigger
CALL apoc.trigger.add('addLabelToNewNodes',
  'UNWIND $createdNodes AS newNode
   MATCH (newNode)-[:IN_CAT]->(classNode:Class)
   CALL apoc.create.addLabels(newNode, [classNode.name]) YIELD node
   RETURN count(node)',
  {phase:'before'})