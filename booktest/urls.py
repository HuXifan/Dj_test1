from django.conf.urls import url
from booktest import views

# 应用的urls.py 格式和test1/urls.py一样
# 列表添加配置项 index, index2
# 在应用中的urls文件进行url配置的时候要严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项，从上到下
    url(r'^index$', views.index),  # 建立视图和index 之间的联系
    url(r'^index2/$', views.index2),  # 建立视图和index2之间的联系
]
"""配置成功之后，去除匹配的a字符，那剩下的index字符串继续到应用的urls文件中进行正则匹配，
，index视图函数返回内容hello python给浏览器来显示。"""
