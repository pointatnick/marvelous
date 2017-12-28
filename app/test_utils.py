from app import utils


def test_parse_input():
    assert utils.parse_input('') == []
    assert utils.parse_input('Spider-Man') == ['Spider-Man']
    