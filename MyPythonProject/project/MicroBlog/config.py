# 配置文件
import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard code'
    SQLALCHEMY_DATABASE_URI=os.environ.get('database_url') or \
    'sqlite:///'+os.path.join(basedir,'app.db')