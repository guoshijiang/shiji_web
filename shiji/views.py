#encoding=utf-8

import datetime
import logging
from collections import defaultdict
from decimal import Decimal
from django import http
from django.conf import settings
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from shiji.models import Comment, News


def index(request):
    comment_list = Comment.objects.filter(is_del='NO').order_by("-id")[:3]
    return render(request, 'front/index.html', locals())


def product(request):
    return render(request, 'front/product.html', locals())


def dynamic(request):
    news_list = News.objects.filter(is_del='NO').order_by("-id")[:4]
    return render(request, 'front/dynamic.html', locals())


def news(request):
    news_list = News.objects.filter(is_del='NO').order_by("-id")
    return render(request, 'front/news.html', locals())


def comment(request):
    comment_list = Comment.objects.filter(is_del='NO').order_by("-id")
    return render(request, 'front/comment.html', locals())


def about(request):
    return render(request, 'front/about.html', locals())


def news_detail(request, id):
    news_detail= News.objects.get(id=id)
    return render(request, 'front/news_detail.html', locals())





