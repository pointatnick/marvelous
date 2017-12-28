import time
import hashlib
import requests


def parse_input(input):
    # given a string, returns a list of strings, delimited by ','
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
    public_key = '8bfbc491d6c583ad498640d6fa843487'
    private_key = '0a9946e6e4f1cedbe03d7074f5feca19b33b3757'
    ts = time.time()
    hash_key = str(ts) + private_key + public_key
    m = hashlib.md5(hash_key.encode('utf-8')).hexdigest()
    r = requests.get(
        'https://gateway.marvel.com:443/v1/public/characters?ts={}&apikey={}&hash={}&name={}'.
        format(str(ts), public_key, m, character))
    return r.json()['data']['results'][0]['id']


def find_common_list(comics_lists):
    # given a list of a list of comic titles,
    # returns list of titles in both sets
    comics_sets = []
    for comics in comics_lists:
        comics_sets.append(set(comics))

    return set.intersection(*comics_sets)