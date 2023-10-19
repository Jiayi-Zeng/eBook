from django.shortcuts import render
from .models import ClozeQuestion
from django.http import Http404

def detail(request, question_id):
    try:
        question = ClozeQuestion.objects.get(pk=question_id)
    except ClozeQuestion.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})