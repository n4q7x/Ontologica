from __future__ import annotations

from pathlib import Path

from ontologica import Ontology
from ontologica.cli.cli import main as cli_main


def test_cli_like_workflow(tmp_path: Path) -> None:
    store = tmp_path / "cli_story.pkl"
    store_arg = ["--file", store.as_posix()]

    print("🆕 CLI user initializes repository")
    cli_main(store_arg + ["new"])

    print("➕ CLI adds two things and a predicate")
    cli_main(store_arg + ["add", "Alice"])
    cli_main(store_arg + ["add", "Bob"])
    cli_main(store_arg + ["add-predicate", "likes"])

    print("🔗 CLI binds Alice likes Bob")
    cli_main(store_arg + ["bind", "Alice", "likes", "Bob"])

    print("📤 CLI exports JSON snapshot")
    json_path = tmp_path / "cli_story.json"
    cli_main(store_arg + ["export-json", json_path.as_posix()])

    print("📥 CLI imports snapshot into new file")
    clone_path = tmp_path / "cli_story_clone.pkl"
    cli_main(["--file", clone_path.as_posix(), "import-json", json_path.as_posix()])

    print("🔍 Test verifies stored ontology contents")
    onto = Ontology.load(clone_path.as_posix())
    assert onto.find_one("Alice") is not None
    assert onto.find_one("likes") is not None
    assert onto.find_one("Bob") is not None
    assert any(stmt.label == "Alice likes Bob" for stmt in onto.things)

    print("✅ CLI story finished with", len(onto.things), "things")
