from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=80)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    birthday = models.DateField()
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(
        upload_to="photo/teachers",
        null=True,
        default="photo/teachers/default_teacher_avatar.jpg",
    )

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
