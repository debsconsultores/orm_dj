from django.db import models

# Create your models here.

from app1.models import ModeloAuditoria

class Question(ModeloAuditoria):
    question_text = models.CharField(max_length=200)


class Choice(ModeloAuditoria):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
