from django.db import models


class Student(models.Model):
    id_of_student = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")
    course = models.ManyToManyField('course.Course', null=True)

    def __str__(self):
        return self.name
