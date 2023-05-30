from django.urls import path

from . import views


urlpatterns = [
    path("", views.all_teachers, name="all_teachers"),
    path("create/", views.create_teacher, name="create_teacher"),
    path("<int:teacher_id>/", views.edit_teacher, name="edit_teacher"),
    path("subject", views.all_subjects, name="all_subjects"),
    path("create-subject/", views.create_subject, name="create_subject"),
    path("subject/<int:subject_id>/", views.edit_subject, name="edit_subject"),
]
