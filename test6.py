



from ontology import Ontology


try:
    ontology = Ontology("data.json")
except FileNotFoundError:
    print("File not found!")
