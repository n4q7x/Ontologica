# models.py

from dataclasses import dataclass


# -------------------------------------------------------------
# NODE TYPES: Atom and Predicate
# -------------------------------------------------------------

@dataclass
class Atom:
    """
    A basic ontology node representing an atomic symbol.
    
    Fields:
        id: natural number identifier
        label: human-readable label (string)
        kind: always "Atom"
    """
    id: int
    label: str
    kind: str = "Atom"


@dataclass
class Predicate:
    """
    A node that represents a relationship type (binary predicate).
    
    Fields:
        id: natural number identifier
        label: predicate label (string)
        kind: always "Predicate"
    """
    id: int
    label: str
    kind: str = "Predicate"


# -------------------------------------------------------------
# TRIPLE TYPE
# -------------------------------------------------------------

@dataclass
class Triple:
    """
    A reifiable triple: (subject, predicate, object)

    Fields:
        id: triple identifier (natural number)
        subject: id of subject node/triple
        predicate: id of predicate node
        object: id of object node/triple
        label: human-readable description of the triple
        kind: always "Triple"
    """
    id: int
    subject: int
    predicate: int
    object: int
    label: str
    kind: str = "Triple"