from django.shortcuts import render, redirect
# from django.views.generic import CreateView
from .models import Answer
from question.models import Question


def edit_answer(request, exam_id, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    if request.POST:
        answer.answer = request.POST['input_data']
        answer.save()
        return redirect('exam:get_exam', exam_id)
    context = {"value": answer.answer,
               "title": "Edit answer '{}'".format(answer)}
    return render(request, 'edit.html', context)


def add_answer(request, exam_id, question_id):
    if request.POST:
        question = Question.objects.get(pk=question_id)
        answer = request.POST['input_data']
        if answer:
            answer = Answer.objects.create(answer=answer, question=question)
            return redirect("exam:get_exam", exam_id)
    return render(request, "add.html", {"title": "Add an answer"})


def delete_answer(request, exam_id, answer_id):
    Answer.objects.filter(pk=answer_id).delete()
    return redirect("exam:get_exam", exam_id)
