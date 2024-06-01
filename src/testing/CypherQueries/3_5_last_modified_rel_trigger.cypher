//3.5 last modified rel trigger
CALL apoc.trigger.add(
  'updateLastModifiedOnRelationCreate',
  'UNWIND $createdRelationships AS rel
   WITH STARTNODE(rel) AS a, ENDNODE(rel) AS b
   WHERE NOT ("_NsPrefix" IN labels(a) OR "_NsPrefix" IN labels(b))
   SET a._lastModified = timestamp(), b._lastModified = timestamp()',
  {phase:'before'}
)