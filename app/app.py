import json
from flask import Flask, request, render_template

from data_process.search import search as the_search

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


# @app.route('/search-form', methods=['GET'])
# def search():
#     query = request.args.get('q').strip()
#     if len(query) == 0:
#         return render_template('query-erro.html')
#
#     data = json.loads(the_search(query))
#     data = data[list(data.keys())[0]]
#
#     return render_template('search.html', data=data)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q').strip()
    if len(query) == 0:
        return render_template('query-erro.html')
    return the_search(query)


if __name__ == '__main__':
    app.run()
