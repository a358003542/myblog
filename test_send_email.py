#!/usr/bin/env python
# -*-coding:utf-8-*-


from flask_mail import Message
from hello import mail, app

msg = Message('test', sender='a358003542@qq.com', recipients=['a358003542@qq.com'])

msg.body = 'body'
msg.html = 'html'


with app.app_context():
    mail.send(msg)