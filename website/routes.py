from website import app
from flask import render_template, request, url_for, redirect, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, HiddenField
from wtforms.validators import InputRequired

class Login_form(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Submit')

class Register_form(FlaskForm):
    email = EmailField('E-Mail', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Submit')

class Twofactor_form(FlaskForm):
    twofactorcode = StringField('twofactorcode', validators=[InputRequired()])
    id = HiddenField('ID', validators=[InputRequired()])
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
    return render_template('home.html')

@app.route('/sharetop')
def sharetop():
    print("loading sharetop page")
    start_form = Sharetop_start_form()
    stop_form = Sharetop_stop_form()
    download_form = Sharetop_download_form()
    # TODO content
    return render_template('sharetop.html', start_form=start_form, stop_form=stop_form, download_form=download_form)

@app.route('/guacamole')
def guacamole():
    print("loading guacamole page")
    return render_template('guacamole.html')

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = Register_form()
    # TODO content
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    print("loading login page")
    form = Login_form()
    # TODO content
    return render_template('login.html', form=form)

@app.route("/logout")
def session_logout():
    # TODO content
    print("loading logout page")
    return redirect(url_for('login'))

@app.route("/profile")
def profile():
    print("loading profile page")
    # TODO content
    return render_template('profile.html')

