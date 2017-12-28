from app import utils


def test_parse_input():
    assert utils.parse_input('') == []
    assert utils.parse_input('Spider-Man') == ['Spider-Man']
    assert utils.parse_input('Spider-Man,     , Iron Man') == ['Spider-Man', 'Iron Man']


def test_get_cid():
    assert utils.get_cid('Spider-Man') == 1009610
    assert utils.get_cid('fake_char') == None