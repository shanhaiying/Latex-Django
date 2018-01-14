from django.db import models


# Create your models here.
class Exam(models.Model):
    name_of_exam = models.CharField(max_length=50)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_exam

    def __repr__(self):
        return self.name_of_exam
