import pytest
from src.ontologica.core.parser import Parser

def test_parse_triples_basic():
    parser = Parser()
    text = """
    # Example triples
    (A, likes, B)
    (B, knows, C)
    """
    triples = parser.parse(text)
    assert triples == [
        ("A", "likes", "B"),
        ("B", "knows", "C")
    ]

def test_parse_triples_ignores_comments_and_blanks():
    parser = Parser()
    text = """
    # This is a comment
    
    (X, is_a, Y)
    
    # Another comment
    (Y, part_of, Z)
    """
    triples = parser.parse(text)
    assert triples == [
        ("X", "is_a", "Y"),
        ("Y", "part_of", "Z")
    ]

def test_write_triples(tmp_path):
    parser = Parser()
    triples = [
        ("A", "likes", "B"),
        ("B", "knows", "C")
    ]
    out_file = tmp_path / "triples.txt"
    parser.write_triples(triples, out_file, header="# Header")
    content = out_file.read_text()
    assert "# Header" in content
    assert "(A, likes, B)" in content
    assert "(B, knows, C)" in content
