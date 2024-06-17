#包初始化操作
from flask import Flask,request
from flask_babel import Babel
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler
from flask_mail import Mail
from flask_moment import Moment
from elasticsearch import Elasticsearch

def get_local():
    #return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'en'
#创建实例app db migrate login等
app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
mail=Mail(app)
login=LoginManager(app)
login.login_view='login'
moment=Moment(app)
babel=Babel(app,locale_selector=get_local)
app.elasticsearch=Elasticsearch([app.config['ELASTICSEARCH_URL']])

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth=None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth=(app.config['MAIL_USERNAME'],app.config['MAIL_PASSWORD'])
        secure=None
        if app.config['MAIL_USE_TLS']:
            secure=()
        mail_handler=SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'],app.config['MAIL_PORT']),
            fromaddr='no-reply@'+app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],
            subject='Microblog Error Log',
            credentials=auth,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

# 创建应用实例后 注册后面的这些模块
from app import routes,models,errors
