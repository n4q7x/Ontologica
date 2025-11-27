from ontologica import Ontology
from src.ontologica.core.parser import Parser
import sys

def check_completeness(data_path):
    parser = Parser()
    triples = parser.parse_file(data_path)
    onto = Ontology()
    things = {}
    predicates = {}
    for subj, pred, obj in triples:
        if subj not in things:
            things[subj] = onto.add_thing(subj)
        if obj not in things:
            things[obj] = onto.add_thing(obj)
        if pred not in predicates:
            predicates[pred] = onto.add_predicate(pred)
        onto.bind(things[subj], predicates[pred], things[obj])
    # Placeholder completeness check
    # You can define what 'complete' means for your ontology
    is_complete = hasattr(onto, 'is_complete') and onto.is_complete() if callable(getattr(onto, 'is_complete', None)) else False
    if is_complete:
        print(f"Ontology loaded from {data_path} is COMPLETE.")
    else:
        print(f"Ontology loaded from {data_path} is NOT complete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_completeness.py <data_file>")
    else:
        check_completeness(sys.argv[1])
