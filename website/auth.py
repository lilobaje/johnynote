from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user




from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth=Blueprint('auth',__name__)#route urls

@auth.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
          email = request.form.get('email')
          
          password = request.form.get('password')

          user = User.query.filter_by(email=email).first()
          if user:
               if check_password_hash(user.password, password):
                    flash('Logged im successfully!', category='successs')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
               else:
                flash('Incorrect password, try again.', category='error')
          else:
               flash('Email does not exist.', category='error')

     return render_template ("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
     if request.method == 'POST':
          email= request.form.get('email')
          username = request.form.get('username')
          password1 = request.form.get('password1')


          user = User.query.filter_by(email=email).first()
          if user:
            flash('Email already exists.', category='error')
          if len(email) < 4:
               flash('Email must be greater than four characters.', category='erro')
          elif len(username) < 4:
               flash('username must be greater than four characters.', category='erro')
          elif len(password1) < 2 :
               flash('password must be greater than two characters.', category='erro')
          else: 
                new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('Account Activated', category='Success')
                return redirect(url_for('views.home'))

          

     return render_template ("signup.html",user=current_user)