from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "age",
    )


admin.site.register(Student, StudentAdmin)
