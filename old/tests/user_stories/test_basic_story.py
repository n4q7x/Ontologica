from __future__ import annotations

from pathlib import Path

from ontologica import Ontology, Statement


def test_basic_story_walkthrough(tmp_path: Path) -> None:
    print("👤 User starts Ontologica story")
    onto = Ontology()
    assert len(onto.things) == 0

    print("➕ Adds Alice and Bob atoms")
    alice = onto.add("Alice")
    bob = onto.add("Bob")
    assert {alice, bob}.issubset(onto.things)

    print("⚙️  Introduces predicate 'likes'")
    likes = onto.add_predicate("likes")

    print("🔗 Creates first statement Alice likes Bob")
    stmt = onto.bind(alice, likes, bob)
    assert stmt.label == "Alice likes Bob"

    print("💾 Saves ontology, then loads fresh copy")
    path = tmp_path / "story_basic.pkl"
    onto.save(path.as_posix())
    restored = Ontology.load(path.as_posix())

    print("🔍 Confirms entities after reload")
    assert restored.find_one("Alice") is not None
    assert restored.find_one("likes") is not None
    restored_stmt = next(t for t in restored.things if isinstance(t, Statement))
    assert restored_stmt.subject.label == "Alice"
    assert restored_stmt.obj.label == "Bob"

    print("📈 Story complete with", len(restored.things), "things recorded")
