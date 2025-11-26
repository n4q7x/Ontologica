# Ontologica – Example Usage Sketches

These are example “design mockups” of how Ontologica *could* look in use.
They’re intended as input for tests and API design, not as a guaranteed
description of the current implementation.

---

## Example 1 – Tiny toy ontology (people & predicates)

A very small, abstract example that exercises the core operations:

```python
>>> from ontology import Ontology
>>> onto = Ontology()

# Create some entities and predicates
>>> alice = onto.add("Alice")
Thing(label='Alice', id=1)
>>> bob = onto.add(label="Bob")
Thing(label='Bob', id=2)
>>> carol = onto.add("Carol")
Thing(label='Carol', id=3)

>>> likes = onto.add_predicate("likes")
Predicate(label='likes', id=4)
>>> hates = onto.add_predicate("hates")
Predicate(label='hates', id=5)

# Bind a few facts
>>> onto.bind(alice, likes, bob)
Statement(label='Alice likes Bob', id=6)
>>> onto.bind(alice, likes, carol)
Statement(label='Alice likes Carol', id=7)
>>> onto.bind(bob, hates, carol)
Statement(label='Bob hates Carol', id=8)
```

### Enumerating and showing the ontology

```python
>>> onto.enumerate()
Enumerated 3 statements over 3 entities and 2 predicates

>>> onto.show()
Entities:
  [1] Thing(label='Alice')
  [2] Thing(label='Bob')
  [3] Thing(label='Carol')

Predicates:
  [4] Predicate(label='likes')
  [5] Predicate(label='hates')

Statements:
  [6] Statement(label='Alice likes Bob', id=6, truth=None)
       subject:   [1] Alice
       predicate: [4] likes
       object:    [2] Bob
  [7] Statement(label='Alice likes Carol', id=7, truth=None)
       subject:   [1] Alice
       predicate: [4] likes
       object:    [3] Carol
  [8] Statement(label='Bob hates Carol', id=8, truth=None)
       subject:   [2] Bob
       predicate: [5] hates
       object:    [3] Carol
```

### Classification and completeness

```python
>>> onto.classify({
...     (alice, likes, bob): True,
...     (alice, likes, carol): False,
...     (bob, hates, carol): True,
... })
Classification updated:
  true: 2, false: 1, unknown: 0

>>> onto.show(limit=None)
Statements:
  [6] Statement(label='Alice likes Bob', id=6, truth=True)
  [7] Statement(label='Alice likes Carol', id=7, truth=False)
  [8] Statement(label='Bob hates Carol', id=8, truth=True)

>>> onto.check_completeness(scope="alice feelings")
Completeness(scope='alice feelings') -> 0.66 (2/3 relevant statements classified)
```

### Slicing and querying

```python
>>> onto.slice(subject="Alice")
[('Alice', 'likes', 'Bob', True),
 ('Alice', 'likes', 'Carol', False)]

>>> onto.slice(predicate="hates", include_truth=True)
[('Bob', 'hates', 'Carol', True)]

>>> onto.query("predicate='likes' AND truth=True")
Query matched 1 statement -> ['Alice likes Bob']

>>> onto.query("subject='Alice' AND truth=False")
Query matched 1 statement -> ['Alice likes Carol']
```

### Snapshots / persistence

```python
>>> onto.push(target="local://snapshots/people.snap")
Snapshot written to local://snapshots/people.snap (8 nodes total)

>>> onto.save_json("people_ontology.json")
Exported 8 nodes to people_ontology.json

>>> onto.save_pickle("people_ontology.pkl")
Pickle written to people_ontology.pkl
```

---

## Example 1 (CLI equivalent) – People & predicates

```bash
$ python3 src/cli/cli.py new -f people.pkl
[ontologica] Created new ontology at 'people.pkl'

$ python3 src/cli/cli.py add -f people.pkl "Alice"
[ontologica] Added Thing 'Alice' (id=1)

$ python3 src/cli/cli.py add -f people.pkl "Bob"
[ontologica] Added Thing 'Bob' (id=2)

$ python3 src/cli/cli.py add -f people.pkl "Carol"
[ontologica] Added Thing 'Carol' (id=3)

$ python3 src/cli/cli.py add-predicate -f people.pkl "likes"
[ontologica] Added Predicate 'likes' (id=4)

$ python3 src/cli/cli.py add-predicate -f people.pkl "hates"
[ontologica] Added Predicate 'hates' (id=5)

$ python3 src/cli/cli.py bind -f people.pkl "Alice" "likes" "Bob"
[ontologica] Added Statement 'Alice likes Bob' (id=6)

$ python3 src/cli/cli.py bind -f people.pkl "Alice" "likes" "Carol"
[ontologica] Added Statement 'Alice likes Carol' (id=7)

$ python3 src/cli/cli.py bind -f people.pkl "Bob" "hates" "Carol"
[ontologica] Added Statement 'Bob hates Carol' (id=8)
```

