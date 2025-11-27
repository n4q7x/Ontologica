from __future__ import annotations

from pathlib import Path

from ontologica import Ontology, Statement


def test_policy_analyst_story(tmp_path: Path) -> None:
    # Jeffrey is a municipal policy analyst. He often juggles overlapping mandates,
    # but he needs to prove which department reports to which oversight board.
    # He decides to open Ontologica to sketch the accountability chain, first by
    # starting with an empty registry he can trust.
    registry = Ontology()
    assert len(registry.things) == 0

    # He adds the departments and boards that appear in this week's briefing.
    housing = registry.add("Housing Department")
    transit = registry.add("Transit Authority")
    oversight = registry.add("Oversight Council")
    ethics = registry.add("Ethics Committee")
    assert all(entity in registry.things for entity in (housing, transit, oversight, ethics))

    # Jeffrey frequently reasons in terms of obligations, so he records a predicate
    # describing which body reports to another.
    reports_to = registry.add_predicate("reports_to")
    assert reports_to in registry.things

    # The analyst binds the specific relationships his memo must defend and he
    # checks every statement as he makes it to avoid narrative drift.
    housing_stmt = registry.bind(housing, reports_to, oversight)
    transit_stmt = registry.bind(transit, reports_to, oversight)
    ethics_stmt = registry.bind(ethics, reports_to, oversight)
    assert all(isinstance(stmt, Statement) for stmt in (housing_stmt, transit_stmt, ethics_stmt))
    assert housing_stmt.label == "Housing Department reports_to Oversight Council"

    # Jeffrey exports a JSON snapshot that he can pass to colleagues and he
    # immediately reloads it to ensure the narrative survived serialization.
    json_path = tmp_path / "policy_story.json"
    registry.save_json(json_path.as_posix())
    restored = Ontology.load_json(json_path.as_posix())
    assert len(restored.things) == len(registry.things)
    assert restored.find_one("Transit Authority") is not None
    restored_statements = [t for t in restored.things if isinstance(t, Statement)]
    assert any(stmt.label == ethics_stmt.label for stmt in restored_statements)

    # With the story verified, Jeffrey is confident he can quote exact chains of
    # responsibility during the committee hearing.
    assert len(restored_statements) == 3
