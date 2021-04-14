from django.http.response import Http404
from django.shortcuts import render,HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context = {'question':question}
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = 
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    return HttpResponse("you are looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("you are voting on the question %s." % question_id) 