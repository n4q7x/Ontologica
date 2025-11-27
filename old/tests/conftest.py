from __future__ import annotations

import pytest

from ontologica import Ontology, Thing, Predicate


@pytest.fixture
def empty_ontology() -> Ontology:
    """Return a fresh ontology for tests that need a blank slate."""
    return Ontology()


@pytest.fixture
def simple_ontology() -> tuple[Ontology, Thing, Thing, Predicate]:
    """Provide an ontology seeded with Alice, Bob, and the 'likes' predicate."""
    onto = Ontology()
    alice = onto.add("Alice")
    bob = onto.add("Bob")
    likes = onto.add_predicate("likes")
    return onto, alice, bob, likes
