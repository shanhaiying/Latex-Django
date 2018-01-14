from django.shortcuts import render, redirect
# from django.views.generic import CreateView
from .models import Exam
from course.models import Course


def add_exam(request, course_id):
    if request.POST:
        exam_name = request.POST['input_data']
        course = Course.objects.get(pk=course_id)
        Exam.objects.create(name_of_exam=exam_name, course=course).save()
        return redirect("study:home_page")
    return render(request, 'add.html', {"title": "Add an exam"})


def get_exam(request, exam_id):
    e = Exam.objects.filter(id=exam_id)
    if e:
        context = {"examination": e}
        return render(request, 'get_exam.html', context)
    return redirect('study:home_page')


def edit_exam(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    if request.POST:
        exam.name_of_exam = request.POST['input_data']
        exam.save()
        return redirect('study:home_page')
    context = {"value": exam,
               "title": "Edit exam '{}'".format(exam)}
    return render(request, 'edit.html', context)


def delete_exam(request, exam_id):
    Exam.objects.filter(pk=exam_id).delete()
    return redirect("study:home_page")
