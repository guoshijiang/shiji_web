#encoding=utf-8

from django import forms
from shiji.models import OnlineMsg


class OnlineMsgForm(forms.ModelForm):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.CharField(required=True)
    weichat = forms.CharField(required=True)
    content = forms.CharField(required=True)

    class Meta:
        model = OnlineMsg
        fields = ['name', 'phone', 'email', 'content']

    def __init__(self, request, *args, **kw):
        self.request = request
        super(OnlineMsgForm, self).__init__(*args, **kw)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name in ['', None]:
            return self.add_error('name', '名字不能为空')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone in ['', None]:
            return self.add_error('name', '手机号码不能为空')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in ['', None]:
            return self.add_error('email', 'email不能为空')
        return email

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content in ['', None]:
            return self.add_error('content', '内容不能为空')
        return content

    def clean_weichat(self):
        weichat = self.cleaned_data.get('weichat')
        if weichat in ['', None]:
            return self.add_error('weichat', '微信不能为空')
        return weichat

    def save(self):
        super(OnlineMsgForm, self).save(commit=True)
