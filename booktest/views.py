from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 1 定义视图函数,必须要一个参数request，HttpRequest对象
"""视图函数必须有一个参数request，进行处理之后，需要返回一个HttpResponse的类对象"""


# http://127.0.0.1:8000/index
def index(request):
    # 进行处理 和M和T交互
    # 处理后给浏览器一个应答
    pass
    return HttpResponse("返回没毛病,视图和index的链接已经建立！")


# 2 进行url配置 > 建立url地址和视图的对应关系

# http://127.0.0.1:8000/index2
def index2(request):
    return HttpResponse("hello world, hello python web, hello Django")
