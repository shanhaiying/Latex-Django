from django.urls import path

from . import views

app_name = 'answer'
urlpatterns = [
    path('<int:exam_id>/<int:question_id>/addanswer',
         views.add_answer, name="add_answer"),
    path('<int:exam_id>/<int:answer_id>/delete_answer',
         views.delete_answer, name="delete_answer"),
    path('<int:exam_id>/<int:answer_id>/edit_answer',
         views.edit_answer, name="edit_answer"),
]
