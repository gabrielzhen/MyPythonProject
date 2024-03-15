#路由模块
from app import app,db
from flask import render_template,flash,redirect,request,url_for,g 
from app.forms import LoginForm,RegistrationForm,EditProfileForm,EmptyForm,PostForm,ResetPasswordRequestForm,ResetPasswordForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,Post
import sqlalchemy as sa
from urllib.parse import urlsplit
from datetime import datetime,timezone
from app.email import send_password_reset_email
from flask_babel import _,get_locale
from langdetect import detect,LangDetectException
from app.translate import translate

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen=datetime.now(timezone.utc)
        db.session.commit()
    g.locale=str(get_locale())

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
@login_required
def index():
    # user={'username':'Miguei'}
    form=PostForm()
    if form.validate_on_submit():
        flash(_('your post is now live!'))
        try:
            language=detect(form.post.data)
        except LangDetectException:
            language=''
        post=Post(body=form.post.data,author=current_user,language=language)
        db.session.add(post)
        db.session.commit()
    page=request.args.get('page',1,type=int)
    posts=db.paginate(current_user.following_posts(),page=page,
                      per_page=app.config['POSTS_PER_PAGE'],error_out=False)
    next_url=url_for('index',page=posts.next_num) if posts.has_next else None
    prev_url=url_for('index',page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html',title='Home',form=form,posts=posts.items,
                           next_url=next_url,prev_url=prev_url)

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
            flash(_('Invalid username or password'))
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
        flash(_('congratulations,ztj already become a god'))     
        return redirect('/login')
    return render_template('register.html',title='Sign Up',form=form)
 
@app.route('/user/<username>')
def user(username):
    user=db.first_or_404(sa.select(User).where(User.username==username))
    page=request.args.get('page',1,type=int)
    query=user.posts.select().order_by(Post.timestamp.desc())
    posts=db.paginate(query,page=page,
                      per_page=app.config['POSTS_PER_PAGE'],error_out=False)
    next_url=url_for('user',username=user.username,page=posts.next_num) if posts.has_next else None
    prev_url=url_for('user',username=user.username,page=posts.prev_num) if posts.has_prev else None
    form=EmptyForm()
    return render_template('user.html',user=user,posts=posts.items,form=form,
                           next_url=next_url,prev_url=prev_url)

@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form=EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.about_me=form.about_me.data
        db.session.commit()
        flash(_('edit secced'))
        return redirect('/edit_profile')
    elif request.method=='GET':
        form.username.data=current_user.username
        form.about_me.data=current_user.about_me
    return render_template('edit_profile.html',title='Edit Profile',form=form)

@app.route('/follow/<username>',methods=['POST'])
@login_required
def follow(username):
    form=EmptyForm()
    if form.validate_on_submit():
        user=db.session.scalar(sa.select(User).where(User.username==username))
        if user is None:
            flash(_('User%{username} not found!',username=username))
            return redirect('/index')
        if user==current_user:
            flash('You cannot follow yourself')
            return redirect(url_for('user',username=username))
        current_user.follow(user)
        db.session.commit()
        flash(_('you are now following %{username}',username=username))
        return redirect(url_for('user',username=username))
    else:
        return redirect('/index')


@app.route('/unfollow/<username>',methods=['POST'])
@login_required
def unfollow(username):
    form=EmptyForm()
    if form.validate_on_submit():
        user=db.session.scalar(sa.select(User).where(User.username==username))
        if user is None:
            flash(_('User %{username} not found!',username=username))
            return redirect('/index')
        if user==current_user:
            flash(_('You cannot unfollow yourself'))
            return redirect(url_for('user',username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash(_('you are now not following %{username}'))
        return redirect(url_for('user',username=username))
    else:
        return redirect('/index')

@app.route('/explore')
@login_required
def explore():
    page=request.args.get('page',1,type=int)
    query=sa.select(Post).order_by(Post.timestamp.desc())
    posts=db.paginate(query,page=page,per_page=app.config['POSTS_PER_PAGE'],error_out=False)
    next_url=url_for('explore',page=posts.next_num) if posts.has_next else None
    prev_url=url_for('explore',page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html',titile='Explore',posts=posts.items,
                           next_url=next_url,prev_url=prev_url)

@app.route('/reset_password_request',methods=['GET','POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect('/index')
    form=ResetPasswordRequestForm()
    if form.validate_on_submit():
        user=db.session.scalar(
            sa.select(User).where(User.email==form.email.data)
        )
        if user:
            send_password_reset_email(user)
            flash(_('email send please check it !'))
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',title='Reset Password',form=form)

@app.route('/reset_password/<token>',methods=['GET','POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect('/index')
    user=User.verify_reset_password_token(token)
    if not user:
        return redirect('index')
    form=ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_('Your password has been reset'))
        return redirect('/login')
    return render_template('reset_password.html',form=form)

@app.route('/translate',methods=['POST'])
def translate_text():
    data=request.get_json()
    return {'text':translate(data['text'])}