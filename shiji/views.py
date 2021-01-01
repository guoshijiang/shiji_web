#encoding=utf-8

import json
from django.shortcuts import render, redirect
from shiji.models import Comment, News, OnlineMsg
from django.views.decorators.csrf import csrf_exempt
from shiji.form import OnlineMsgForm
from common.helpers import ok_json

def index(request):
    nav_mark = 'index'
    comment_list = Comment.objects.filter(is_del='NO').order_by("-id")[:3]
    return render(request, 'front/index.html', locals())


def product(request):
    nav_mark = 'product'
    return render(request, 'front/product.html', locals())


def dynamic(request):
    nav_mark = 'dynamic'
    news_list = News.objects.filter(is_del='NO').order_by("-id")[:4]
    return render(request, 'front/dynamic.html', locals())


def news(request):
    nav_mark = 'dynamic'
    news_list = News.objects.filter(is_del='NO').order_by("-id")
    return render(request, 'front/news.html', locals())


def comment(request):
    nav_mark = 'index'
    comment_list = Comment.objects.filter(is_del='NO').order_by("-id")
    return render(request, 'front/comment.html', locals())


def about(request):
    nav_mark = 'about'
    return render(request, 'front/about.html', locals())


def news_detail(request, id):
    nav_mark = 'dynamic'
    news_detail= News.objects.get(id=id)
    return render(request, 'front/news_detail.html', locals())


def online_msg(request):
    user_name = request.GET.get('user_name', "")
    phone = request.GET.get('phone', "")
    weichat = request.GET.get('weichat', "")
    email = request.GET.get('email', "")
    describe = request.GET.get('describe', "")
    OnlineMsg.objects.create(
        name=user_name,
        phone=phone,
        email=email,
        weichat=weichat,
        content=describe,
        is_handle="No",
        is_del="No",
    )
    return ok_json(None)

