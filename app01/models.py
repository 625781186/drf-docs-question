# coding=utf-8
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


## {全景项目作品表 -- 有数据}
class UWorksmain(models.Model):
    pk_works_main = models.AutoField(verbose_name = '项目id', help_text = '项目id',
        primary_key = True
    )

    name = models.CharField(verbose_name = '全景项目名称', help_text = '全景项目名称',
        max_length = 30)
    profile = models.TextField(verbose_name = '场景简介', help_text = '场景简介',
        blank = True, null = True
    )
    thumb_path = models.CharField(verbose_name = '略缩图', help_text = '略缩图',
        default = '',
        max_length = 255
    )
    view_uuid = models.CharField(verbose_name = '图纸编码', help_text = '图纸编码',
        default = '',
        max_length = 16
    )
    photo_date = models.DateTimeField(verbose_name = '拍摄时间', help_text = '拍摄时间',
        default = datetime.now,
    )
    privacy_flag = models.IntegerField(verbose_name = '允许公开浏览', help_text = '允许公开浏览',
        default = True,
    )
    privacy_password = models.CharField(verbose_name = '私有密码', help_text = '私有密码',
        blank = True, null = True,
        max_length = 32,
    )

    cdn_host = models.CharField(verbose_name = 'cdn服务器域名', help_text = 'cdn服务器域名',
        default = 'baidu.com',
        max_length = 100)

    ## ------------------------------

    hidelogo_flag = models.IntegerField(verbose_name = 'logo隐藏', help_text = 'logo隐藏',
        default = True,
    )
    hideuser_flag = models.IntegerField(verbose_name = '作者隐藏', help_text = '作者隐藏',
        default = True,
    )
    flag_publish = models.IntegerField(verbose_name = '是否发布作品', help_text = '是否发布作品',
        default = True,
    )
    browsing_num = models.IntegerField(verbose_name = '浏览量', help_text = '浏览量',
        default = True,
    )
    praised_num = models.IntegerField(verbose_name = '点赞量', help_text = '点赞量',
        default = 100,
    )
    hideshare_flag = models.IntegerField(verbose_name = '隐藏分享', help_text = '隐藏分享',
        default = True,
    )
    hidevrglasses_flag = models.IntegerField(verbose_name = '隐藏vr眼镜', help_text = '隐藏vr眼镜',
        default = True,
    )
    hideviewnum_flag = models.PositiveIntegerField(verbose_name = '隐藏人气', help_text = '隐藏人气',
        default = True,
    )

    sort = models.SmallIntegerField(verbose_name = '管理员定义的排序', help_text = '管理员定义的排序',
        default = 999,
    )
    user_sort = models.SmallIntegerField(verbose_name = '用户自定义显示排序', help_text = '用户自定义显示排序',
        default = 999,
    )

    hideprofile_flag = models.IntegerField(verbose_name = '是否显示简介', help_text = '是否显示简介',
        default = True,
    )
    hidepraise_flag = models.IntegerField(verbose_name = '是否允许点赞', help_text = '是否允许点赞',
        default = True,
    )
    flag_allowed_recomm = models.IntegerField(verbose_name = '是否允许推荐', help_text = '是否允许推荐',
        default = True,
    )
    recommend = models.IntegerField(verbose_name = '是否推荐', help_text = '是否推荐',
        default = True,
    )
    user_recommend = models.IntegerField(verbose_name = '用户自定义是否允许管理员推荐', help_text = '用户自定义是否允许管理员推荐',
        default = True,
    )
    # category            = models.PositiveIntegerField()
    create_time = models.DateTimeField(verbose_name = '创建时间', help_text = '创建时间',
        default = datetime.now,
    )

    class Meta:
        ##managed = False
        db_table = 'u_worksmain'
