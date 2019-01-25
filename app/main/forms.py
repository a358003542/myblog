#!/usr/bin/env python
# -*-coding:utf-8-*-


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




class NameForm(FlaskForm):
    name = StringField('请输入您的名字？', validators=[DataRequired()])
    submit = SubmitField('提交')