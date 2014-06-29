#!/usr/bin/python
# -*- coding: utf-8 -*-

#urls.py
from transwarp.web import get,post,view,ctx,interceptor,seeother,notfound
from models import User, Blog, Comment
from apis import api, APIError, APIValueError, APIPermissionError, APIResourceNotFoundError
import os, re, time, base64, hashlib, logging

@view('blogs.html')
@get('/')
def index():
	blogs=Blog.find_all()
	user=User.find_first('where email=?','admin@example.com')
	return dict(blogs=blogs,user=user)

@api
@get('/api/users')
def api_get_users():
    users = User.find_by('order by created_at desc')
    for u in users:
        u.password = '******'
    return dict(users=users)
