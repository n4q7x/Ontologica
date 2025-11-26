
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





# CLI








# GUI