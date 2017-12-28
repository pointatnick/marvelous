from app import app, utils
from flask import request, render_template, url_for
import requests
import json
import hashlib
import time


@app.route('/')
@app.route('/index')
def index():
    return "Marvelous"


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/results')
def results():
    MARVEL_LIMIT = 100

    characters = utils.parse_input(request.args.get('text', ''))
    public_key = '8bfbc491d6c583ad498640d6fa843487'
    private_key = '0a9946e6e4f1cedbe03d7074f5feca19b33b3757'
    ts = time.time()
    hash_key = str(ts) + private_key + public_key
    m = hashlib.md5(hash_key.encode('utf-8')).hexdigest()
    r1 = requests.get(
        'https://gateway.marvel.com:443/v1/public/characters?ts={}&apikey={}&hash={}&name={}'.
        format(str(ts), public_key, m, characters[0]))
    cid = r1.json()['data']['results'][0]['id']

    ts = time.time()
    hash_key = str(ts) + private_key + public_key
    m = hashlib.md5(hash_key.encode('utf-8')).hexdigest()
    offset = 0
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
        print(titles, len(titles))
        if count < MARVEL_LIMIT:
            break
    # comics = utils.find_common_list(#list of comics)
    return render_template('results.html', comics=comics)
