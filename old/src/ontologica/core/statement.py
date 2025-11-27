from __future__ import annotations

from dataclasses import dataclass

from .identifiers import next_id
from .predicate import Predicate
from .thing import Thing


@dataclass(frozen=True)
class Statement(Thing):
    subject: Thing
    predicate: Predicate
    obj: Thing

    def __init__(self, label: str, subject: Thing, predicate: Predicate, obj: Thing):
        # Work around frozen dataclass by using object.__setattr__ and manual ids.
        object.__setattr__(self, "label", label)
        object.__setattr__(self, "id", next_id())
        object.__setattr__(self, "subject", subject)
        object.__setattr__(self, "predicate", predicate)
        object.__setattr__(self, "obj", obj)
