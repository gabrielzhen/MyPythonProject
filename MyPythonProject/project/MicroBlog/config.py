# 配置文件
import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard code'
    SQLALCHEMY_DATABASE_URI=os.environ.get('database_url') or \
    'sqlite:///'+os.path.join(basedir,'app.db')

    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_PORT=int(os.environ.get('MAIL_PORT') or '25')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    ADMINS=['ggshop326@gmail.com']