#表单注册模块
from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from app import db
from app.models import User
from flask_babel import lazy_gettext as _l
import sqlalchemy as sa

class LoginForm(FlaskForm):
    username=StringField(_l('Username'),validators=[DataRequired()])
    password=PasswordField(_l('Password'),validators=[DataRequired()])
    remember_me=BooleanField(_l('Remember Me'))
    submit=SubmitField(_l('Sign In'))
    
class RegistrationForm(FlaskForm):
    username=StringField(_l('Username'),validators=[DataRequired()])
    email=StringField(_l('Email'),validators=[DataRequired(),Email()])
    password=PasswordField(_l('Password'),validators=[DataRequired()])
    password2=PasswordField(_l('Repeat Password'),validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(_l('Sign Up'))

    def validate_username(self,username):
        user=db.session.scalar(sa.select(User).where(
            User.username==username.data))
        if user is not None:
            raise ValidationError(_l('Please use a diffrent username.'))
    
    def validata_email(self,email):
        email=db.session.scalar(sa.select(email).where(
            User.email==email.data))
        if email is not None:
            raise ValidationError(_l('Please use a diffrent email.'))
        
class EditProfileForm(FlaskForm):
    username=StringField(_l('Username'),validators=[DataRequired()])
    about_me=TextAreaField(_l('About me'),validators=[Length(min=0,max=140)])
    submit=SubmitField(_l('Submit'))

    def __init__(self, original_username,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username=original_username

    def validate_username(self,username):
        if username.data != self.original_username:
            user=db.session.scalar(sa.select(User).where(User.username==self.username.data))
            if user is not None:
                raise ValidationError(_l('please use a different username'))
    
class EmptyForm(FlaskForm):
    submit=SubmitField(_l('Submit'))

class PostForm(FlaskForm):
    post=TextAreaField(_l('say something!'),validators=[
        DataRequired(),Length(min=1,max=140)
    ])
    submit=SubmitField(_l('Submit'))

class ResetPasswordRequestForm(FlaskForm):
    email=StringField(_l('Email'),validators=[DataRequired(),Email()])
    submit=SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password=PasswordField(_l('Password'),validators=[DataRequired()])
    password2=PasswordField(_l('Repeat Password'),validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(_l('Request Password Reset'))