
This document is for designing and prototyping what it will actually be to use Ontologica. I will then backfill these syntax specifications with tests and finally implement code passing those tests.




# API

## Instantiating and loading ontologies

```python
>>> import ontologica
```

```python
>>> import ontology
```

```python
>>> from Ontologica import Ontology
```

```python
>>> from Ontologica import Ontology, Thing, Atom, Predicate, Statement
```

```python
>>> onto = Ontology()
```

```python
>>> ontology = Ontology()
```

```python
>>> ontology = Ontology("my-db.txt")
```

```python
>>> ontology = Ontology("birds")
```

```python
>>> ontology = Ontology(subject="birds")
```

```python
>>> ontology = Ontology(subject="birds", type="RDF")
```

```python
>>> ontology = Ontology(subject="birds", lexicon="bfo-medical", type="sqlite3")
```

```python
>>> ontology = Ontology.from_json("data.json")
```

```python
>>> ontology = Ontology.from_json("./data.json")
```

```python
>>> ontology = Ontology.load("https://somedata.ttl")
```

```python
>>> ontology = Ontology.load("https://somedata.owl")
```

## Merging, interacting, and integrating ontologies

```python
>>> from ontology1 as ("db1.db"), ontology2 as ("extra.csv", schema="schema.ont"):
...    return Ontology.merge(ontology1, ontology2)
```

```python
>>> integrated = Ontology.integrate(onto1, onto2, onto3, schema="mapping.cql")
```

## Adding Elements Efficiently


## Modifying and Editing (what entities added, which predicates hold true)



## Importing existing vocabularies from standardized lexicons hosted online at ontologi.ca (???)



## dump your ontology locally to a file

## send your ontology over the internet in .json?

## turn your ontology into a semantic web page, serving live

## link your ontology to someone else's. now changed are synced, must be kept up to date, etc.


## import logic features

### see which nodes have similar neighborhoods. type inference.

### see the first order logical theory describing your ontology.

### run integrity constraints / checks. ontology must be complete. etc. green check marks at cli tell you that you cannot push / publish your ontology to the datanet until it has attained completeness.

### examples of the kinds of queries you can write, beyond lame obvious ones. its not about "what is this person's name"? it's about "find me people (in the world, on the internet) with such and such a description. etc.



# longterm vision for interactive usage

## public a data feed to the datanet

## walk / traverse / query net for certain questions



# CLI








# GUI