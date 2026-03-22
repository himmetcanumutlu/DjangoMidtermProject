from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("Baktığınız soru: %s." % question_id)


def results(request, question_id):
    response = "Sorunun cevabına bakıyorsunuz: %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Soruya yanıt veriyorsunuz: %s." % question_id)