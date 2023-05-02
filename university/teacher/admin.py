from django.contrib import admin

from .models import Teacher, Subject


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "patronymic",
        "birthday",
        "subject",
    )


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
