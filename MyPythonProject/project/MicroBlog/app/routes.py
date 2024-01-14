from app import app
from flask import render_template,flash,redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'username':'Miguei'}
    posts=[
        {'author':{'username':'John'},
         'body':'beautiful day in portland'},
        {'author':{'username':'susan'},
         'body':'the avengers movie was so cool'}
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested from user{} ,remember_me={}'.format(form.username.data,form.password.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form)
