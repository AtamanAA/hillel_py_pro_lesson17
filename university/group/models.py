from django.db import models

from student.models import Student
from teacher.models import Teacher


class Group(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='group', blank=True)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
