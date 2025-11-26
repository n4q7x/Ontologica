
<p align="center">
<img width="300" height="1000" alt="197a19bf84928d6ef410df1f1981b76c382521eba555d9a885884a03a2a1b70c" src="https://github.com/user-attachments/assets/82e893c7-e5d7-46d6-b256-9b64b6daffaa" />
</p>
This repo is the current iteration of my years-long quest to build formal ontology tools.

The current iteration is the consummation of years of self-directed research into the necessary topics surrounding formal ontology ("FO"), including logic, linguistics, philosophy, metaphysics, cognitive science, type theory, computer science, category theory, functional programming, web development, databases, the semantic web, and much more.

The design will continue to change, but this is the closest I have come in making something usable. My hope is that the development can take a turn to a new stage where features are added and areas for improvement identified whilst the tool has an active, if modest, user base.

Ontologica takes design influence from many, many pre-existing ideas, theories, projects, and tools: basic formal ontology, information economy metalanguage, Haskell, Prolog, categorical query language, SQL, Neo4j, and numerous thinkers such as Frege, Bertrand Russell, Per Martin-Löf, Alan Turing, David Spivak, and so on (this list to be added to). In a way, I cannot claim to have invented anything original, but am only trying to put together the many features and design choices of such things into one system that feels perfect to me, has everything I would like, and not more. This project is intended to be only the beginning of a longer research inquest into seeing how formal ontology can be more common amongst non-technical users and could lead to a different kind of internet called the "datanet". Again, I wish to stress that none of these ideas are new, but I am simply repackaging classic, established ideas like relational data models, graph databases, RDF, the semantic web, etc, but trying to breathe new life into them, synthesize them and put my own finishing touches on them. I would like to emphasize that one of the most important features an ontology system should have, in my opinion, is **reification** (discussed further, below).

I am 30 years old and have more or less decided at this point that increasing the use of formal ontologies in society has basically become my mission on Earth. Please, please consider contributing to this work by donating or becoming a sponsor. Thank you.


**Ontologica** is a Python library + CLI for building, exploring, and persisting ontologies composed of **Things**, **Predicates**, and **Statements**.

It is designed to be:

- **Extremely readable** — the entire core fits into a few hundred lines of clear Python  
- **Lightweight** — no dependencies beyond the standard library  
- **Programmable** — import the module to build ontologies inside Python  
- **Usable** — includes a CLI for building and inspecting ontologies interactively  
- **Portable** — export/import ontologies as JSON  
- **Persistent** — save/load via pickle for fast REPL workflows  
- **Extensible** — structured cleanly so new features can be added without pain  

Ontologica is being actively developed by **Julius Hamilton**, who is seeking collaborators, users, and funding to take this further. The project is fully open source and intended to remain that way.

---

## What does it do?

Ontologica models a tiny but expressive universe of entities:

- **Thing** — atomic element (e.g. "Alice")
- **Predicate** — binary relation (e.g. "likes")
- **Statement** — a triple `(subject, predicate, object)`  
  - each one is itself a Thing  
  - automatically gets a fused label like "Alice likes Bob"

The core container is:

- **Ontology** — a set of all Things, including Predicates & Statements

Ontologica supports:

- Adding Things & Predicates  
- Binding new Statements  
- Enumerating all possible statements over existing Things × Predicates × Things  
- Pretty-printing (recursively formatted block output)  
- Slicing by subject/predicate/object using label, id, or Thing  
- Flexible searching  
- Pickle save/load  
- JSON export/import  
- A working CLI for everyday use

---

## Example

```python
from ontology import Ontology

onto = Ontology()

alice = onto.add("Alice")
bob   = onto.add("Bob")
likes = onto.add_predicate("likes")

onto.bind(alice, likes, bob)

onto.show()
```

Sample output:

```
Thing(label='Alice', id=0)

Thing(label='Bob', id=1)

Predicate(label='likes', id=2)

Statement(label='Alice likes Bob', id=3)
  subject:
      Thing(label='Alice', id=0)
  predicate:
      Predicate(label='likes', id=2)
  object:
      Thing(label='Bob', id=1)
```

---

## CLI

Ontologica ships with a command line tool:

```bash
python ontology_cli.py new -f myonto.pkl
python ontology_cli.py add -f myonto.pkl "Alice"
python ontology_cli.py add-predicate -f myonto.pkl "likes"
python ontology_cli.py bind -f myonto.pkl "Alice" "likes" "Bob"
python ontology_cli.py show -f myonto.pkl
python ontology_cli.py export-json -f myonto.pkl myonto.json
```

---

## Installation

For now, clone the repository:

```bash
git clone https://github.com/<yourname>/ontologica.git
cd ontologica
```

Eventually this will be published on PyPI as:

```bash
pip install ontologica
```

(coming soon)

---

## Project Structure

```
ontology.py        # main module
ontology_cli.py    # CLI tool
test_ontology.py   # basic tests
README.md          # this file
```

---

## Goals & Philosophy

Ontologica aims to become:

- A **standard minimal ontology representation** for Python
- An example of **clean, explicit, well-structured code**  
- A tool that is easy to build on:  
  - inference  
  - type-checking  
  - rule engines  
  - visualizers  
  - semantic search  
  - logical programming layers

As the project grows, the goal is to maintain:

- Clarity  
- Stability  
- Zero-dependency portability  
- Intuitive CLI + Python APIs  

---

## Contributing

Contributions are welcome. If you’d like to help with:

- Architecture & design  
- Rule systems  
- Graph visualizations  
- Performance  
- Better persistence formats  
- Documentation  
- Testing  

…feel free to open issues or PRs.

---

## Funding & Support

**I (Julius Hamilton) am actively looking for funding, sponsorship, or employment opportunities related to ontology work, logic engines, knowledge-representation tools, or Python systems programming.**

If this project interests you, or you’d like to support its future development:

- Reach out via GitHub issues  
- Connect on LinkedIn  
- Propose collaboration or contract work  
- Offer sponsorship or grants  

Ontologica will remain open source. Funding helps accelerate its development.

---

## License

GPL-3.0
