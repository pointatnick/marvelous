from app import utils


def test_parse_characters():
    assert utils.parse_characters('') == []
    assert utils.parse_characters('Spider-Man') == ['Spider-Man']