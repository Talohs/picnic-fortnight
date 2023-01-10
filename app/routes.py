from app import app
from flask import render_template

@app.route("/")
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Dan', fruits=fruits)

@app.route("/posts")
def posts():
    return render_template('posts.html', name='Dan')

@app.route('/sign-up')
def signup():
    return render_template('sign-up.html', name='Dan')

@app.route('/log-in')
def login():
    return render_template('log-in.html', name='Dan')