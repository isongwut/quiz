from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import Topic,Question,Choice


def index(request):
    latest_topic_list = Topic.objects.order_by('-pub_date')[:]
    context = {'latest_topic_list': latest_topic_list}
    return render(request, 'quiz/index.html',context)

def detail(request,topic_id):
    topic = Topic.objects.get(pk = topic_id)
    return render(request, 'quiz/detail.html',{'topic':topic})

def check_answers(request,topic_id):
    topic = Topic.objects.get(pk=topic_id)
    score = 0
    for question in topic.question_set.all():
        for choice in question.choice_set.all():
            selected_choice = request.POST.get(str(choice.id),False)
            if(str(selected_choice) == 'True'):
                score += 1
    context = {'topic':topic,'score':score,'questions':topic.question_set.count()}
    return render(request, 'quiz/result.html',context)

def answer(request,topic_id):
    topic = Topic.objects.get(pk = topic_id)
    return render(request, 'quiz/answer.html',{'topic':topic})

