from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class NewsModel(models.Model):
    class Meta:
        db_table = 'news_list'
        ordering = ('-created_at',)

    title = models.CharField(max_length=250,
                             validators=[V.RegexValidator(RegEx.NEWS_TITLE.pattern, RegEx.NEWS_TITLE.msg)])
    body = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentsModel(models.Model):
    class Meta:
        db_table = 'news_comments'
        ordering = ('-created_at',)

    comment_body = models.TextField()
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
