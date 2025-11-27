from __future__ import annotations

from dataclasses import dataclass, field

from .identifiers import next_id


def thing_set_factory() -> set[Thing]:  # pragma: no cover - trivial helper
    return set()


@dataclass(frozen=True)
class Thing:
    label: str
    id: int = field(default_factory=next_id, init=False)

    def __post_init__(self) -> None:
        if not self.label:
            raise ValueError("label cannot be empty")
