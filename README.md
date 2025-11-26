
<p align="center">
<img width="300" height="1000" alt="197a19bf84928d6ef410df1f1981b76c382521eba555d9a885884a03a2a1b70c" src="https://github.com/user-attachments/assets/82e893c7-e5d7-46d6-b256-9b64b6daffaa" />
</p>

# Getting started

```sh
git clone https://github.com/n4q7x/Ontologica/
cd Ontologica
python3 cli.py
```

## Example use

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
