from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user


@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()  # class instance
    if form.validate_on_submit():  # this is executed when user submits form
        # if everything is valid, it will go here
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:  # if there are no errors from validation
        for err_msg in form.errors.values():
            flash(f'There was an error while creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():  # this runs 2 functions behind the scenes when validating
        possible_user = User.query.filter_by(username=form.username.data).first()  # filters user by provided username
        if possible_user and possible_user.check_password_correction(attempted_password=form.password.data):
            login_user(possible_user)
            flash(f'You have been successfully logged in as: {possible_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Wrong credentials! Please try again', category='danger')
    return render_template('login.html', form=form)
