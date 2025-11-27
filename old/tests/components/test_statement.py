from __future__ import annotations

from ontologica import Statement, Thing, Predicate


def test_statement_fuses_subject_predicate_object() -> None:
    alice = Thing("Alice")
    likes = Predicate("likes")
    bob = Thing("Bob")

    stmt = Statement("Alice likes Bob", alice, likes, bob)

    assert stmt.subject is alice
    assert stmt.predicate is likes
    assert stmt.obj is bob
    assert stmt.label == "Alice likes Bob"
