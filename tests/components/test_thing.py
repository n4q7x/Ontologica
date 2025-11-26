from __future__ import annotations

import pytest

from ontologica import Thing


def test_thing_requires_non_empty_label() -> None:
    atom = Thing("Alice")

    assert atom.label == "Alice"
    assert isinstance(atom.id, int)

    with pytest.raises(ValueError):
        Thing("")
