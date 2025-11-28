


from ontology import Ontology

filepath = "badfilename"


try:
    ontology = Ontology(filepath)
except FileNotFoundError:
    print("File not found!")

