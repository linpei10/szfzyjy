from django.db import models

import django.utils.timezone as timezone


# Create your models here.


class UserInfo(models.Model):
    """
    用户表
    """
    createDate = models.DateTimeField(default=timezone.now)  # 创建日期
    modifyDate = models.DateTimeField(auto_now=True)  # 修改日期
    email = models.EmailField(max_length=64, unique=True)  # 邮箱
    phone = models.CharField(max_length=32, unique=True, null=True)  # 手机号
    password = models.CharField(max_length=32)  # 密码
    company = models.CharField(max_length=32, null=True)  # 公司
    posotion = models.CharField(max_length=32, null=True)  # 职位
    name = models.CharField(max_length=32)  # 姓名
    wechat = models.CharField(max_length=32, null=True)  # 微信


class Permission(models.Model):
    """
     权限表
    """
    pass
