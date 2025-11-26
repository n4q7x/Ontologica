from __future__ import annotations

from pathlib import Path

from ontologica import Ontology, Predicate, Statement


def test_pickle_round_trip_behaves_like_database_dump(simple_ontology: tuple[Ontology, object, object, Predicate], tmp_path: Path) -> None:
    onto, alice, bob, likes = simple_ontology
    onto.bind(alice, likes, bob)

    path = tmp_path / "onto.pkl"
    onto.save(path.as_posix())

    restored = Ontology.load(path.as_posix())
    assert len(restored.things) == len(onto.things)
    assert any(isinstance(t, Statement) for t in restored.things)


def test_json_round_trip_behaves_like_query_export(simple_ontology: tuple[Ontology, object, object, Predicate], tmp_path: Path) -> None:
    onto, alice, bob, likes = simple_ontology
    onto.bind(alice, likes, bob)

    path = tmp_path / "onto.json"
    onto.save_json(path.as_posix())

    restored = Ontology.load_json(path.as_posix())
    assert len(restored.things) == len(onto.things)
    labels = {t.label for t in restored.things}
    assert {"Alice", "Bob", "Alice likes Bob"}.issubset(labels)
