from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

from booktest.models import BookInfo  # 导入图书模型类

# Create your views here.
# 1 定义视图函数,必须要一个参数request，HttpRequest对象
"""视图函数必须有一个参数request，进行处理之后，需要返回一个HttpResponse的类对象"""


def my_render(request, template_path, context_dict):
    # 封装函数  多余的
    # 使用模板文件
    # a)加载模板文件:  去模板目录下面获取html文件的内容，得到一个模板对象。
    temp = loader.get_template(template_path)  # loader 方法的返回值是一歌模板对象
    # b)定义模板上下文:  向模板文件传递数据。
    context = RequestContext(request, context_dict)
    # c)模板渲染:   把使用的变量和语句替换掉，得到一个标准的html内容。"""
    res_html = temp.render(context)  # 传过来模板上下文，返回替换后的内容
    # d) 返回给浏览器
    return HttpResponse(res_html)


# http://127.0.0.1:8000/index
def index(request):
    # 进行处理 和M和T交互
    # 处理后给浏览器一个应答
    pass
    # return HttpResponse("返回没毛病,视图和index的链接已经建立！")
    #
    # # 使用模板文件
    # # a)加载模板文件:  去模板目录下面获取html文件的内容，得到一个模板对象。
    # temp = loader.get_template('booktest/index.html')  # loader 方法的返回值是一歌模板对象
    # # b)定义模板上下文:  向模板文件传递数据。
    # context = RequestContext(request, {})
    # # c)模板渲染:   把使用的变量和语句替换掉，得到一个标准的html内容。"""
    # res_html = temp.render(context)  # 传过来模板上下文，返回替换后的内容
    # # d) 返回给浏览器
    # return HttpResponse(res_html)

    # 使用自定义函数 my_render()
    return my_render(request, 'booktest/index.html', {'content': 'hello python web', 'list': list(range(1, 10))})
    # return render(request, 'booktest/index.html', {'content': 'hello python web'})


# 2 进行url配置 > 建立url地址和视图的对应关系

# http://127.0.0.1:8000/index2
def index2(request):
    return HttpResponse("hello world, hello python web, hello Django")


# render方法已经封装好了
def index666(request):
    return render(request, 'booktest/index.html', {'content': 'hello python web'})


""" """


def show_books(request):
    '''显示图书的信息'''
    # 1 通过M查找图书信息
    books = BookInfo.objects.all()
    # 2 使用模板
    return render(request, 'booktest/show_books.html', {'books': books})
    #


def detail(request, bid):
    '''查询图书关联的信息'''
    # 1 根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)  # 接返回值book包含查询的结果

    # 2 查询和book关联的英雄信息
    heros = book.heroinfo_set.all()

    # 3 使用模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})
