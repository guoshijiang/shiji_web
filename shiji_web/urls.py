"""shiji_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from shiji.views import (
    index, product, dynamic, about, news,
    comment, news_detail, online_msg
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path(r'product', product, name='product'),
    path(r'dynamic', dynamic, name='dynamic'),
    path(r'news', news, name='news'),
    path(r'comment', comment, name='comment'),
    path(r'<int:id>/news_detail', news_detail, name='news_detail'),
    path(r'about', about, name='about'),
    path(r'online_msg', online_msg, name='online_msg'),
    path('ueditor/', include('DjangoUeditor.urls')),  # 添加DjangoUeditor的URL
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 增加此行
]
