from django.urls import path

from . import views

app_name = 'exam'

urlpatterns = [
    path('<int:course_id>/exam/add', views.add_exam, name="add_exam"),
    path('<int:exam_id>/', views.get_exam, name="get_exam"),
    path('<int:exam_id>/edit', views.edit_exam, name="edit_exam"),
    path('<int:exam_id>/delete', views.delete_exam, name="delete_exam"),
]
