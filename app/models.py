from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser 사용
class Users(AbstractUser):
    user_auth = models.CharField(max_length=50)
    hint = models.CharField(max_length=50)


# 작성, 수정 시간을 상속
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Labels(TimeStampedModel):
    label = models.CharField(max_length=100)


class Memos(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    writer = models.ForeignKey(Users, on_delete=models.CASCADE)
    img = models.FileField(upload_to="", blank=True)
    like = models.BigIntegerField(default=0)
    auth = models.CharField(max_length=100, default='open')
    labels = models.ManyToManyField('Labels', related_name='memos', blank=True)

    def clicked(self):
        self.like += 1
        self.save()
        return self


class Chats(TimeStampedModel):
    memo = models.ForeignKey(Memos, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    writer = models.ForeignKey(Users, on_delete=models.CASCADE)
