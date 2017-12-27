from app import app
import requests
import hashlib
import time
from pprint import pprint
from flask import request, render_template, url_for


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
        'https://gateway.marvel.com:443/v1/public/characters?ts=' + str(ts) +
        'name=Spider-Man&apikey=' + public_key + '&hash=' + m)
    pprint(r.json())
    return "Marvelous"

@app.route('/test', methods = ['GET','POST'])
def test():
    print('hello')
    if request.method == 'POST':
        print(request.form)
        hero = request.form['nm']
        return render_template('results.html', hero = hero )

        # if request.form['form'] == 'nm':
        #     print('box info?')
        #     pass
        # if request.form['form'] == 'Spider-Man':
        #     print('button pressed')
        #     pass
    elif request.method == 'GET':
        return render_template('test.html')

>>>>>>> Stashed changes
