from app import app, utils
from flask import request, render_template, url_for
import requests
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
    # marvel API only allows queries of 100 things at a time
    MARVEL_LIMIT = 100

    # get list of characters from input
    characters = utils.parse_input(request.args.get('text', ''))

    # get character IDs
    cids = []
    for character in characters:
        cids.append(utils.get_cid(character))

    # ts = time.time()
    # hash_key = str(ts) + private_key + public_key
    # m = hashlib.md5(hash_key.encode('utf-8')).hexdigest()
    # offset = 0
    # titles = []
    # while True:
    #     r2 = requests.get(
    #         'https://gateway.marvel.com:443/v1/public/characters/{}/comics?ts={}&apikey={}&hash={}&limit={}&offset={}'
    #         .format(
    #             str(cid), str(ts), public_key, m, str(MARVEL_LIMIT),
    #             str(offset)))
    #     count = r2.json()['data']['count']
    #     results = r2.json()['data']['results']
    #     offset = offset + MARVEL_LIMIT
    #     for result in results:
    #         titles.append(result['title'])
    #     print(titles, len(titles))
    #     if count < MARVEL_LIMIT:
    #         break
    # comics = utils.find_common_list(#list of comics)
    return render_template('results.html', comics=comics)
