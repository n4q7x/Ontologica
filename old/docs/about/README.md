
This repo is the current iteration of my years-long quest to build formal ontology tools.

The current iteration is the consummation of years of self-directed research into the necessary topics surrounding formal ontology ("FO"), including logic, linguistics, philosophy, metaphysics, cognitive science, type theory, computer science, category theory, functional programming, web development, databases, the semantic web, and more.

The design will continue to change, but this is the closest I have come to a usable tool. My hope is that the development can take a turn to a stage where features are added and areas for improvement identified whilst the tool has an active, if modest, user base.

Ontologica takes design influence from many pre-existing ideas and tools: basic formal ontology (BFO), the information economy metalanguage (IEML), Haskell, Prolog, categorical query language, SQL, Neo4j, Protégé, and numerous thinkers such as Frege, Bertrand Russell, Per Martin-Löf, Alan Turing, David Spivak, and so on (this list to be added to). In a way, I cannot claim to have invented anything original, but am only trying to put together the many features and design choices of such things into one system that feels perfect to me, has everything I would like, and not more. This project is intended to be only the beginning of a longer research inquest into seeing how formal ontology can be more common amongst non-technical users and could lead to a different kind of internet called the "datanet". Again, I wish to stress that none of these ideas are new, but I am simply repackaging classic, established ideas like relational data models, graph databases, RDF, the semantic web, etc, but trying to breathe new life into them, synthesize them and put my own finishing touches on them. I would like to emphasize that one of the most important features an ontology system should have, in my opinion, is **reification** (discussed further, below).

I am 30 years old and have more or less decided at this point that increasing the use of formal ontologies in society has become my mission on Earth. Please, please consider contributing to this work by donating or becoming a sponsor. I would also be open to having an assistant who can help me with outreach, promoting the tool, networking and fundraising. Thank you.


***

Ontologica is currently a Python module, a CLI tool, and soon, a GUI application. 

Once the ability to construct personal ontologies for oneself feels sufficiently comfortably designed, I will begin exploring how people can share their ontologies with other people, link their ontological nodes, entries and records with other people's, validate public nodes for their semantic accuracy, and so on.

Ontologica's data model, currently - or, its own meta-ontology, perhaps - is based on the notions of "things" and "predicates", largely. However, I am still devoting a lot of thought to questions of how predicates and things are composed, what fundamental type that should be, and if there will be other fundamental types, as well.

I decided to develop it in Python because it is the language I am most experienced in; it has an ecosystem and community that values usability, cleanness, and readability; it is often used in modern data science-related applications; and it is versatile and can handle virtually the entire application development from back to front, bottom to top.

Ontologica is for creating **persistent** ontologies - people are intended to use it to make ontologies that they will use in their work and daily lives. Building a good ontology can mean the refinement of a precious data artifact. That is why Ontologica will have features making it similar to a database system or language. Because it emphasizes readability and portability, it currently persists ontologies in a simple text file format. Time will tell if eventually the goal would be to be able to export (and import, and manipulate between) many formats like JSON, Turtle, SQLite, plaintext, and so on.

It is possible that some day Ontologica will actually become its own programming language, analogous to Wolfram Mathematica, ushering in a new paradigm of "ontological programming".

It is possible that in the future, Ontologica will support predicates of any finite arity. Currently, all predicates are binary.

Ontologica is open-source and always will be. Unfortunately, the formal ontology space does not yet have a premier, open-source tool. A lot of the best graph database tools are closed-source.

## Installation and demo of current version (0.1.0)

For now, you can clone the repo and run its scripts yourself in Python. Soon, hopefully it will be packaged for pip.



## "Semantic gauging" and iterative, bottom-up design

In this section I will explain why Ontologica is such a useful design tool to structure one's own thinking, using the central technique of "semantic gauging" for iterative ontology design and refinement. This is related to and influenced by the concept of "clause testing" in linguistics.







