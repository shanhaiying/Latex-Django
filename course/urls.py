from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    path('add', views.add_course, name="add_course"),
    path('<int:course_id>/edit', views.edit_course, name="edit_course"),
    path('<int:course_id>/delete',
         views.delete_course, name="delete_course"),
]
