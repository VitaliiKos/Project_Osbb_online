from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class PollModel(models.Model):
    class Meta:
        db_table = 'poll'
        ordering = ('created_at',)

    question = models.CharField(max_length=150
                                , validators=[
            V.RegexValidator(RegEx.POLL_QUESTION.pattern, RegEx.POLL_QUESTION.msg)]
                                )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class ChoiceModel(models.Model):
    class Meta:
        db_table = 'choice'
        ordering = ('id',)

    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=150)

    def __str__(self):
        return self.choice_text


class VoteModel(models.Model):
    class Meta:
        db_table = 'vote'
        ordering = ('id',)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE)
    choice = models.ForeignKey(ChoiceModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
