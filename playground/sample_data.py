from ontologica import Ontology

# Create an ontology instance
onto = Ontology()

# Add real-world public figures
elon = onto.add_thing("Elon Musk")
taylor = onto.add_thing("Taylor Swift")
pope = onto.add_thing("Pope Francis")

# Add predicates
born_in = onto.add_predicate("born_in")
profession = onto.add_predicate("profession")
nationality = onto.add_predicate("nationality")

# Add places
pretoria = onto.add_thing("Pretoria")
pennsylvania = onto.add_thing("Pennsylvania")
buenos_aires = onto.add_thing("Buenos Aires")

# Add professions
entrepreneur = onto.add_thing("Entrepreneur")
singer = onto.add_thing("Singer")
religious_leader = onto.add_thing("Religious Leader")

# Add nationalities
south_african = onto.add_thing("South African")
american = onto.add_thing("American")
argentine = onto.add_thing("Argentine")

# Bind facts
onto.bind(elon, born_in, pretoria)
onto.bind(elon, profession, entrepreneur)
onto.bind(elon, nationality, south_african)

onto.bind(taylor, born_in, pennsylvania)
onto.bind(taylor, profession, singer)
onto.bind(taylor, nationality, american)

onto.bind(pope, born_in, buenos_aires)
onto.bind(pope, profession, religious_leader)
onto.bind(pope, nationality, argentine)

# Save for CLI loading (if needed)
# Example: onto.save('playground/sample_ontology.pkl')

# Print summary
onto.show()