from django.forms import ModelForm, DateInput
from .models import Teacher, Subject


class DateInputCustom(DateInput):
    input_type = "date"


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "patronymic", "birthday", "subject", ]

        widgets = {
            "birthday": DateInputCustom(),
        }


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["name", ]
