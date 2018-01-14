from django.urls import path

from . import views

app_name = 'question'
urlpatterns = [
    path('<int:exam_id>/addquestion', views.add_question,
         name="add_question"),
    path('<int:exam_id>/<int:question_id>/delete_question',
         views.delete_question, name="delete_question"),
    path('<int:exam_id>/<int:question_id>/edit_question',
         views.edit_question, name="edit_question"),
]
