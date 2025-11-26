from __future__ import annotations

from ontologica import Ontology, Thing, Predicate, Statement


def test_public_symbols_are_importable() -> None:
    assert Ontology is not None
    assert Thing is not None
    assert Predicate is not None
    assert Statement is not None
