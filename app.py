from flask import Flask, render_template, request, jsonify
from search import *
from watchlist_entry import *
from get_details import *
from db_connect import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    user_query = request.form['search_name']

    search_obj = Search()
    movie_data, series_data = search_obj.search_all(user_query)

    return render_template('search.html', mdata=movie_data, sdata=series_data)


@app.route('/details', methods=['POST', 'GET'])
def details():
    content_id = request.form['content_id']
    details_obj = Details()
    content_data = details_obj.get_details(content_id)

    return render_template('details.html', data=content_data)


@app.route('/watchlist_entry', methods=['POST'])
def watchlist_entry():
    content_id = request.json['content_id']

    entry_obj = AddEntry()
    content_data = entry_obj.new_entry(content_id)

    db_obj = Database()
    db_obj.database_connect()
    db_obj.database_dump(content_data)
    db_obj.database_close()

    return jsonify({'status': 'success'}), 200


@app.route('/delete_entry', methods=['GET', 'POST'])
def delete_entry():
    content_id = request.form['content_id']

    db_obj = Database()
    db_obj.database_connect()
    db_obj.database_delete_entry(content_id)
    content_data = db_obj.database_load()
    db_obj.database_close()

    return render_template('watchlist.html', data=content_data)


@app.route('/watchlist', methods=['GET', 'POST'])
def watchlist():
    db_obj = Database()
    db_obj.database_connect()
    content_data = db_obj.database_load()
    db_obj.database_close()

    return render_template('watchlist.html', data=content_data)


if __name__ == '__main__':
    app.run(debug=True)
