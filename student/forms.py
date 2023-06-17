from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.core.exceptions import ValidationError
from django import forms
import phonenumbers

from .models import Student
from group.models import Group


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "age",
            "phone",
            "photo",
            "group",
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
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "photo": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    group = ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=CheckboxSelectMultiple(
            attrs={
                "class": "form-check form-check-inline",
            }
        ),
        required=False,
    )

    def clean_phone(self):
        phone_raw = self.cleaned_data["phone"]
        try:
            phone = phonenumbers.parse(phone_raw, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Phone isn't valid!")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone isn't valid!")
        return phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
