


from ontology import Ontology


try:
    ontology = Ontology("mydata")
except ValueError:
    print("File has no extension!")

