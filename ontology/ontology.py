# ontology.py

from .loaders import load_any
from .normalize import normalize_json

class Ontology:
    def __init__(self, source=None):

        if source is None:
            self.atoms = {}
            self.predicates = {}
            self.triples = {}
            return

        # load_any now returns (format, raw_data)
        fmt, raw = load_any(source)

        # ---- Format dispatch ----
        if fmt == ".json":
            atoms, predicates, triples = normalize_json(raw)

        else:
            raise ValueError(f"No normalizer available for format {fmt}")

        # build lookup tables
        self.atoms = {a.id: a for a in atoms}
        self.predicates = {p.id: p for p in predicates}
        self.triples = {t.id: t for t in triples}