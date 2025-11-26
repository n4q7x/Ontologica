from __future__ import annotations

from ontologica import Ontology, Predicate, Statement


def test_add_and_add_predicate_register_items(empty_ontology: Ontology) -> None:
    alice = empty_ontology.add("Alice")
    likes = empty_ontology.add_predicate("likes")

    assert alice in empty_ontology.things
    assert likes in empty_ontology.things
    assert isinstance(likes, Predicate)


def test_bind_creates_statement_with_fused_label(simple_ontology: tuple[Ontology, object, object, Predicate]) -> None:
    onto, alice, bob, likes = simple_ontology

    stmt = onto.bind(alice, likes, bob)

    assert isinstance(stmt, Statement)
    assert stmt.label == "Alice likes Bob"
    assert stmt.subject is alice
    assert stmt.obj is bob


def test_enumerate_creates_cartesian_statements(simple_ontology: tuple[Ontology, object, object, Predicate]) -> None:
    onto, alice, bob, likes = simple_ontology
    subjects = list(onto.things)
    predicates = [t for t in subjects if isinstance(t, Predicate)]

    onto.enumerate()

    statements = [t for t in onto.things if isinstance(t, Statement)]
    expected = len(subjects) * len(predicates) * len(subjects)
    assert len(statements) == expected
    assert any(s.subject is alice and s.obj is bob for s in statements)
    assert all(s.predicate is likes for s in statements if s.predicate.label == "likes")


def test_find_one_resolves_by_label_and_id(simple_ontology: tuple[Ontology, object, object, Predicate]) -> None:
    onto, alice, *_ = simple_ontology

    assert onto.find_one("Alice") is alice
    assert onto.find_one(alice.id) is alice
    assert onto.find_one(alice) is alice
    assert onto.find_one("Missing") is None
