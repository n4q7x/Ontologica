from __future__ import annotations

from pathlib import Path

from ontologica import Ontology, Statement


def test_researcher_discovers_patterns(tmp_path: Path) -> None:
    print("🧪 Researcher loads seed ontology")
    onto = Ontology()
    alice = onto.add("Alice")
    bob = onto.add("Bob")
    carol = onto.add("Carol")
    likes = onto.add_predicate("likes")
    cites = onto.add_predicate("cites")

    print("📊 Researcher enumerates possible hypotheses")
    onto.enumerate()
    total_statements = len([t for t in onto.things if isinstance(t, Statement)])
    print("    total statements:", total_statements)
    assert total_statements == len(onto.things) - 5  # subtract atoms/predicates

    print("🔍 Researcher filters for 'likes' predicate")
    matches = [s for s in onto.things if isinstance(s, Statement) and s.predicate.label == "likes"]
    assert matches

    print("🧷 Researcher pins one fact and exports JSON")
    pinned = matches[0]
    onto.show(predicate="likes")
    onto_path = tmp_path / "researcher.json"
    onto.save_json(onto_path.as_posix())

    print("♻️  Researcher reloads dataset for peer review")
    restored = Ontology.load_json(onto_path.as_posix())
    restored_matches = [
        s for s in restored.things if isinstance(s, Statement) and s.predicate.label == "likes"
    ]
    assert len(restored_matches) == len(matches)
    assert any(s.label == pinned.label for s in restored_matches)

    print("📚 Researcher story finished with", len(restored.things), "items")
