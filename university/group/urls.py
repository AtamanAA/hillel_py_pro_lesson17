from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_groups, name="all_groups"),
    path('create/', views.create_group, name="create_group"),
    path('<int:group_id>/', views.edit_group, name="edit_group"),
]