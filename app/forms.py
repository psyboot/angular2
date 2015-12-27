from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(Form):
    userlogin = StringField('login', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    name = StringField('name', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    number = StringField('number', validators=[DataRequired()])
    sea = BooleanField('sea', default=False)
    remember_me = BooleanField('remember_me', default=False)


