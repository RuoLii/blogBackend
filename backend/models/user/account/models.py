from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 删除 Member 记录时， 同时删除 Users 表记录

    #  用户头像字段
    avater = models.URLField(max_length=512, blank=True)
    #  自我介绍字段
    description = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return str(self.user)
