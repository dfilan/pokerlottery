from flask import Blueprint, render_template, request

from pokerlottery.compute_winner import compute_winner

bp = Blueprint('index', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        info_array = []
        # TODO rewrite this logic
        # in particular what if there aren't exactly 6 players
        # also: maybe separate out a thing so that you can do something like a 'post' just by going to a URL
        # so maybe it's not actually a post request, but a get request with a query string?
        for i in range(6):
            name = request.form[f'name{i}']
            lucky_word = request.form[f'lucky_word{i}']
            chip_count = int(request.form[f'chip_count{i}'])
            info_array.append({'name': name, 'lucky_word': lucky_word, 'chip_count': chip_count})
        winner = compute_winner(info_array)
        return render_template('winner/index.html', winner=winner, info_array=info_array)
    return render_template('index/index.html')
