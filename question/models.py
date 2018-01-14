from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=150)
    exam = models.ForeignKey('exam.Exam', on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def __repr__(self):
        return self.question
