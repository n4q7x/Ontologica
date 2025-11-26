from __future__ import annotations

import json
import pickle
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, Optional, TypeVar, Union

from .identifiers import reset_counter
from .predicate import Predicate
from .statement import Statement
from .thing import Thing, thing_set_factory

Key = Union[Thing, int, str]
TThing = TypeVar("TThing", bound=Thing)


@dataclass
class Ontology:
    things: set[Thing] = field(default_factory=thing_set_factory)

    # --- internal: low-level register for any Thing subclass ---

    def _register(self, thing: TThing) -> TThing:
        """Internal: add an existing Thing/Predicate/Statement to the set."""
        self.things.add(thing)
        return thing

    # --- public construction API ---

    def add(self, label: str) -> Thing:
        """Create a plain Thing (an atom) with this label and add it."""
        return self._register(Thing(label))

    def add_predicate(self, label: str) -> Predicate:
        """Create a Predicate with this label and add it."""
        return self._register(Predicate(label))

    def __iter__(self) -> Iterable[Thing]:
        return iter(self.things)

    # --- internal helper: resolve Key -> *all* matching Things ---

    def _resolve_things(self, key: Key) -> set[Thing]:
        if isinstance(key, Thing):
            return {key}
        result: set[Thing] = set()
        if isinstance(key, int):
            for t in self.things:
                if t.id == key:
                    result.add(t)
        else:  # str
            for t in self.things:
                if t.label == key:
                    result.add(t)
        return result

    # --- helpful public lookup (single match) for CLI / callers ---

    def find_one(self, key: Key) -> Optional[Thing]:
        matches = self._resolve_things(key)
        if not matches:
            return None
        return next(iter(matches))

    # --- bind: create a Statement and add it ---

    def bind(self, subject: Thing, predicate: Predicate, obj: Thing) -> Statement:
        self._register(subject)
        self._register(predicate)
        self._register(obj)

        fused_label = f"{subject.label} {predicate.label} {obj.label}"
        stmt = Statement(
            label=fused_label,
            subject=subject,
            predicate=predicate,
            obj=obj,
        )
        return self._register(stmt)

    # --- enumerate all possible statements ---

    def enumerate(self) -> None:
        all_things = list(self.things)
        predicates = [t for t in all_things if isinstance(t, Predicate)]

        for subj in all_things:
            for pred in predicates:
                for obj in all_things:
                    self.bind(subj, pred, obj)

    # --- internal slice ---

    def _slice(self, key: Key, attr: str) -> set[Statement]:
        targets = self._resolve_things(key)
        if not targets:
            return set()

        result: set[Statement] = set()
        for t in self.things:
            if isinstance(t, Statement) and getattr(t, attr) in targets:
                result.add(t)
        return result

    # --- pretty-print helper for a single Thing (recursive on Statement) ---

    def _pretty_print_thing(self, t: Thing, indent: int = 0) -> None:
        pad = " " * indent

        if isinstance(t, Statement):
            print(f"{pad}Statement(label={t.label!r}, id={t.id})")
            print(f"{pad}  subject:")
            self._pretty_print_thing(t.subject, indent + 4)
            print(f"{pad}  predicate:")
            self._pretty_print_thing(t.predicate, indent + 4)
            print(f"{pad}  object:")
            self._pretty_print_thing(t.obj, indent + 4)
        else:
            print(pad + repr(t))

    # --- universal show() ---

    def show(
        self,
        key: Key | None = None,
        *,
        subject: Key | None = None,
        predicate: Key | None = None,
        object: Key | None = None,
    ) -> None:
        results: set[Thing] = set()
        stmt_filters: list[set[Statement]] = []

        if subject is not None:
            stmt_filters.append(self._slice(subject, "subject"))
        if predicate is not None:
            stmt_filters.append(self._slice(predicate, "predicate"))
        if object is not None:
            stmt_filters.append(self._slice(object, "obj"))

        if stmt_filters:
            stmts = stmt_filters[0].copy()
            for sset in stmt_filters[1:]:
                stmts &= sset
            results.update(stmts)

        if key is not None:
            targets = self._resolve_things(key)
            results.update(targets)
            for t in self.things:
                if isinstance(t, Statement):
                    if (
                        t.subject in targets
                        or t.predicate in targets
                        or t.obj in targets
                    ):
                        results.add(t)

        if not results and key is None and not stmt_filters:
            results = set(self.things)

        def sort_key(x: Thing):
            if isinstance(x, Statement):
                kind_rank = 2
            elif isinstance(x, Predicate):
                kind_rank = 1
            else:
                kind_rank = 0
            return (kind_rank, x.label, x.id)

        for t in sorted(results, key=sort_key):
            self._pretty_print_thing(t)
            print()

    # --- pickle persistence ---

    def save(self, path: str) -> None:
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path: str) -> Ontology:
        with open(path, "rb") as f:
            onto: Ontology = pickle.load(f)

        max_id = max((t.id for t in onto.things), default=-1)
        reset_counter(max_id + 1 if max_id >= 0 else 0)
        return onto

    # --- portable JSON export/import ---

    def to_dict(self) -> Dict[str, Any]:
        data_things: list[Dict[str, Any]] = []
        for t in self.things:
            item: Dict[str, Any] = {
                "id": t.id,
                "label": t.label,
            }
            if isinstance(t, Statement):
                item["kind"] = "Statement"
                item["subject_id"] = t.subject.id
                item["predicate_id"] = t.predicate.id
                item["object_id"] = t.obj.id
            elif isinstance(t, Predicate):
                item["kind"] = "Predicate"
            else:
                item["kind"] = "Thing"
            data_things.append(item)
        return {"things": data_things}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Ontology:
        onto = cls()
        id_map: Dict[int, Thing] = {}
        max_id = -1

        for item in data.get("things", []):
            kind = item["kind"]
            if kind == "Statement":
                continue
            label = item["label"]
            saved_id = item["id"]
            max_id = max(max_id, saved_id)

            if kind == "Thing":
                obj = Thing(label)
            elif kind == "Predicate":
                obj = Predicate(label)
            else:
                raise ValueError(f"Unknown kind: {kind!r}")

            object.__setattr__(obj, "id", saved_id)
            id_map[saved_id] = obj
            onto._register(obj)

        for item in data.get("things", []):
            if item["kind"] != "Statement":
                continue
            label = item["label"]
            saved_id = item["id"]
            max_id = max(max_id, saved_id)

            subj = id_map[item["subject_id"]]
            pred_thing = id_map[item["predicate_id"]]
            obj = id_map[item["object_id"]]

            if not isinstance(pred_thing, Predicate):
                raise ValueError(f"Expected Predicate, got {type(pred_thing)}")

            stmt = Statement(
                label=label,
                subject=subj,
                predicate=pred_thing,
                obj=obj,
            )
            object.__setattr__(stmt, "id", saved_id)
            id_map[saved_id] = stmt
            onto._register(stmt)

        reset_counter(max_id + 1 if max_id >= 0 else 0)
        return onto

    def save_json(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load_json(cls, path: str) -> Ontology:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)
