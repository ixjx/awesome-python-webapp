#!/usr/bin/python
# -*- coding: utf-8 -*-

#urls.py
from transwarp.web import get,post,view,ctx,interceptor,seeother,notfound
from models import User, Blog, Comment

@view('blogs.html')
@get('/')
def index():
	blogs=Blog.find_all()
	user=User.find_first('where email=?','admin@example.com')
	return dict(blogs=blogs,user=user)
