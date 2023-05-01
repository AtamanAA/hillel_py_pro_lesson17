from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from .models import Student
from group.models import Group


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", "group", ]

    group = ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=CheckboxSelectMultiple(),
        required=False,
    )
