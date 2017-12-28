import time
import hashlib
import requests


public_key = '8bfbc491d6c583ad498640d6fa843487'
private_key = '0a9946e6e4f1cedbe03d7074f5feca19b33b3757'


def parse_input(input):
    # given a string, returns a list of strings
    # entries in result list do not have leading/ending whitespace
    characters = input.split(',')
    formatted_characters = []
    for character in characters:
        temp = character.strip()
        if temp != '':
            formatted_characters.append(temp)
    return formatted_characters


def get_cid(character):
    # given a character, returns the ID of that character from marvel API
    ts = time.time()
    hash_key = str(ts) + private_key + public_key
    m = hashlib.md5(hash_key.encode('utf-8')).hexdigest()
    r = requests.get(
        'https://gateway.marvel.com:443/v1/public/characters?ts={}&apikey={}&hash={}&name={}'.
        format(str(ts), public_key, m, character))
    result = r.json()['data']['results']
    # if API lookup returns no result, we return None
    if result == []:
        return None
    else:
        return result[0]['id']


def get_comic_list(cid):
    # given a character ID, returns the list of comics that character is featured in
    # marvel API only allows queries of 100 things at a time
    MARVEL_LIMIT = 100

    ts = time.time()
    hash_key = str(ts) + private_key + public_key
    m = hashlib.md5(hash_key.encode('utf-8')).hexdigest()
    offset = 0  # need to keep track of this to request next 100 titles
    titles = []
    while True:
        r2 = requests.get(
            'https://gateway.marvel.com:443/v1/public/characters/{}/comics?ts={}&apikey={}&hash={}&limit={}&offset={}'
            .format(
                str(cid), str(ts), public_key, m, str(MARVEL_LIMIT),
                str(offset)))
        count = r2.json()['data']['count']
        results = r2.json()['data']['results']
        offset = offset + MARVEL_LIMIT
        for result in results:
            titles.append(result['title'])
        if count < MARVEL_LIMIT:
            break
    print(titles)
    return titles


def build_comic_lists(cids):
    # given a list of character IDs, assembles comic lists from those IDs
    comic_lists = []
    for cid in cids:
        comic_lists.append(get_comic_list(cid))
    return comic_lists


def find_common_list(comics_lists):
    # given a list of a list of comic titles,
    # returns list of titles in both sets
    comic_sets = []
    for comic_list in comics_lists:
        comic_sets.append(set(comic_list))

    return set.intersection(*comic_sets)
