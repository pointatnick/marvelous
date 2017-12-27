from app import app
import requests
import hashlib
import time
from pprint import pprint


@app.route('/')
@app.route('/index')
def index():
    public_key = '8bfbc491d6c583ad498640d6fa843487'
    private_key = '0a9946e6e4f1cedbe03d7074f5feca19b33b3757'
    ts = time.time()
    print(ts)
    hash_key = str(ts) + private_key + public_key
    print(hash_key)
    m = hashlib.md5(hash_key.encode('utf-8')).hexdigest()
    print(m)
    r = requests.get(
        'https://gateway.marvel.com:443/v1/public/characters?ts=' + str(ts)
        + '&apikey=' + public_key
        + '&hash=' + m
        + '&name=Spider-Man')
    pprint(r.json())
    return "Marvelous"