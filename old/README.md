
<p align="center">
<img width="300" height="1000" alt="197a19bf84928d6ef410df1f1981b76c382521eba555d9a885884a03a2a1b70c" src="https://github.com/user-attachments/assets/82e893c7-e5d7-46d6-b256-9b64b6daffaa" />
</p>

# Getting started


```sh
git clone https://github.com/n4q7x/Ontologica/
cd Ontologica
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest
python3 src/cli/cli.py

```

## Abstract example

```python

from ontology import Ontology

onto = Ontology()

e1 = onto.add("entity1")
e2   = onto.add("entity2")
p1 = onto.add_predicate("pred1")

onto.enumerate()

onto.show()

onto.classify((e1, p1, e2) = True, ...)

onto.check_completeness()

onto.push() / write()

onto.slice(predicate: "p1")

onto.query("...")

onto.assert(forall, (subject, is_pred, some_object), (subject, is_pred, object))

```

## Specific Example

```python

Using Ontologica in conjunction with a web crawler, maybe Spacy NER, to load and model-check an ontology about something (i.e., politicians):




```



## CLI

The CLI is a work in progress. It will be a REPL, where you launch it and can write interactive commands.

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

[![Buy Me a Coffee](https://img.buymeacoffee.com/button-api/?text=Support%20Ontologica&emoji=☕&slug=your-handle&button_colour=FFDD00&font_colour=000000&font_family=Inter&outline_colour=000000&coffee_colour=ffffff)](https://www.buymeacoffee.com/your-handle)
[![PayPal](https://img.shields.io/badge/PayPal-Donate-blue.svg)](https://www.paypal.com/donate?hosted_button_id=PLACEHOLDER)

Ontologica will remain open source. Funding helps accelerate its development.

---

## License

GPL-3.0