Show the ontology:

```bash
$ python3 src/cli/cli.py show -f people.pkl
Entities:
  [1] Alice
  [2] Bob
  [3] Carol

Predicates:
  [4] likes
  [5] hates

Statements:
  [6] (Alice) -[likes]-> (Bob)    truth: ?
  [7] (Alice) -[likes]-> (Carol)  truth: ?
  [8] (Bob)   -[hates]-> (Carol)  truth: ?
```

Slice and query via CLI:

```bash
$ python3 src/cli/cli.py slice -f people.pkl --subject "Alice"
[Alice] -[likes]-> [Bob]    truth: ?
[Alice] -[likes]-> [Carol]  truth: ?

$ python3 src/cli/cli.py query -f people.pkl "predicate='likes'"
Matched 2 statements:
  [6] Alice likes Bob
  [7] Alice likes Carol
```

---

## Example 2 – Task dependencies (project planning ontology)

This one models tasks and `depends_on` relationships, and uses completeness to check if the dependency graph is “fully known”.

```python
>>> from ontology import Ontology
>>> onto = Ontology()

# Create tasks as entities
>>> setup_env   = onto.add("Setup dev environment")
Thing(label='Setup dev environment', id=1)
>>> design_spec = onto.add("Write design spec")
Thing(label='Write design spec', id=2)
>>> impl_core   = onto.add("Implement core module")
Thing(label='Implement core module', id=3)
>>> write_tests = onto.add("Write tests")
Thing(label='Write tests', id=4)
>>> review_pr   = onto.add("Review pull request")
Thing(label='Review pull request', id=5)

# Create predicates
>>> depends_on = onto.add_predicate("depends_on")
Predicate(label='depends_on', id=6)
>>> blocks = onto.add_predicate("blocks")
Predicate(label='blocks', id=7)

# Add dependency facts
>>> onto.bind(impl_core, depends_on, setup_env)
Statement(label='Implement core module depends_on Setup dev environment', id=8)
>>> onto.bind(impl_core, depends_on, design_spec)
Statement(label='Implement core module depends_on Write design spec', id=9)
>>> onto.bind(write_tests, depends_on, impl_core)
Statement(label='Write tests depends_on Implement core module', id=10)
>>> onto.bind(review_pr, depends_on, write_tests)
Statement(label='Review pull request depends_on Write tests', id=11)
```

### Pretty-print the task graph

```python
>>> onto.show(predicate="depends_on")
Statements (predicate='depends_on'):
  [8] Statement(id=8, truth=None)
       subject:   Thing(label='Implement core module', id=3)
       predicate: Predicate(label='depends_on', id=6)
       object:    Thing(label='Setup dev environment', id=1)

  [9] Statement(id=9, truth=None)
       subject:   Thing(label='Implement core module', id=3)
       predicate: Predicate(label='depends_on', id=6)
       object:    Thing(label='Write design spec', id=2)

  [10] Statement(id=10, truth=None)
       subject:   Thing(label='Write tests', id=4)
       predicate: Predicate(label='depends_on', id=6)
       object:    Thing(label='Implement core module', id=3)

  [11] Statement(id=11, truth=None)
       subject:   Thing(label='Review pull request', id=5)
       predicate: Predicate(label='depends_on', id=6)
       object:    Thing(label='Write tests', id=4)
```

### Classifying which dependencies are “confirmed”

```python
>>> onto.classify({
...     (impl_core, depends_on, setup_env): True,
...     (impl_core, depends_on, design_spec): True,
...     (write_tests, depends_on, impl_core): True,
...     (review_pr, depends_on, write_tests): None,  # still undecided
... })
Classification updated:
  true: 3, false: 0, unknown: 1

>>> onto.check_completeness(scope="task dependencies")
Completeness(scope='task dependencies') -> 0.75 (3/4 classified)
```

### Slicing for “what blocks what”

```python
>>> onto.bind(setup_env,  blocks, impl_core)
Statement(label='Setup dev environment blocks Implement core module', id=12)
>>> onto.bind(impl_core,  blocks, write_tests)
Statement(label='Implement core module blocks Write tests', id=13)
>>> onto.bind(write_tests, blocks, review_pr)
Statement(label='Write tests blocks Review pull request', id=14)

>>> onto.slice(predicate="blocks")
[('Setup dev environment', 'blocks', 'Implement core module', None),
 ('Implement core module', 'blocks', 'Write tests', None),
 ('Write tests', 'blocks', 'Review pull request', None)]
```

