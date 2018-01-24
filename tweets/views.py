# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.views.generic import View
from tweets.models import Tweet, HashTag
from user_profile.models import User
from tweets.forms import TweetForm


class Index(View):

    def get(self,request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)


    def post(self, request):
        return HttpResponse('I am called from a post request')

class Profile(View):

    def get(self, request, username):
        form=TweetForm()
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter()
        params["tweet"] = tweets
        params["user"] = user
        params["form"] = form
        return render(request, 'profile.html', params)



class PostTweet(Profile):

    def post(self,request,username):
        form = TweetForm(request.POST)
        if form.is_valid():
            user=User.objects.get(username=username)
            tweet=Tweet(
                    user=user,
                    text=form.cleaned_data['text'],
                    country=form.cleaned_data['country']
                     )
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)         
        else:
            return HttpResponse(form.response.as_json())
        return HttpResponseRedirect('/user/'+username)


class HashTagCloud(View):
    """Hash tag page rechable from /hashtag/<hashtag> URL"""
    def get(self,request,hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet
        return render(request, 'hashtag.html', params)

