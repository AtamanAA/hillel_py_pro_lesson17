from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_students, name="all_students"),
    path("create/", views.create_student, name="create_student"),
    path("<int:student_id>/", views.edit_student, name="edit_student"),
]
