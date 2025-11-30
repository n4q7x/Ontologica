module Onto 
  ( Thing(..)
  , Triple(..)
  , Ontology(..)
  , emptyOntology
  , addThing
  , assertTripleRaw
  , smartAddTriple
  , hastype
  ) where

import Data.List (find)

-- BASIC TYPES ---------------------------------------------------------------

newtype Thing = Thing String
  deriving (Eq, Ord, Show)

-- A triple is just Thing Thing Thing
data Triple = Triple Thing Thing Thing
  deriving (Eq, Ord, Show)

-- The ontology is just a bag of triples (for now)
data Ontology = Ontology
  { triples :: [Triple]
  } deriving (Show)

emptyOntology :: Ontology
emptyOntology = Ontology { triples = [] }


-- BASIC OPERATIONS ----------------------------------------------------------

addThing :: Ontology -> Thing -> Ontology
addThing ont _ = ont
-- Nothing to do: a Thing needs no declaration.


assertTripleRaw :: Ontology -> Triple -> Ontology
assertTripleRaw ont t = ont { triples = t : triples ont }


-- QUERYING THE ONTOLOGY -----------------------------------------------------

-- Check if (x, hastype, t) exists
hastype :: Ontology -> Thing -> Thing -> Bool
hastype (Ontology ts) x t =
  any (\(Triple s p o) -> s == x && p == Thing "hastype" && o == t) ts


-- SMART CONSTRUCTOR ---------------------------------------------------------

-- REQUIREMENT:
-- To construct Triple s p o, we must have hastype(p) == predicate inside the ontology.
smartAddTriple :: Ontology -> Thing -> Thing -> Thing -> Either String Ontology
smartAddTriple ont s p o =
  if hastype ont p (Thing "predicate")
     then Right (assertTripleRaw ont (Triple s p o))
     else Left $ "Cannot use " ++ show p ++ 
                 " as predicate: missing hastype(" 
                 ++ show p ++ ", predicate)"
