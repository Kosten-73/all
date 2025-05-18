### models.py (в testapp)
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Question(models.Model):
    text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def is_correct(self):
        return self.answer.strip().lower() == self.question.correct_answer.strip().lower()
