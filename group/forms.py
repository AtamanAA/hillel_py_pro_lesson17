from django.forms import (
    ModelForm,
    ModelMultipleChoiceField,
    CheckboxSelectMultiple,
    ModelChoiceField,
    SelectMultiple,
    Select,
)
from django import forms

from .models import Group
from student.models import Student


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name", "teacher", "students"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "teacher": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "students": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class StudentToGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["group", "students"]

    group = ModelChoiceField(
        queryset=Group.objects.all().order_by("name"),
        widget=Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    students = ModelMultipleChoiceField(
        queryset=Student.objects.all().order_by("first_name"),
        widget=SelectMultiple(
            attrs={
                "class": "form-select",
            }
        ),
        required=False,
    )
