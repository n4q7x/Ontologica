from .loaders import load_any

class Ontology:
    def __init__(self, source=None):
        self.nodes, self.triples = load_any(source)