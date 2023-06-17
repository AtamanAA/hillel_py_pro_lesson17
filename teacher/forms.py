from django.forms import ModelForm, DateInput
from django import forms

from .models import Teacher, Subject


class DateInputCustom(DateInput):
    input_type = "date"


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "patronymic",
            "birthday",
            "subject",
            "photo",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "patronymic": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "birthday": DateInputCustom(
                attrs={
                    "class": "form-control",
                }
            ),
            "subject": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "photo": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = [
            "name",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
