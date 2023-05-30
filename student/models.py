from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)])
    phone = models.CharField(max_length=20, null=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
