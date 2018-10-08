# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class StartForm(FlaskForm):
    days_to_parse = StringField('Введите количество дней для парсинга', validators=[Length(min=1, max=3)])
    parsing = BooleanField('только парсинг')
    buh = BooleanField('только бухгалтерия')
    parsing_buh = BooleanField('и то и другое')

