from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# 后台管理相关文件
# Register your models here.

# 自定义模型管理类

# 注册模型类
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
