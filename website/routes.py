from app import app
from flask import render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
import utility

class Login_form(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Submit')

class Register_form(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Submit')

class Sharetop_start_form(FlaskForm):
    # TODO content
    submit = SubmitField('start')

class Sharetop_stop_form(FlaskForm):
    # TODO content
    submit = SubmitField('stop')

class Sharetop_download_form(FlaskForm):    
    # TODO content
    submit = SubmitField('download')

@app.route('/')
def main():
    print("loading / page")
    return redirect(url_for('home'))

@app.route('/home')
def home():
    print("loading home page")
    return render_template('home.html', current_user=current_user)

@app.route('/sharetop')
@login_required
def sharetop():
    print("loading sharetop page")
    start_form = Sharetop_start_form()
    stop_form = Sharetop_stop_form()
    download_form = Sharetop_download_form()
    # TODO content
    return render_template('sharetop.html', start_form=start_form, stop_form=stop_form, download_form=download_form, current_user=current_user)

@app.route('/guacamole')
def guacamole():
    print("loading guacamole page")
    return redirect("http://localhost:8080/guacamole/#/")

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = Register_form()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        result = utility.register(username=username, password=password)
        
        if result:
            return redirect(url_for('login'))
        flash('registration failed')

    return render_template('register.html', form=form, current_user=current_user)

@app.route('/login', methods=['GET','POST'])
def login():
    print("loading login page")
    form = Login_form()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        result = utility.login(username=username, password=password)
        if result:
            return redirect(url_for('profile'))
        flash('login failed')

    return render_template('login.html', form=form, current_user=current_user)

@app.route("/logout")
@login_required
def session_logout():
    utility.logout()
    print("loading logout page")
    return redirect(url_for('login', current_user=current_user))

@app.route("/profile")
@login_required
def profile():
    print("loading profile page")
    return render_template('profile.html', current_user=current_user)

