# from flask import Flask
import flask
from flask import request, redirect
import pandas as pd
from dbutils import connect_to_db, create_table, search_row, insert_row, display, delete_row, search_for_id, update_row

app = flask.Flask(__name__)

if __name__ == "__app__":
    app.run(debug=True, port=5000)

@app.route("/")
def any():
    return redirect("/home")

@app.route("/home", methods=['Get'])
def home_page():
    connect_to_db()
    return flask.render_template('search.html')

@app.route("/addpage")
def add_page():
    return flask.render_template('add.html')

@app.route("/editpage")
def edit_page():
    return flask.render_template('update.html')

@app.route("/deletepage")
def delete_page():
    return flask.render_template('delete.html')

# !!! CRUD
@app.route("/search", methods=['Get'])
def search():
    title = request.args.get('title')
    results = search_row(title)
    # print(results)
    return results

@app.route("/displayall", methods=['Get'])
def display_all():
    results = display()
    return results
    

@app.route("/add", methods=['Post'])
def add_row():
    #* NOTE: 
    #* if the http request is post and the passed data is in json format
    #* use request.json
    #* data.get
    #* if on url, use get params
    data = request.json
    title = data.get('title')
    genre = data.get('genre')
    date = data.get('date')

    print(title)
    print(genre)
    print(date)
    results = insert_row(title, genre, date)
    return results

@app.route("/delete", methods=['DELETE'])
def delete():
    book_id = request.args.get('bookID')
    # Debugging print
    print(f"BookID to delete: {book_id}")

    result = delete_row(book_id)
    return result

@app.route("/searchByID", methods=['GET'])
def search_by_id():
    book_id = request.args.get('bookID')
    print(book_id)
    results = search_for_id(book_id)
    # print(results)
    return results

@app.route("/update", methods=['POST'])
def update():
    data = request.json
    book_id = data.get('bookID')
    title = data.get('title')
    genre = data.get('genre')
    date = data.get('date')
    result = update_row(book_id, title, genre, date)
    
    return result
