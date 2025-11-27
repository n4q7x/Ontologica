from __future__ import annotations

from pathlib import Path

from ontologica import Ontology, Statement


def test_museum_curator_story(tmp_path: Path) -> None:
    # Mina is a museum curator. She often rotates artifacts between galleries,
    # but she needs to prove which objects belong together for an upcoming tour.
    # She opens Ontologica to narrate those pairings, beginning with a clean slate.
    catalog = Ontology()
    assert len(catalog.things) == 0

    # Mina captures the two artifacts and the temporary gallery she wants to
    # describe before docents arrive.
    astrolabe = catalog.add("Astrolabe")
    tapestry = catalog.add("Silk Tapestry")
    gallery = catalog.add("Navigation Wing")
    assert {astrolabe, tapestry, gallery}.issubset(set(catalog.things))

    # She names the curatorial relationship she cares about so future guides know
    # exactly how to read her intent.
    displayed_with = catalog.add_predicate("displayed_with")
    assert displayed_with in catalog.things

    # Mina binds her story: the astrolabe should be displayed with the tapestry in
    # the navigation wing. She verifies each statement to keep the prose honest.
    pairing = catalog.bind(astrolabe, displayed_with, tapestry)
    placement = catalog.bind(astrolabe, displayed_with, gallery)
    assert pairing.label == "Astrolabe displayed_with Silk Tapestry"
    assert placement.label == "Astrolabe displayed_with Navigation Wing"

    # Because tours are archived for audits, she saves a pickle and reloads it to
    # make sure no beats of the story vanished in transit.
    plan_path = tmp_path / "curator_story.pkl"
    catalog.save(plan_path.as_posix())
    loaded = Ontology.load(plan_path.as_posix())
    assert len(loaded.things) == len(catalog.things)
    loaded_statements = [t for t in loaded.things if isinstance(t, Statement)]
    assert any(stmt.label == pairing.label for stmt in loaded_statements)

    # Mina closes the rehearsal with a final check that the navigation wing is
    # still part of the story she will tell visitors.
    assert loaded.find_one("Navigation Wing") is not None