### Queries over the task graph

```python
>>> onto.query("predicate='depends_on' AND subject='Implement core module'")
Query matched 2 statements -> [
  'Implement core module depends_on Setup dev environment',
  'Implement core module depends_on Write design spec'
]

>>> onto.query("predicate='blocks' AND object='Review pull request'")
Query matched 1 statement -> ['Write tests blocks Review pull request']

# Tasks that have at least one unknown dependency
>>> onto.query("predicate='depends_on' AND truth IS NULL")
Query matched 1 statement -> ['Review pull request depends_on Write tests']
```

### Logical assertion example

We might want to assert a *schema* like:

> “Every task that blocks another task must itself depend on something.”

```python
>>> onto.assert_forall(
...     subject=onto.any(label_like="*"),   # any task
...     predicate=blocks,
...     obj=onto.exists("blocked_task"),
...     requires=onto.exists_dependency(depends_on),
... )
∀ t, blocked_task . t blocks blocked_task ⇒ ∃ d . t depends_on d   ✅
```

*(This is just an aspirational API sketch: `exists_dependency` could be a helper for these kinds of assertions.)*

---

## Example 2 (CLI) – Task dependencies

```bash
$ python3 src/cli/cli.py new -f tasks.pkl
[ontologica] Created new ontology at 'tasks.pkl'

$ python3 src/cli/cli.py add -f tasks.pkl "Setup dev environment"
[id=1] Thing 'Setup dev environment'
$ python3 src/cli/cli.py add -f tasks.pkl "Write design spec"
[id=2] Thing 'Write design spec'
$ python3 src/cli/cli.py add -f tasks.pkl "Implement core module"
[id=3] Thing 'Implement core module'
$ python3 src/cli/cli.py add -f tasks.pkl "Write tests"
[id=4] Thing 'Write tests'
$ python3 src/cli/cli.py add -f tasks.pkl "Review pull request"
[id=5] Thing 'Review pull request'

$ python3 src/cli/cli.py add-predicate -f tasks.pkl "depends_on"
[id=6] Predicate 'depends_on'

$ python3 src/cli/cli.py bind -f tasks.pkl "Implement core module" "depends_on" "Setup dev environment"
$ python3 src/cli/cli.py bind -f tasks.pkl "Implement core module" "depends_on" "Write design spec"
$ python3 src/cli/cli.py bind -f tasks.pkl "Write tests" "depends_on" "Implement core module"
$ python3 src/cli/cli.py bind -f tasks.pkl "Review pull request" "depends_on" "Write tests"

$ python3 src/cli/cli.py show -f tasks.pkl --predicate "depends_on"
[8] Implement core module  --depends_on-->  Setup dev environment
[9] Implement core module  --depends_on-->  Write design spec
[10] Write tests           --depends_on-->  Implement core module
[11] Review pull request   --depends_on-->  Write tests
```

---

## Example 3 – Web crawler + NER (politicians & committees)

This is a “Specific Example”: integrating a web crawler + SpaCy NER to build and inspect a civic ontology.

### High-level sketch

```python
>>> from ontology import Ontology
>>> from civic_scraper import latest_articles   # imaginary library
>>> import spacy

>>> nlp = spacy.load("en_core_web_sm")
>>> onto = Ontology()

>>> sits_on = onto.add_predicate("sits_on")
Predicate(label='sits_on', id=1)
>>> is_mayor_of = onto.add_predicate("is_mayor_of")
Predicate(label='is_mayor_of', id=2)
>>> is_council = onto.add_predicate("is_council")
Predicate(label='is_council', id=3)

# ingest a few articles
>>> for article in latest_articles(limit=3):
...     doc = nlp(article.text)
...     city = onto.add(article.city_name)
...     for ent in doc.ents:
...         if ent.label_ == "PERSON" and "Mayor" in ent.text:
...             mayor = onto.add(ent.text)
...             onto.bind(mayor, is_mayor_of, city)
...         if "Council" in ent.text or "Board" in ent.text:
...             council = onto.add(ent.text)
...             onto.bind(council, is_council, city)
...             # If article says "Mayor X sits on Y", we might detect that too:
...             if "sits on" in article.text:
...                 onto.bind(mayor, sits_on, council)
3 articles ingested -> 9 entities, 3 predicates, 7 statements
```

