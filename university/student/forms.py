from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.core.exceptions import ValidationError
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
            "group",
        ]

    group = ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=CheckboxSelectMultiple(),
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
        return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
