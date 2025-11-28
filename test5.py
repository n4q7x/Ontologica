

from ontology import Ontology


try:
    ontology = Ontology("mydata.cql")
except ValueError:
    print("Unsupported extension!")
