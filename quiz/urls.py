from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<topic_id>[0-9]+)/check_answers/$', views.check_answers, name='check_answers'),

    url(r'^(?P<topic_id>[0-9]+)/check_answers/answer/$', views.answer, name='answer'),
]


