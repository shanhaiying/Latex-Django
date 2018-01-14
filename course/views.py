from django.shortcuts import render, redirect
# from django.views.generic import CreateView
from .models import Course


def add_course(request):
    if request.POST:
        course_name = request.POST['input_data']
        if course_name:
            Course.objects.create(name_of_course=course_name).save()
        return redirect('study:home_page')
    return render(request, 'add.html', {"title": "Add a course"})


def edit_course(request, course_id):
    if request.POST:
        course = Course.objects.get(pk=course_id)
        course.name_of_course = request.POST['input_data']
        course.save()
        return redirect('study:home_page')
    value = Course.objects.get(pk=course_id).name_of_course
    context = {"value": value, "title": "Edit course '{}'".format(value)}
    return render(request, 'edit.html', context)


def delete_course(request, course_id):
    Course.objects.filter(pk=course_id).delete()
    return redirect('study:home_page')
