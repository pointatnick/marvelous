from app import app, utils
from flask import request, render_template, url_for


@app.route('/')
@app.route('/index')
def index():
    return "Marvelous"


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/results')
def results():
    # get list of characters from input
    characters = utils.parse_input(request.args.get('text', ''))

    # get character IDs
    cids = []
    for character in characters:
        cids.append(utils.get_cid(character))

    comic_lists = utils.build_comic_lists(cids)
    comics = utils.find_common_list(comic_lists)
    print(comics)
    return render_template('results.html', comics=comics)


@app.route('/single')
def single():
    character = request.args.get('text','')
    if (character):
        return render_template('single.html', thing = character)
    else:
        return render_template('single.html')