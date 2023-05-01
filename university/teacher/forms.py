from django.forms import ModelForm
from .models import Teacher, Subject


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "patronymic", "birthday", "subject", ]


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["name", ]
