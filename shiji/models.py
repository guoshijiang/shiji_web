#encoding=utf-8

from django.db import models
from common.models import BaseModel
from DjangoUeditor.models import UEditorField


DEL_CHOICES = [(x, x) for x in ['YES', 'NO']]


class Category(BaseModel):
    name = models.CharField(max_length=20, default="", verbose_name=u'分类名称')
    index = models.IntegerField(default=999, verbose_name=u'索引')
    category_mark = models.CharField(max_length=20, default="", verbose_name=u'分类标志')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "分类列表"
        verbose_name_plural = "分类列表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'index': self.index,
            'category_mark': self.category_mark
        }


class News(BaseModel):
    title = models.CharField(max_length=70, verbose_name=u'标题')
    excerpt = models.TextField(max_length=200, blank=True, default="", verbose_name=u'咨询摘要')
    category = models.ForeignKey(Category, related_name='news_category', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name=u'类别')
    img = models.ImageField(upload_to='news_img/%Y/%m/%d/', blank=True, null=True, verbose_name=u'新闻封面')
    body = UEditorField(
        width=800, height=500, toolbars="full", imagePath="img/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True,
        verbose_name=u'新闻内容'
    )
    views = models.PositiveIntegerField(default=0, verbose_name=u'查看次数')
    author = models.CharField(max_length=70, default="知鱼定制", verbose_name=u'作者')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "新闻管理"
        verbose_name_plural = "新闻管理"

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'excerpt': self.excerpt,
            'img': str(self.img),
            'body': self.body,
            'views': self.views,
            'author': self.author,
            'is_del': self.is_del,
            'created_at':self.created_at
        }


class Comment (BaseModel):
    name = models.CharField(max_length=70, default="", verbose_name=u'客户名称')
    photo = models.ImageField(upload_to='cos_logo/%Y/%m/%d/', blank=True, null=True, verbose_name=u'客户头像')
    company = models.CharField(max_length=216, verbose_name=u'客户公司')
    position = models.CharField(max_length=128, verbose_name=u'客户职位')
    star = models.PositiveIntegerField(default=5, verbose_name=u'评论星级')
    content = models.TextField(max_length=500, blank=True, default="", verbose_name=u'评论内容')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "客户评论表"
        verbose_name_plural = "客户评论表"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'photo': str(self.photo),
            'company': self.company,
            'position': self.position,
            'star': self.star,
            'content': self.content,
            'created_at': self.created_at
        }


class OnlineMsg(BaseModel):
    HANDLE_CHOICES = [(x, x) for x in ['YES', 'NO']]
    name = models.CharField(max_length=70, verbose_name=u'姓名')
    phone = models.CharField(max_length=70, verbose_name=u'电话')
    email = models.CharField(max_length=70, verbose_name=u'邮箱')
    weichat = models.CharField(max_length=70, default="guo20123762", verbose_name=u'邮箱')
    content = models.TextField(max_length=500, blank=True, default="", verbose_name=u'留言内容')
    is_handle = models.CharField(max_length=16, choices=HANDLE_CHOICES, default='NO', verbose_name=u'是否处理')
    is_del = models.CharField(max_length=16, choices=DEL_CHOICES, default='NO', verbose_name=u'是否删除')

    class Meta:
        verbose_name = "在线咨询"
        verbose_name_plural = "在线咨询"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'weichat': self.weichat,
            'content': self.content,
            'is_handle': self.is_handle,
            'is_del': self.is_del,
            'created_at': self.created_at
        }
