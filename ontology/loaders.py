from pathlib import Path


# ---------------------------------------------------------
# 1. SUPPORTED EXTENSIONS AND PARSER DISPATCH TABLE
# ---------------------------------------------------------

# Replace these with real parser functions later
def load_json(path: Path):
    raise NotImplementedError

def load_csv(path: Path):
    raise NotImplementedError

def load_turtle(path: Path):
    raise NotImplementedError

def load_rdfxml(path: Path):
    raise NotImplementedError


SUPPORTED_EXTENSIONS = {
    ".json",
    ".csv",
    ".ttl",
    ".rdf",
}

PARSERS = {
    ".json": load_json,
    ".csv": load_csv,
    ".ttl": load_turtle,     # Turtle RDF
    ".rdf": load_rdfxml,     # RDF/XML
}


# ---------------------------------------------------------
# 2. VALIDATE PATH
# ---------------------------------------------------------

def validate_path(source) -> Path:
    """Return a valid Path object or raise appropriate errors."""
    path = Path(source)

    if not path.exists():
        raise FileNotFoundError(f"No such file: {path}")

    if path.suffix == "":
        raise ValueError(f"File has no extension: {path}")

    return path


# ---------------------------------------------------------
# 3. DETECT FORMAT
# ---------------------------------------------------------

def detect_format(path: Path) -> str:
    ext = path.suffix.lower()

    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file extension: {ext}")

    return ext


# ---------------------------------------------------------
# 4. LOAD RAW DATA
# ---------------------------------------------------------

def load_raw(path: Path, filetype: str):
    """Use the correct parser for the given file type."""
    parser = PARSERS[filetype]
    return parser(path)


# ---------------------------------------------------------
# 5. HIGH-LEVEL LOADER (the one Ontology.__init__ will call)
# ---------------------------------------------------------

def load_any(source):
    """Given a source (None, dict, or path), return parsed records."""
    if source is None:
        return set()    # your empty ontology

    if isinstance(source, dict):
        return source   # already "records"

    path = validate_path(source)
    filetype = detect_format(path)
    return load_raw(path, filetype)