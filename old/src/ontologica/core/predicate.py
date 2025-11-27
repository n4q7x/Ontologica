from __future__ import annotations

from dataclasses import dataclass

from .thing import Thing


@dataclass(frozen=True)
class Predicate(Thing):
    """Binary predicate; currently shares behavior with Thing."""
    pass
