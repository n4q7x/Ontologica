<div align="center">
  <img src="logo.png" width="400" style="padding: 40px;">
</div>


# Table of Contents

- [About](#about)
- [Background](#background)
- [Code](#code)
- [Conceptual Foundation](#conceptual-foundation)
- [Data Model](#data-model)
- [Design](#design)
- [Description](#description)
- [Documentation](#documentation)
- [Examples](#examples)
- [Features](#features)
- [Formalization](#formalization)
- [Functions](#functions)
- [Funding](#funding)
- [Goals](#goals)
- [History](#history)
- [Homepage](#homepage)
- [Motivation](#motivation)
- [Pip](#pip)
- [Prototypes](#prototypes)
- [Questions](#questions)
- [Related tools](#related-tools)
- [Research](#research)
- [Theory](#theory)
- [Tests](#tests)
- [To Do](#to-do)
- [Uses](#uses)
- [Quotes](#quotes)


# About

- Ontologica can automate inferences over ontologies.
- Ontologica can be used as a database.
- Ontologica can be used as a knowledge base.
- Ontologica can be used as a research tool.
- Ontologica can be used as a semantic web tool.
- Ontologica can be used as an aid to clear thinking.
- Ontologica can be used as an aid to creative thinking.
- Ontologica can be used as an aid to insightful thinking.
- Ontologica can be used as an automated theorem prover.
- Ontologica can be used as the backend of a RAG LLM system.
- Ontologica can be used to create models of reality.
- Ontologica can be used to create models of society.
- Ontologica can be used to create models of the world.
- Ontologica can be used to help one think more accurately.
- Ontologica can be used to help one think more precisely.
- Ontologica can be used to help one think more rigorously.
- Ontologica can be used to help one think more systematically.
- Ontologica can be used to organize very large bodies of data.
- Ontologica can be used to organize very large bodies of information.
- Ontologica can be used to organize very large bodies of knowledge.
- Ontologica can check for logical inconsistencies.
- Ontologica can integrate between different data schemas.
- Ontologica can model natural language discourse.
- Ontologica can structure projects and workflows.
- Ontologica can visualize formal ontologies.
- Ontologica is a formal ontology editor.
- Ontologica is a formal ontology tool.
- Ontologica is a work in progress.
- Ontologica is by Julius Hamilton.
- Ontologica is interoperable with RDF.
- Ontologica is programmed in Python.
- You can ask questions by querying your ontology in Ontologica.
- You can become more aware of what you yet do not know, in Ontologica.
- You can create models of map data in Ontologica.
- You can identify gaps in your knowledge, in Ontologica.
- You can model any kind of conceptual domain in Ontologica.
- You can systematically pinpoint avenues for completing missing information in Ontologica.
- You can use Ontologica for open-source intelligence.
- You can use Ontologica to formalize law.
- You can use Ontologica to formalize rule systems.
- Ontologica can be used as a universal productivity tool.

# Background

My interest in knowledge graphs and formal ontologies took hold in 2023 with the advent of user-facing large language models (namely, ChatGPT). Though I was interested in computer programming, philosophy, linguistics, semantic precision, rigorous analysis, logical reasoning, the formalization of meaning, and the automation of natural language related-processes before that, there was something about LLMs that really captured my imagination and set me on a research journey to try to think about how we could use deterministic computer programs to draw logical inferences based on conceptual models of reality. I realized that I needed to understand the foundations of mathematics and logic much better, so I have been studying those for the past 3 years.


# Conceptual Foundation

For the conceptual foundations of Ontologica, see `/docs/conceptualfoundations.md`.

# Data model

When you create an ontology, you essentially create an empty set, *Things*.

In this formalization of Ontologica, we choose to model the ontology as a set, because:

- the order of the elements does not matter
- we do not allow duplicate elements (i.e., "indiscernibles are identical")

When you add a thing to an ontology, there are two ways of thinking about this.

One is, the ontology stays the same, but something *about* it (i.e., the records that are a part of it) has changed. But this is still a change in *what exists*, because it means the *fact* "such as such records are in *this ontology*" no longer exists in this ontology, whereas some new fact does.

The second is, this is a different ontology. The first ontology was an argument to a function that creates a new ontology. The old ontology has been consumed, and no longer exists.

We can always choose to move back and forth between the perspective of "it's the same thing, but something about it changed" and "we deleted the old thing and created a new one".




# Design

Ontologica aims to set a new standard for the usability of formal ontology tools.


# Features
- create ontologies
- delete ontologies
- edit ontologies
- add records to ontologies
- delete records from ontologies
- modify records in ontologies
- run functions over ontologies
- export data
- import data




# Functions


This is the current forefront of where my theorization is taking me.

I think there are a couple different ways we can think about functions.

Sometimes, we can act on a certain object, and change something about it. Sometimes, the way it changes, in regard to that action, is deterministic. There is only one way it will change. Hence, there is a functional relationship between what action we choose, and what change will occur.

When we act on an object, we are choosing a type of action. Given that the action is classified by a type, it naturally opens the possibility that that action has an identity of its own; it can exist independently from the thing it is acting on; and in fact, it can be applied to other things, as well. This is how we can move from the perspective of an action to a function: a single action on a single object implies in the background a general function which for any entity of that type, acts on it in the same way.


The problem with trying to reduce the notion of action as composed of more fundamental actions, just like entities and predicates, we end up still having to still choose some kind of primitive action, like string concatenation, or a successor function, or projection functions in the idea of computable numbers, etc.

WIP



# History

For my personal history of formal ontologies, check out my document "History.md" in `/docs`.


# Motivation

I believe that formal ontologies can make the world more:

- efficient
- prosperous
- truthful
- fair
- free
- just
- logical
- safe
- happy

# Related tools

- Spacy
- CQL
- Protege
- Haskell
- Palantir
- Prolog
- Neo4j
- Gremlin
- GraphQL (?)
- SQL

# Prototypes

The following are envisioned examples of what it would be like to use Ontologica. These examples will then be implemented in code.

## Example 1

Create an Ontology from scratch:

```python

import ontology

my_ontology = ontology.Ontology()

```

## Example 2

Creating an ontology by loading from a local data tile.


# Similar tools


# Tests

## 


# To Do

- refactor repo heavily

# Tools


# Uses

Formal ontologies can be used for:

- recording information
- retrieving information
- checking for logical consistency
- checking for knowledge completeness
- automating processes
- discovering new things


# Quotes

- Bertrand russell, the new logic makes us more creative rather than constraining our thought.