# ontology_cli.py

import argparse
import os
from typing import Optional, Union

from src.core.ontology import Ontology, Thing, Predicate, Statement, Key


def load_or_new(path: str) -> Ontology:
    if os.path.exists(path):
        return Ontology.load(path)
    return Ontology()


def parse_key(raw: Optional[str]) -> Optional[Key]:
    """
    Try to interpret a CLI string as int (id) if it looks like an int,
    otherwise keep it as a string (label).
    """
    if raw is None:
        return None
    raw = raw.strip()
    if raw.isdigit():
        return int(raw)
    return raw


def cmd_new(args: argparse.Namespace) -> None:
    onto = Ontology()
    onto.save(args.file)
    print(f"Created new ontology at {args.file}")


def cmd_add(args: argparse.Namespace) -> None:
    onto = load_or_new(args.file)
    t = onto.add(args.label)
    onto.save(args.file)
    print(f"Added Thing: {t!r}")


def cmd_add_predicate(args: argparse.Namespace) -> None:
    onto = load_or_new(args.file)
    p = onto.add_predicate(args.label)
    onto.save(args.file)
    print(f"Added Predicate: {p!r}")


def cmd_bind(args: argparse.Namespace) -> None:
    onto = load_or_new(args.file)

    subj_key = parse_key(args.subject)
    pred_key = parse_key(args.predicate)
    obj_key = parse_key(args.object)

    subj = onto.find_one(subj_key) if subj_key is not None else None
    pred = onto.find_one(pred_key) if pred_key is not None else None
    obj = onto.find_one(obj_key)   if obj_key is not None else None

    if subj is None:
        raise SystemExit(f"Could not find subject {args.subject!r}")
    if pred is None or not isinstance(pred, Predicate):
        raise SystemExit(f"Could not find predicate {args.predicate!r} (or it is not a Predicate)")
    if obj is None:
        raise SystemExit(f"Could not find object {args.object!r}")

    stmt = onto.bind(subj, pred, obj)
    onto.save(args.file)
    print("Added Statement:")
    onto._pretty_print_thing(stmt)  # reuse pretty printer


def cmd_enumerate(args: argparse.Namespace) -> None:
    onto = load_or_new(args.file)
    onto.enumerate()
    onto.save(args.file)
    print("Enumerated all possible statements over current Things/Predicates.")


def cmd_show(args: argparse.Namespace) -> None:
    onto = load_or_new(args.file)

    key = parse_key(args.key)
    subject = parse_key(args.subject)
    predicate = parse_key(args.predicate)
    object_ = parse_key(args.object)

    onto.show(
        key=key,
        subject=subject,
        predicate=predicate,
        object=object_,
    )


def cmd_export_json(args: argparse.Namespace) -> None:
    onto = load_or_new(args.file)
    onto.save_json(args.json)
    print(f"Exported ontology in JSON format to {args.json}")


def cmd_import_json(args: argparse.Namespace) -> None:
    onto = Ontology.load_json(args.json)
    onto.save(args.file)
    print(f"Imported ontology from JSON {args.json} into {args.file}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ontology-cli", description="Ontology CLI tool")
    p.add_argument(
        "--file",
        "-f",
        default="ontology.pkl",
        help="Path to ontology pickle file (default: ontology.pkl)",
    )

    sub = p.add_subparsers(dest="command", required=True)

    # new
    sp = sub.add_parser("new", help="Create a new, empty ontology file")
    sp.set_defaults(func=cmd_new)

    # add
    sp = sub.add_parser("add", help="Add an atomic Thing with a label")
    sp.add_argument("label", help="Label of the Thing")
    sp.set_defaults(func=cmd_add)

    # add-predicate
    sp = sub.add_parser("add-predicate", help="Add a Predicate with a label")
    sp.add_argument("label", help="Label of the Predicate")
    sp.set_defaults(func=cmd_add_predicate)

    # bind
    sp = sub.add_parser("bind", help="Create a Statement (subject predicate object)")
    sp.add_argument("subject", help="Subject (id or label)")
    sp.add_argument("predicate", help="Predicate (id or label)")
    sp.add_argument("object", help="Object (id or label)")
    sp.set_defaults(func=cmd_bind)

    # enumerate
    sp = sub.add_parser("enumerate", help="Generate all possible statements")
    sp.set_defaults(func=cmd_enumerate)

    # show
    sp = sub.add_parser("show", help="Show parts of the ontology")
    sp.add_argument(
        "--key",
        help="Global search key (id or label): show things + statements containing them",
    )
    sp.add_argument(
        "--subject",
        help="Filter statements by subject (id or label)",
    )
    sp.add_argument(
        "--predicate",
        help="Filter statements by predicate (id or label)",
    )
    sp.add_argument(
        "--object",
        help="Filter statements by object (id or label)",
    )
    sp.set_defaults(func=cmd_show)

    # export-json
    sp = sub.add_parser("export-json", help="Export ontology to JSON")
    sp.add_argument("json", help="Path to JSON file")
    sp.set_defaults(func=cmd_export_json)

    # import-json
    sp = sub.add_parser("import-json", help="Import ontology from JSON")
    sp.add_argument("json", help="Path to JSON file")
    sp.set_defaults(func=cmd_import_json)

    return p


def main(argv: Optional[list[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
