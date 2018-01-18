# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from tweets.models import Tweet
from user_profile.models import User
'''
def index(request):
    if request.method == 'GET':
        return HttpResponse('I am called from get request')
    elif request.method == 'POST':
        return HttpResponse('I am called from a post request')
'''

class Index(View):
    def get(self,request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
    def post(self, request):
        return HttpResponse('I am called from a post request')

class Profile(View):
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter()
        params["tweets"] = tweets
        params["users"] = user
        return render(request, 'profile.html', params)