### Inspect the civic ontology

```python
>>> onto.show(limit=None)
Entities:
  [1] 'Springfield'
  [2] 'Mayor Lee'
  [3] 'Ethics Board'
  [4] 'Mayor Ortiz'
  [5] 'Port Council'
  [6] 'Mayor Kwan'
  [7] 'Transit Committee'
  [8] 'Riverside'
  [9] 'Bayview'

Predicates:
  [1] sits_on
  [2] is_mayor_of
  [3] is_council

Statements:
  [10] Mayor Lee is_mayor_of Springfield      truth=None
  [11] Ethics Board is_council Springfield    truth=None
  [12] Mayor Lee sits_on Ethics Board         truth=None
  [13] Mayor Ortiz is_mayor_of Bayview        truth=None
  [14] Port Council is_council Bayview        truth=None
  [15] Mayor Ortiz sits_on Port Council       truth=None
  [16] Mayor Kwan is_mayor_of Riverside       truth=None
  [17] Transit Committee is_council Riverside truth=None
```

### Slicing and querying

```python
>>> onto.slice(predicate="sits_on")
[('Mayor Lee', 'sits_on', 'Ethics Board', None),
 ('Mayor Ortiz', 'sits_on', 'Port Council', None)]

>>> onto.slice(object="Ethics Board")
[('Mayor Lee', 'sits_on', 'Ethics Board', None)]

>>> onto.query("predicate='is_mayor_of' AND object='Bayview'")
Query matched 1 statement -> ['Mayor Ortiz is_mayor_of Bayview']

>>> onto.query("predicate='is_council' AND subject LIKE '%Council'")
Query matched 1 statement -> ['Port Council is_council Bayview']

# who sits on a board in the same city they are mayor of?
>>> onto.query("""
...  sits_on(subject=?m, object=?board)
...  AND is_mayor_of(subject=?m, object=?city)
...  AND is_council(subject=?board, object=?city)
... """)
Query matched 2 tuples:
  m='Mayor Lee', board='Ethics Board', city='Springfield'
  m='Mayor Ortiz', board='Port Council', city='Bayview'
```

### Completeness & classification in this civic context

```python
>>> onto.classify({
...   ("Ethics Board", "is_council", "Springfield"): True,
...   ("Port Council", "is_council", "Bayview"): True,
...   ("Transit Committee", "is_council", "Riverside"): False,  # article says it's dissolved
... })
Classification updated:
  true: 2, false: 1, unknown: 0

>>> onto.check_completeness(scope="council catalog")
Completeness(scope='council catalog') -> 1.00 (3/3 known councils classified)
```

Snapshot:

```python
>>> onto.save_json("civic_ontology.json")
Exported 17 nodes to civic_ontology.json
```

---

## Example 3 (CLI) – Civic ontology from preprocessed data

Imagine you have preprocessed CSV data with columns: `mayor, committee, city`.

```bash
$ python3 src/cli/cli.py new -f civic.pkl
[ontologica] Created new ontology at 'civic.pkl'

$ python3 src/cli/cli.py add-predicate -f civic.pkl "sits_on"
[id=1] Predicate 'sits_on'
$ python3 src/cli/cli.py add-predicate -f civic.pkl "is_mayor_of"
[id=2] Predicate 'is_mayor_of'
$ python3 src/cli/cli.py add-predicate -f civic.pkl "is_council"
[id=3] Predicate 'is_council'

# (Pretend this is done in a loop over rows)
$ python3 src/cli/cli.py bind -f civic.pkl "Mayor Lee" "is_mayor_of" "Springfield"
$ python3 src/cli/cli.py bind -f civic.pkl "Ethics Board" "is_council" "Springfield"
$ python3 src/cli/cli.py bind -f civic.pkl "Mayor Lee" "sits_on" "Ethics Board"
$ python3 src/cli/cli.py bind -f civic.pkl "Mayor Ortiz" "is_mayor_of" "Bayview"
$ python3 src/cli/cli.py bind -f civic.pkl "Port Council" "is_council" "Bayview"
$ python3 src/cli/cli.py bind -f civic.pkl "Mayor Ortiz" "sits_on" "Port Council"

$ python3 src/cli/cli.py show -f civic.pkl --predicate "sits_on"
[10] Mayor Lee   --sits_on-->   Ethics Board
[11] Mayor Ortiz --sits_on-->   Port Council

$ python3 src/cli/cli.py slice -f civic.pkl --object "Ethics Board"
[10] Mayor Lee --sits_on--> Ethics Board

$ python3 src/cli/cli.py query -f civic.pkl "is_mayor_of(object='Bayview')"
Matched:
  [13] Mayor Ortiz is_mayor_of Bayview
```

