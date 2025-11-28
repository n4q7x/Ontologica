from .loaders import load_any


class Ontology:
    """High-level public Ontology object."""

    def __init__(self, source=None):
        """
        source may be:
            - None          → empty ontology
            - str / Path    → file path
            - dict          → direct record data
        """
        self.records = load_any(source)

    def load(self, source):
        """Reload this ontology with new data."""
        self.records = load_any(source)