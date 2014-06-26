#!/usr/bin/env python
# -*- coding: utf-8 -*-

#urls.py
import transwarp.web
import models

@view('test_users.html')
@get('/')
def test_users():
	users=User.find_all()
	return dict(users=users)