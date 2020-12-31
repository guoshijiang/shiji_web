from django.contrib import admin
from shiji.models import (
   Category, News, Comment, OnlineMsg
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index', 'is_del')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'excerpt', 'is_del')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'position', 'is_del')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(OnlineMsg)
class OnlineMsgAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'weichat')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')