---

## Example 4 – Simple classification game (truth labeling)

This one doubles as a testbed for `classify`, `slice`, and `check_completeness`.

```python
>>> from ontology import Ontology
>>> onto = Ontology()

>>> earth  = onto.add("Earth")
Thing(label='Earth', id=1)
>>> mars   = onto.add("Mars")
Thing(label='Mars', id=2)
>>> pluto  = onto.add("Pluto")
Thing(label='Pluto', id=3)

>>> is_planet = onto.add_predicate("is_planet")
Predicate(label='is_planet', id=4)

# Enumerate all candidates
>>> onto.enumerate(subjects=[earth, mars, pluto], predicates=[is_planet], objects=[earth, mars, pluto])
Enumerated 9 candidate statements (3 entities × 1 predicate × 3 entities)

# We really only care about (X, is_planet, X), but enumeration is generic
>>> onto.show(limit=5)
Statements:
  [5] Earth is_planet Earth   truth=None
  [6] Earth is_planet Mars    truth=None
  [7] Earth is_planet Pluto   truth=None
  [8] Mars is_planet Earth    truth=None
  [9] Mars is_planet Mars     truth=None
  ...

# Use classify to mark the self-relations as true/false,
# leaving mixed ones (like 'Earth is_planet Mars') as unknown.
>>> onto.classify({
...     (earth, is_planet, earth): True,
...     (mars,  is_planet, mars): True,
...     (pluto, is_planet, pluto): False,
... })
Classification updated:
  true: 2, false: 1, unknown: 6

>>> onto.slice(subject="Earth", object="Earth", predicate="is_planet", include_truth=True)
[('Earth', 'is_planet', 'Earth', True)]

>>> onto.check_completeness(scope="planet-status")
Completeness(scope='planet-status') -> 1.00 (3/3 key statements classified)
```

---

## Example 5 – Logical assertion / “model check” style

Here we treat the ontology like something to be checked against a specification.

```python
>>> from ontology import Ontology
>>> onto = Ontology()

>>> parent_of = onto.add_predicate("parent_of")
Predicate(label='parent_of', id=1)
>>> ancestor_of = onto.add_predicate("ancestor_of")
Predicate(label='ancestor_of', id=2)

>>> alice = onto.add("Alice")
>>> bob   = onto.add("Bob")
>>> carol = onto.add("Carol")

>>> onto.bind(alice, parent_of, bob)
Statement(label='Alice parent_of Bob', id=4)
>>> onto.bind(bob, parent_of, carol)
Statement(label='Bob parent_of Carol', id=5)

# Suppose some external process derived ancestor_of facts:
>>> onto.bind(alice, ancestor_of, bob)
Statement(label='Alice ancestor_of Bob', id=6)
>>> onto.bind(alice, ancestor_of, carol)
Statement(label='Alice ancestor_of Carol', id=7)
>>> onto.bind(bob, ancestor_of, carol)
Statement(label='Bob ancestor_of Carol', id=8)
```

We might want to assert a rule like:

> For all x, y: if x is a parent of y, then x is an ancestor of y.

```python
>>> onto.assert_forall(
...     subject=onto.any_of(alice, bob, carol),
...     predicate=parent_of,
...     obj=onto.any_of(alice, bob, carol),
...     implies=(ancestor_of,),
... )
∀ x,y ∈ {Alice,Bob,Carol} . x parent_of y ⇒ x ancestor_of y  ✅
```

Then a more complex property:

> Ancestor is transitive: if x ancestor_of y and y ancestor_of z, then x ancestor_of z.

```python
>>> onto.assert_forall(
...     subject=onto.any_of(alice, bob, carol),
...     predicate=ancestor_of,
...     obj=onto.any_of(alice, bob, carol),
...     transitive=True,
... )
∀ x,y,z . x ancestor_of y ∧ y ancestor_of z ⇒ x ancestor_of z  ✅
```

If there was a missing fact, you’d see something like:

```python
>>> # Suppose we forgot 'Alice ancestor_of Carol'
>>> onto.assert_forall(
...     subject=onto.any_of(alice, bob, carol),
...     predicate=ancestor_of,
...     obj=onto.any_of(alice, bob, carol),
...     transitive=True,
... )
∀ x,y,z . x ancestor_of y ∧ y ancestor_of z ⇒ x ancestor_of z  ❌
Counterexamples (1):
  x='Alice', y='Bob', z='Carol'
```
