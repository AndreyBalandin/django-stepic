from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from models import Question

@require_GET
def question(request, id):
    print(id)
    question = get_object_or_404(Question, id=id)
    print(question.title)
    return render(request, 'question.html', {
	'question': question,
	'answers': question.answer_set.all(),
	})


def test(request, *args, **kwargs):
    return HttpResponse('Test passed.')
