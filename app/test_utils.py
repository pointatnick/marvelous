from app import utils


# def test_parse_input():
#     assert utils.parse_input('') == []
#     assert utils.parse_input('Spider-Man') == ['Spider-Man']

def test_find_common_list():
    assert utils.find_common_list([[1,2,3],[2,3,4]]) == {2,3}
    assert utils.find_common_list([[],[]]) == set()
    assert utils.find_common_list([[],[],[]]) == set()
    assert utils.find_common_list([[1],[2]]) == set()
    
def test_parse_input():
    assert utils.parse_input('') == []
    assert utils.parse_input('Spider-Man') == ['Spider-Man']
    assert utils.parse_input('Spider-Man,     , Iron Man') == ['Spider-Man', 'Iron Man']

def test_get_cid():
    assert utils.get_cid('Spider-Man') == 1009610
