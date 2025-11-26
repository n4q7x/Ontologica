from ontologica import Ontology
from src.ontologica.core.parser import Parser
import sys

def enumerate_ontology(data_path):
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
    parser.write_triples(
        [(stmt.subject.name, stmt.predicate.name, stmt.object.name) for stmt in onto.statements],
        data_path,
        header="# Enumerated Ontologica Triples"
    )
    print(f"Enumerated {len(onto.statements)} triples written to {data_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python enumerate.py <data_file>")
    else:
        enumerate_ontology(sys.argv[1])
