from __future__ import annotations

from ontologica import Predicate


def test_predicate_preserves_label() -> None:
    likes = Predicate("likes")

    assert likes.label == "likes"
    assert repr(likes)
