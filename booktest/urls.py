from django.conf.urls import url
from booktest import views

# 应用的urls.py 格式和test1/urls.py一样
# 列表添加配置项 index, index2
# 在应用中的urls文件进行url配置的时候要严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项，从上到下
    url(r'^index$', views.index),  # 建立视图和index 之间的联系
    # 每一个配置项都会调用url函数，第一个参数是正则表达式，第二个参数是对应的处理操作，可以写一个视图的名字
    url(r'^index2/$', views.index2),  # 建立视图和index2之间的联系
    url(r'^books$', views.show_books),  # 显示图书信息
    # url(r'^book/\d+', views.detail),
    url(r'^books/(\d+)$', views.detail),   # 显示英雄信息
    # 把某部分变成组，Django调用对应视图时会把组里的内容作为参数传递给视图
   ]
"""配置成功之后，去除匹配的a字符，那剩下的index字符串继续到应用的urls文件中进行正则匹配，
，index视图函数返回内容hello python给浏览器来显示。"""
