"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# 项目的urls文件
# index
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  # 一个配置项
    url(r'^', include('booktest.urls')),  # 也可以是包含booktest应用中的urls文件
]
"""配置成功之后，去除匹配的a字符，那剩下的index字符串继续到应用的urls文件中进行正则匹配，
匹配成功之后执行视图函数index，index视图函数返回内容hello python给浏览器来显示。"""
"""url配置的目的是让建立url和视图函数的对应关系。
url配置项定义在urlpatterns的列表中，每一个配置项都调用url函数。
url函数有两个参数，第一个参数是一个正则表达式，第二个是对应的处理动作。"""