from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseRedirect

from models import Question
from forms import AskForm, AnswerForm


def paginate(request, qs):
    LIMIT = 10  # objects at one page
    try:
        limit = int(request.GET.get('limit', LIMIT))
    except ValueError:
        limit = LIMIT
    if limit > 100:
        limit = LIMIT
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

def question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'question.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form
        })

@require_GET
def main(request):
    questions = Question.objects.order_by('-id')
    paginator, page = paginate(request, questions)
    return render(request, 'list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        })

@require_GET
def popular(request):
    questions = Question.objects.order_by('-rating')
    paginator, page = paginate(request, questions)
    return render(request, 'list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
        })

def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'answer.html', {
        'form': form
        })


def test(request, *args, **kwargs):
    return HttpResponse('Test passed.')
