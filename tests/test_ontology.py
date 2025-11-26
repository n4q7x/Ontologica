from ontologica import Ontology


def test_imports():
    """Test that core modules can be imported."""
    assert Ontology is not None


def test_create_ontology():
    """Test that we can instantiate an Ontology."""
    onto = Ontology()
    assert onto is not None


def test_basic_functionality():
    """Test basic usage works."""
    onto = Ontology()
    entity = onto.add("Alice")
    assert entity.label == "Alice"