from __future__ import annotations

from itertools import count

_id_counter = count()


def next_id() -> int:
    """Return the next unique identifier for Thing-derived instances."""
    return next(_id_counter)


def reset_counter(start: int) -> None:
    """Reset the global identifier counter so future ids begin at start."""
    global _id_counter
    _id_counter = count(start)
