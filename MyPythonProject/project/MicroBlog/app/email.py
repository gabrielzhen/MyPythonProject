from flask_mail import Message
from app import mail,app
from flask import render_template
from threading import Thread

# 1.新开一个窗口
# aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
# 2.应用服务器设置服务器信息
# export MAIL_SERVER=localhost
# export MAIL_PORT=8025


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject,sender,recipients,text_body,html_body):
    msg=Message(subject,sender=sender,recipients=recipients)
    msg.body=text_body
    msg.html=html_body
    Thread(target=send_async_email,args=(app,msg)).start()

def send_password_reset_email(user):
    token=user.get_reset_password_token()
    send_mail('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',user=user,token=token),
               html_body=render_template('email/reset_password.html',user=user,token=token)
               )