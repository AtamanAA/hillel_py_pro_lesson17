from django.forms import (
    ModelForm,
    ModelMultipleChoiceField,
    CheckboxSelectMultiple,
    ModelChoiceField,
)

from .models import Group
from student.models import Student


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name", "teacher", "students"]


class StudentToGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["group", "students"]

    group = ModelChoiceField(
        queryset=Group.objects.all().order_by("name"),
    )

    students = ModelMultipleChoiceField(
        queryset=Student.objects.all().order_by("first_name"),
        widget=CheckboxSelectMultiple(),
        required=False,
    )
