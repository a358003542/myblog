#!/usr/bin/env python
# -*-coding:utf-8-*-


from myblog import Role, User, db

admin_role = Role(name='Admin')

mod_role = Role(name='Moderator')

user_role = Role(name='User')

user_john = User(username='john', role=admin_role)

user_susan = User(username='susan', role=user_role)

user_david = User(username='david', role=user_role)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_david)
db.session.add(user_john)
db.session.add(user_susan)

db.session.commit()

admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()

db.session.delete(mod_role)
db.session.commit()
