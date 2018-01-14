from django.db import models


class Answer(models.Model):
    answer = models.CharField(max_length=50)
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE)
