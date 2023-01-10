from app import app
from flask import render_template
from app.forms import Signupform

@app.route("/")
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Dan', fruits=fruits)

@app.route("/posts")
def posts():
    return render_template('posts.html', name='Dan')

@app.route('/sign-up')
def signup():
    form = Signupform()
    return render_template('sign-up.html', form=form)

@app.route('/log-in')
def login():
    return render_template('log-in.html', name='Dan')