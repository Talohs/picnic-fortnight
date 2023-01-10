from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import Signupform

@app.route("/")
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Dan', fruits=fruits)

@app.route("/posts")
def posts():
    return render_template('posts.html', name='Dan')

@app.route('/sign-up',  methods=['GET', 'POST'])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        print('Form submitted and validated')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        flash('Thank you for signing up', 'success')
        #After sign-up redirect to home
        
        # TODO: Check to see if there is a User with that username
        if username == 'Taloh':
            flash('That user already exists', 'danger')
            return redirect(url_for('signup'))
        # TODO: Create a new user with form data and add to database

        # redirect back to home
        return redirect(url_for('index'))
    return render_template('sign-up.html', form=form)

@app.route('/log-in',)
def login():
    return render_template('log-in.html', name='Dan')