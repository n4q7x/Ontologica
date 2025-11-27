class Parser:
    """
    Simple parser for Ontologica triple format: (subject, predicate, object)
    Ignores lines that do not start with '('.
    """
    def __init__(self, strip_comments=True):
        self.strip_comments = strip_comments

    def parse(self, text):
        triples = []
        for line in text.splitlines():
            line = line.strip()
            if self.strip_comments and (not line or line.startswith('#')):
                continue
            if line.startswith('(') and line.endswith(')'):
                # Remove parentheses and split by comma
                inner = line[1:-1]
                parts = [p.strip() for p in inner.split(',')]
                if len(parts) == 3:
                    triples.append(tuple(parts))
        return triples

    def parse_file(self, path):
        with open(path, 'r') as f:
            return self.parse(f.read())

    def write_triples(self, triples, path, header=None):
        with open(path, 'w') as f:
            if header:
                f.write(header + '\n')
            for t in triples:
                f.write(f"({t[0]}, {t[1]}, {t[2]})\n")
