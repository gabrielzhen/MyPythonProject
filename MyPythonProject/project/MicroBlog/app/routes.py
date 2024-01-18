from app import app,db
from flask import render_template,flash,redirect,request
from app.forms import LoginForm,RegistrationForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User
import sqlalchemy as sa
from urllib.parse import urlsplit

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

@app.route('/register',method=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form=RegistrationForm()
    
    