from django.shortcuts import render, redirect
# from django.views.generic import CreateView
from question.models import Question
from exam.models import Exam


def add_question(request, exam_id):
    if request.POST:
        exam = Exam.objects.get(pk=exam_id)
        question = request.POST['input_data']
        if exam:
            question = Question.objects.create(question=question, exam=exam)
            return redirect("exam:get_exam", exam_id)
    return render(request, "add.html", {"title": "Add a question"})


def edit_question(request, exam_id, question_id):
    question = Question.objects.get(pk=question_id)
    if request.POST:
        question.question = request.POST['input_data']
        question.save()
        return redirect('exam:get_exam', exam_id)
    context = {"value": question,
               "title": "Edit question '{}'".format(question)}
    return render(request, 'edit.html', context)


def delete_question(request, exam_id, question_id):
    Question.objects.filter(pk=question_id).delete()
    return redirect("exam:get_exam", exam_id)
