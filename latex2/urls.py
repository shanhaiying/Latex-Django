from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studysystem.urls'), name="home_page"),
    path('course/', include('course.urls'), name="course_page"),
    path('exam/', include('exam.urls'), name="exam_page"),
    path('question/', include('question.urls'), name="question_page"),
    path('answer/', include('answer.urls'), name="answer_page"),
]
