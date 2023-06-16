from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class FaultModel(models.Model):
    class Meta:
        db_table = 'fault_msg'
        ordering = ('-created_at',)

    title = models.CharField(max_length=250, validators=[
        V.RegexValidator(RegEx.FAULT_TITLE.pattern, RegEx.FAULT_TITLE.msg)])
    body = models.TextField()
    problem_solving = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FaultCommentModel(models.Model):
    class Meta:
        db_table = 'fault_comment'
        ordering = ('-created_at',)

    comment_body = models.TextField()
    fault_msg = models.ForeignKey(FaultModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fault_msg
