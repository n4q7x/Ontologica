# test_ontology.py

import os
import tempfile

from core.core import Ontology, Thing, Predicate, Statement


def test_add_and_add_predicate():
    onto = Ontology()

    a = onto.add("Alice")
    b = onto.add("Bob")
    likes = onto.add_predicate("likes")

    # Types are correct
    assert isinstance(a, Thing)
    assert isinstance(b, Thing)
    assert isinstance(likes, Predicate)

    # All are in the ontology
    assert a in onto.things
    assert b in onto.things
    assert likes in onto.things

    # IDs are unique
    ids = {a.id, b.id, likes.id}
    assert len(ids) == 3


def test_bind_creates_statement_with_fused_label():
    onto = Ontology()

    alice = onto.add("Alice")
    bob = onto.add("Bob")
    likes = onto.add_predicate("likes")

    stmt = onto.bind(alice, likes, bob)

    assert isinstance(stmt, Statement)
    assert stmt in onto.things
    assert stmt.label == "Alice likes Bob"
    assert stmt.subject is alice
    assert stmt.predicate is likes
    assert stmt.obj is bob


def test_slice_only_returns_statements():
    """Internal _slice helper should only ever return Statement instances."""
    onto = Ontology()

    alice = onto.add("Alice")
    bob = onto.add("Bob")
    likes = onto.add_predicate("likes")
    onto.bind(alice, likes, bob)

    result = onto._slice("Alice", "subject")

    assert result  # not empty
    assert all(isinstance(x, Statement) for x in result)
    # every statement returned has subject Alice
    assert all(s.subject is alice for s in result)


def test_enumerate_produces_full_cartesian():
    onto = Ontology()

    alice = onto.add("Alice")
    bob = onto.add("Bob")
    likes = onto.add_predicate("likes")

    # Right now: 2 Things + 1 Predicate
    onto.enumerate()

    # Subjects: Alice, Bob
    # Predicates: likes
    # Objects: Alice, Bob
    # => 2 * 1 * 2 = 4 statements
    statements = {t for t in onto.things if isinstance(t, Statement)}
    assert len(statements) == 4

    labels = {s.label for s in statements}
    assert "Alice likes Alice" in labels
    assert "Alice likes Bob" in labels
    assert "Bob likes Alice" in labels
    assert "Bob likes Bob" in labels


def test_pickle_roundtrip():
    onto = Ontology()
    alice = onto.add("Alice")
    likes = onto.add_predicate("likes")
    bob = onto.add("Bob")
    onto.bind(alice, likes, bob)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "onto.pkl")

        onto.save(path)
        loaded = Ontology.load(path)

        # Same number of things
        assert len(loaded.things) == len(onto.things)

        # There is at least one statement with the same label
        orig_stmt_labels = {t.label for t in onto.things if isinstance(t, Statement)}
        loaded_stmt_labels = {t.label for t in loaded.things if isinstance(t, Statement)}
        assert orig_stmt_labels == loaded_stmt_labels


def test_json_roundtrip():
    onto = Ontology()
    alice = onto.add("Alice")
    likes = onto.add_predicate("likes")
    bob = onto.add("Bob")
    onto.bind(alice, likes, bob)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "onto.json")

        onto.save_json(path)
        loaded = Ontology.load_json(path)

        # Same number of things
        assert len(loaded.things) == len(onto.things)

        # Same multiset of (kind, label)
        def sig_set(o: Ontology):
            out = []
            for t in o.things:
                if isinstance(t, Statement):
                    kind = "Statement"
                elif isinstance(t, Predicate):
                    kind = "Predicate"
                else:
                    kind = "Thing"
                out.append((kind, t.label))
            return sorted(out)

        assert sig_set(onto) == sig_set(loaded)


def test_find_one():
    onto = Ontology()
    alice = onto.add("Alice")
    bob = onto.add("Bob")

    # by label
    x = onto.find_one("Alice")
    assert x is alice

    # by id
    y = onto.find_one(alice.id)
    assert y is alice

    # missing
    assert onto.find_one("NotThere") is None
