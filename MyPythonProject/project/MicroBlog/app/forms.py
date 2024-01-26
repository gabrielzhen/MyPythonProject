from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from app import db
from app.models import User
import sqlalchemy as sa

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    password2=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=db.session.scalar(sa.select(User).where(
            User.username==username.data))
        if user is not None:
            raise ValidationError('Please use a diffrent username.')
    
    def validata_email(self,email):
        email=db.session.scalar(sa.select(email).where(
            User.email==email.data))
        if email is not None:
            raise ValidationError('Please use a diffrent email.')
        
class EditProfileForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    about_me=TextAreaField('About me',validators=[Length(min=0,max=140)])
    submit=SubmitField('Submit')
    
