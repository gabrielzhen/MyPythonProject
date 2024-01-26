from app import app,db
from flask import render_template,flash,redirect,request
from app.forms import LoginForm,RegistrationForm,EditProfileForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User
import sqlalchemy as sa
from urllib.parse import urlsplit
from datetime import datetime,timezone

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen=datetime.now(timezone.utc)
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
def index():
    # user={'username':'Miguei'}
    posts=[
        {'author':{'username':'John'},
         'body':'beautiful day in portland'},
        {'author':{'username':'susan'},
         'body':'the avengers movie was so cool'}
    ]
    return render_template('index.html',title='Home',posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form=LoginForm()
    if form.validate_on_submit():
        user=db.session.scalar(
            sa.select(User).where(User.username==form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user,remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or urlsplit(next_page).netloc!='':
            next_page=('/index')
        return redirect(next_page)
    return render_template('login.html',title='Sign In',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('congratulations,ztj already become a god')     
        return redirect('/login')
    return render_template('register.html',title='Sign Up',form=form)
 
@app.route('/user/<username>')
def user(username):
    user=db.first_or_404(sa.select(User).where(User.username==username))
    posts=[
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',user=user,posts=posts)

@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form=EditProfileForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.about_me=form.about_me.data
        db.session.commit()
        flash('edit secced')
        return redirect('/edit_profile')
    elif request.method=='GET':
        form.username.data=current_user.username
        form.about_me.data=current_user.about_me
    return render_template('edit_profile.html',title='Edit Profile',form=form)