from pathlib import Path

from .normalize import normalize_json_data



# ---------------------------------------------------------
# 1. SUPPORTED EXTENSIONS AND PARSER DISPATCH TABLE
# ---------------------------------------------------------

# Replace these with real parser functions later



import json


def load_json(path: Path):
    """
    Load ontology data from a JSON file.
    Returns whatever Python structure is inside the JSON (dict, list, etc).
    
    Raises:
        ValueError: if JSON is syntactically invalid
        OSError: if file cannot be opened
    """
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in '{path}': {e.msg} at line {e.lineno}") from e
    
    except OSError as e:
        # covers permission denied, unreadable file, etc.
        raise OSError(f"Could not open '{path}': {e.strerror}") from e



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
    path = Path(source)

    # 1. Must have an extension
    if path.suffix == "":
        raise ValueError(f"File '{path}' has no extension.")

    # 2. Must be a supported extension
    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file extension: {path.suffix}")

    # 3. Must exist
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

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
    if source is None:
        return {"nodes": [], "triples": []}

    path = validate_path(source)
    ext = detect_format(path)
    raw = load_raw(path, ext)

    # call the proper normalizer
    if ext == ".json":
        return normalize_json_data(raw)

    # other formats later...