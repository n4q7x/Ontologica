




# first, you want to know .. what phonemes exist.


"""

p = Ontology(label="phonology")

p.add_entities([
    "phoneme",
    "phonology",
    "schwa",
    "IPA alphabet"
])

p.add_predicates([
    "has as sound",
    "has as name",
    "has as IPA glyph",
    "being a part of"
])

p.assert([
    "class IPA_alphabet is incomplete"
])

p.test() # ERROR: Ontology is incomplete.

p.show_facts()

p.enumerate()

p.infer() # maybe, if we declare using types makes things a lot easier i guess....


"""