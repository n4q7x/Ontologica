{-# LANGUAGE DeriveGeneric #-}

module Onto
  ( Thing(..)
  , Triple(..)
  , Law(..)
  , Ontology(..)
  , emptyOntology
  , addThing
  , assertTripleRaw
  , smartAddTriple
  , hastype
  ) where

import qualified Data.Set as Set
import Data.Set (Set)
import GHC.Generics (Generic)

--------------------------------------------------------------------------------
-- BASIC TYPES
--------------------------------------------------------------------------------

newtype Thing = Thing String
  deriving (Eq, Ord, Show)

data Triple = Triple Thing Thing Thing
  deriving (Eq, Ord, Show, Generic)

data Law = Law
  { lawName :: String
  , lawDesc :: String
  } deriving (Eq, Ord, Show)

--------------------------------------------------------------------------------
-- ONTOLOGY DATA STRUCTURE
--------------------------------------------------------------------------------

data Ontology = Ontology
  { things  :: Set Thing     -- DECLARED *EXPLICITLY* by the user
  , triples :: Set Triple    -- triples, must reference existing Things
  , laws    :: Set Law
  } deriving (Show)

emptyOntology :: Ontology
emptyOntology = Ontology
  { things  = Set.empty
  , triples = Set.empty
  , laws    = Set.empty
  }

--------------------------------------------------------------------------------
-- BASIC OPERATIONS
--------------------------------------------------------------------------------

-- Add a Thing explicitly
addThing :: Ontology -> Thing -> Ontology
addThing ont t =
  ont { things = Set.insert t (things ont) }

-- Raw triple assertion (NO CHECKS, DOES NOT ADD THINGS EITHER)
assertTripleRaw :: Ontology -> Triple -> Ontology
assertTripleRaw ont tri =
  ont { triples = Set.insert tri (triples ont) }

--------------------------------------------------------------------------------
-- QUERY FUNCTIONS
--------------------------------------------------------------------------------

-- Does (x, hastype, t) exist?
hastype :: Ontology -> Thing -> Thing -> Bool
hastype ont x t =
  Set.member (Triple x (Thing "hastype") t) (triples ont)

--------------------------------------------------------------------------------
-- SMART TRIPLE CONSTRUCTOR
--------------------------------------------------------------------------------

-- REQUIREMENTS:
-- 1. All three Things must be declared in ont.things
-- 2. The predicate Thing must have type "predicate" in the ontology
--
-- If those conditions are not met, return Left <error>.
--
smartAddTriple :: Ontology -> Thing -> Thing -> Thing
               -> Either String Ontology
smartAddTriple ont s p o =
  let missing =
        [ t | (name,t) <- [("subject",s),("predicate",p),("object",o)]
            , not (Set.member t (things ont)) ]
  in case missing of
       (t:_) ->
         Left ("Triple uses undeclared Thing: " ++ show t)

       [] ->
         if hastype ont p (Thing "predicate")
           then Right $
             ont { triples = Set.insert (Triple s p o) (triples ont) }
           else Left $
             "Predicate error: " ++ show p ++
             " does not have type 'predicate'."
