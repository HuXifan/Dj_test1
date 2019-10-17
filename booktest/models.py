from django.db import models


# 设计和表对应的类，模型类
# Create your models here.


# 一类
# 图书类
class BookInfo(models.Model):
    """图书模型类"""
    # id会自动生成
    # CharField 说明是一个字符串，max——length指定字符串最大长度
    btitle = models.CharField(max_length=20)
    # 　DateField() 说明是日期类型
    bpub_date = models.DateField()


# 多类
# 英雄类
class HeroInfo(models.Model):

    # CharField 说明是一个字符串，max——length指定字符串最大长度
    hname = models.CharField(max_length=20)
    # 　DateField() 说明是日期类型
    # hage = models.DateField()
    # BooleanField说明是布尔类型，default指定默认值 False代表男
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性，建立图书类和英雄人物之间的一对多关系
    # 关系属性对应的表的字段名格式：关系属性名_id  hbook_id(外键)
    hbook = models.ForeignKey('BookInfo')



