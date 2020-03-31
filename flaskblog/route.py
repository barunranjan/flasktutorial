from flaskblog.model import User, Post
from flaskblog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from flaskblog.form import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
posts = [
    {
        'title': 'Facebook',
        'name': 'Varun',
        'date': '30 April 2020',
        'content': 'Facebook is a social networking site for connecting to friend'
    },

    {
        'title': 'Youtube',
        'name': 'Rahul',
        'date': '1 May 2020',
        'content': 'youtube is a social networking site for watching video'
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account have been created with {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
         user = User.query.filter_by(email=form.email.data).first()
         if user and bcrypt.check_password_hash(user.password, form.password.data):
             login_user(user, remember=form.remember.data)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect(url_for('home'))
         else:
            flash("Wrong User name or password", 'danger')
    return render_template('login.html', title='Registration', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')