# normalize.py

from typing import Tuple, List, Dict
from .models import Atom, Predicate, Triple   # <-- import your real classes


# -------------------------------------------------------------------
# (1) VALIDATE JSON SCHEMA
# -------------------------------------------------------------------

def validate_json_schema(raw: dict) -> None:
    """
    Validate that the raw JSON dict conforms to the Ontologica JSON structure.
    Raises ValueError if anything is invalid.
    """

    # Top-level must be a dict
    if not isinstance(raw, dict):
        raise ValueError("Ontology JSON must be a dictionary.")

    # Required top-level keys
    if "nodes" not in raw:
        raise ValueError("Ontology JSON missing required field: 'nodes'.")
    if "triples" not in raw:
        raise ValueError("Ontology JSON missing required field: 'triples'.")

    nodes = raw["nodes"]
    triples = raw["triples"]

    # ---- Validate nodes ----
    if not isinstance(nodes, list):
        raise ValueError("'nodes' must be a list.")

    for node in nodes:
        if not isinstance(node, dict):
            raise ValueError("Each node must be a dict.")

        for key in ("id", "kind", "label"):
            if key not in node:
                raise ValueError(f"Node missing required field: '{key}'.")

        # id
        if not isinstance(node["id"], int) or node["id"] < 0:
            raise ValueError(f"Node id must be a non-negative integer, got {node['id']}.")

        # kind
        kind = node["kind"]
        if kind not in ("Atom", "Predicate"):
            raise ValueError(f"Node kind must be 'Atom' or 'Predicate', got '{kind}'.")

        # label
        if not isinstance(node["label"], str):
            raise ValueError("Node 'label' must be a string.")

    # ---- Validate triples ----
    if not isinstance(triples, list):
        raise ValueError("'triples' must be a list.")

    for t in triples:
        if not isinstance(t, dict):
            raise ValueError("Each triple must be a dict.")

        for key in ("id", "kind", "subject", "predicate", "object", "label"):
            if key not in t:
                raise ValueError(f"Triple missing required field: '{key}'.")

        if not isinstance(t["id"], int) or t["id"] < 0:
            raise ValueError(f"Triple id must be a non-negative integer, got {t['id']}.")

        if t["kind"] != "Triple":
            raise ValueError(f"Triple 'kind' must be 'Triple', got '{t['kind']}'.")

        # subject / predicate / object
        for field in ("subject", "predicate", "object"):
            if not isinstance(t[field], int) or t[field] < 0:
                raise ValueError(
                    f"Triple '{field}' must be a non-negative integer id, got {t[field]}"
                )

        if not isinstance(t["label"], str):
            raise ValueError("Triple 'label' must be a string.")


# -------------------------------------------------------------------
# (2) NORMALIZE RAW JSON → INTERNAL OBJECTS
# -------------------------------------------------------------------

def normalize_json(raw: dict) -> Tuple[List[Atom], List[Predicate], List[Triple]]:
    """
    Fully validate + convert JSON ontology data into internal Python objects.
    
    Returns:
        (atoms, predicates, triples)
    """

    # 1. Validate structure
    validate_json_schema(raw)

    # 2. Extract raw lists
    raw_nodes = raw["nodes"]
    raw_triples = raw["triples"]

    atoms: List[Atom] = []
    predicates: List[Predicate] = []
    triples: List[Triple] = []

    # ---- Build node objects ----
    for node in raw_nodes:
        kind = node["kind"]
        node_id = node["id"]
        label = node["label"]

        if kind == "Atom":
            atoms.append(Atom(id=node_id, label=label))
        else:  # Predicate
            predicates.append(Predicate(id=node_id, label=label))

    # ---- Build triple objects ----
    for t in raw_triples:
        triples.append(
            Triple(
                id=t["id"],
                subject=t["subject"],
                predicate=t["predicate"],
                object=t["object"],
                label=t["label"]
            )
        )

    return atoms, predicates, triples