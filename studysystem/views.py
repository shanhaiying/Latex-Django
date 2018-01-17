import subprocess
import os
import re
import pyqrcode

from django.views.static import serve
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.views.generic import CreateView
from exam.models import Exam
from course.models import Course
from studysystem.models import Student

from latex2.settings import BASE_DIR

# Create your views here.


def home_page(request):
    c = Course.objects.all()
    context = {"courses": c}
    return render(request, 'home.html', context)


def get_students(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "get_students.html", context)


def get_student(request, student_id):
    student = Student.objects.filter(pk=student_id)
    courses = Course.objects.all()
    context = {"student": student, "courses": courses}
    if request.POST:
        number = request.POST.get('number', "error")
        name = request.POST.get('name', "error")
        surname = request.POST.get('surname', "error")
        if not number == "error":
            student = Student.objects.get(pk=student_id)
            student.number = number
            student.name = name
            student.surname = surname
            student.save()
            return redirect("study:get_students")

        else:
            id = request.POST.get('dropdown_courses', "error")
            if not id == "error":
                student = Student.objects.get(pk=student_id)
                course = Course.objects.get(pk=id)
                student.course.add(course)
        return redirect("study:get_student", student_id)
    return render(request, "students/get_student.html", context)


def add_student(request):
    if request.POST:
        number = request.POST.get('number', 'error')
        name = request.POST.get('name', 'error')
        surname = request.POST.get('surname', 'error')

        if not (number or name or surname) == "error":
            Student.objects.create(id_of_student=number,
                                   name=name,
                                   surname=surname)

        return redirect("study:get_students")
    return render(request, "students/add_student.html")


def delete_student(request, student_id):
    Student.objects.filter(pk=student_id).delete()
    return redirect("study:get_students")


def delete_course(request, student_id, course_id):
    student = Student.objects.get(pk=student_id)
    course = Course.objects.get(pk=course_id)
    student.course.remove(course)
    return redirect("study:get_student", student_id)


def generate_page(request, exam_id):
    course = Course.objects.get(exam=exam_id)
    students = Student.objects.filter(course=course)
    context = {"students": students}

    if request.POST:
        student_id = request.POST.get("dropdown_students", "error")
        if not student_id == "error":
            # Just a file to be based on something
            with open('latex_sample.tex') as f:
                file = f.read()
            # Template of answers
            with open('closed_answer_template.txt', 'r') as answer_temp:
                answer_tempalte = answer_temp.read()

            with open('open_answer_template.txt', 'r') as open_answer_template:
                open_answer_template = open_answer_template.read()

            exam = Exam.objects.get(pk=exam_id)
            questions = exam.question_set.all()

            # Create some temporary file and create there questions with
            # answers
            with open('temp.txt', 'w') as f:
                for num, quest in enumerate(questions):
                    num += 1

                    # Writing questions
                    f.write("\n\question {}\n".format(quest))
                    f.write(r"\n")
                    if quest.answer_set.all():
                        # Writing circle answers
                        new_anwers = re.sub(
                            "_Number_", str(num), answer_tempalte)

                        file = re.sub(r"%paste_here_answers", new_anwers, file)

                        f.write(r"\\begin{oneparchoices}")
                        for answer in quest.answer_set.all():
                            f.write("\n\choice {} \n".format(answer.answer))
                        f.write(r"\\end{oneparchoices} %question" + str(num))
                        f.write(r"\n%paste_here_question")
                    else:
                        f.write(r"\n\\begin{solutionorlines}[0.5in]\n" +
                                r"\\end{solutionorlines}")
                        new_anwers = re.sub("_Number_", str(
                            num), open_answer_template)
                        file = re.sub(r"%paste_here_answers", new_anwers, file)

            # Reading that temp file
            with open('temp.txt', 'r') as f:
                tempfile = f.read()

            # Writing to a new file
            file_name = exam.name_of_exam
            filename = file_name + ".tex"
            with open(filename, 'w') as f:
                f.write(re.sub(r'%paste_here_question', tempfile, file))
            student = Student.objects.get(pk=student_id)
            qr = pyqrcode.create(student.id_of_student)
            qr.eps('QRCode.eps')

            cmd = ['pdflatex', '-interaction', 'nonstopmode', filename]
            proc = subprocess.Popen(cmd)
            proc.communicate()
            try:
                os.remove("{}.aux".format(file_name))
                os.remove("{}.log".format(file_name))
                os.remove("{}.tex".format(file_name))
                os.remove("temp.txt")
            except Exception as e:
                pass

            path_to_file = BASE_DIR + "\\" + file_name + ".pdf"
            return serve(request, os.path.basename(path_to_file),
                         os.path.dirname(path_to_file))
            # return redirect('get_exam', exam_id)
    return render(request, 'generate.html', context)
