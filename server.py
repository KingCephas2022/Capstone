from flask import render_template, request, session, render_template, request, redirect, flash
#import string
#import random
from extentions import db
from models import Url,User
from app import create_app,generate_short_url

app = create_app()

@app.route("/")
def home():
        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Create a new user
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists in the database
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user_id'] = user.id
            return render_template('shortener.html')
        else:
            return 'Invalid username or password'

    return render_template('login.html')


@app.route('/shorten', methods=['POST', 'GET'])
def shorten():
    original_url = request.form['url']

    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = generate_short_url()  # Generate a unique short URL
        url = Url(original_url=original_url, short_url=short_url)
        db.session.add(url)
        db.session.commit()

        flash('Shortened URL created successfully!')
     
    return render_template('shortner.html')

@app.route("/about")
def about():
        return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)