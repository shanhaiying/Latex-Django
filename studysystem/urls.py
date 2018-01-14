from django.urls import path

from . import views

app_name = 'study'
urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('student/add', views.add_student, name="add_student"),
    path('student/get_students', views.get_students, name="get_students"),
    path('student/get_student/<int:student_id>', views.get_student, name="get_student"),

    path('generate/<int:exam_id>/', views.generate_page,
         name="generate_page"),
]
