from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from watchlist import app, db
from watchlist.models import User, Movie
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        if not current_user.is_authenticated:  # 如果当前用户未认证
            return redirect(url_for('index'))  # 重定向到主页
        title=request.form.get('title')
        year=request.form.get('year')
        movie=Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
        flash('1')
        return redirect(url_for('index'))
    movies=Movie.query.all()
    return render_template('index.html',movies=movies)

@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method=='POST':
        title=request.form.get('title')
        year=request.form.get('year')
        movie.title=title
        movie.year=year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))
    return render_template('edit.html', movie=movie)

@app.route('/movie/delete/<int:movie_id>', methods=['POST'])  # 限定只接受 POST 请求
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)  # 获取电影记录
    db.session.delete(movie)  # 删除对应的记录
    db.session.commit()  # 提交数据库会话
    flash('Item deleted.')
    return redirect(url_for('index'))  # 重定向回主页

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')

        if not username or not password:
            flash('input username or password')
            return redirect(url_for('login'))
        user=User.query.first()
        if username==user.username and user.validate_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('error username or password')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()  # 登出用户
    flash('Goodbye.')
    return redirect(url_for('index'))  # 重定向回首页

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('settings'))

        current_user.name = name
        # current_user 会返回当前登录用户的数据库记录对象
        # 等同于下面的用法
        # user = User.query.first()
        # user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))

    return render_template('settings.html')

