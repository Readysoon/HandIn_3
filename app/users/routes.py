from flask import Blueprint, render_template, request, url_for, redirect
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

blueprint = Blueprint('users', __name__)

@blueprint.get('/register')
def get_register():
    return render_template('users/register.html')

@blueprint.post('/register')
def post_register():
    try:  
        if request.form.get('password') != request.form.get('password_confirmation'):
            return render_template('users/register.html', error='The password confirmation must match the password. ')
        elif User.query.filter_by(email=request.form.get('email')).first():
            return render_template('users/register.html', error='The email address is already registered.')
        
        user = User(
            email=request.form.get('email'),
            password=generate_password_hash(request.form.get('password'))
        )
        user.save()

        login_user(user)
        return redirect(url_for('planets.planets'))
    except Exception as error_message:
        error = error_message or 'An error occured while creating an user. Please make sure to enter valid data.'
        return render_template('user/register.html', error=error)

@blueprint.get('/login')
def get_login():
    return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(email=request.form.get('email')).first()

        if not user:
            raise Exception('No user with the given email address was found.')
        elif not check_password_hash(user.password, request.form.get('password')):
            raise Exception('The password does not appear to be correct.')
        
        login_user(user)
        return redirect(url_for('planets.planets'))
    
    except Exception as error_message:
        error = error_message or 'An error occured while logging in. Please verify your email and password'
        return render_template('users/login.html', error=error)

@blueprint.get('/logout')
def logout():
    login_user()

    return redirect(url_for('users.get_login'))