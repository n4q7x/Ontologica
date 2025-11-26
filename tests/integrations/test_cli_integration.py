from __future__ import annotations

from pathlib import Path

import pytest

from ontologica import Ontology
from ontologica.cli.cli import main as cli_main


def run_cli(*args: str) -> None:
    cli_main(list(args))


def test_cli_drives_add_and_bind(tmp_path: Path) -> None:
    store = tmp_path / "cli_integration.pkl"

    run_cli("--file", store.as_posix(), "new")
    run_cli("--file", store.as_posix(), "add", "Alice")
    run_cli("--file", store.as_posix(), "add", "Bob")
    run_cli("--file", store.as_posix(), "add-predicate", "likes")
    run_cli("--file", store.as_posix(), "bind", "Alice", "likes", "Bob")

    ont = Ontology.load(store.as_posix())
    assert ont.find_one("Alice likes Bob") is not None


def test_cli_show_filters_by_predicate(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    store = tmp_path / "cli_show.pkl"
    run_cli("--file", store.as_posix(), "new")
    run_cli("--file", store.as_posix(), "add", "City")
    run_cli("--file", store.as_posix(), "add", "Park")
    run_cli("--file", store.as_posix(), "add-predicate", "adjacent_to")
    run_cli("--file", store.as_posix(), "bind", "City", "adjacent_to", "Park")

    run_cli("--file", store.as_posix(), "show", "--predicate", "adjacent_to")

    captured = capsys.readouterr()
    assert "adjacent_to" in captured.out
    assert "City" in captured.out
    assert "Park" in captured.out
