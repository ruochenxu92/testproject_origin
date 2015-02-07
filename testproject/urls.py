from django.conf.urls import patterns, include, url
from django.contrib import admin
from task import views
import haystack

urlpatterns = patterns('',
    #match list page with rule books, and will pass keyword args to views functions
    url(r'^$', views.ListTasksView.as_view()),
    url(r'^tasks/$', views.ListTasksView.as_view()),
    url(r'^tasksUpdate/(?P<pk>[\w-]+)$', views.TaskUpdate.as_view()),
    url(r'^tasksDelete/(?P<pk>[\w-]+)$', views.TaskDelete.as_view()),
    url(r'^tasksCreate/$', views.TaskCreate.as_view()),
    url(r'^tasksContact/$', views.ContactView.as_view()),
    (r'^descriptions/([\w-]+)/$', views.ListDescriptionView.as_view()),
    #
    #
    # url(r'^search/', include('haystack.urls')),
    (r'^search/', include('haystack.urls')),

    # url(r'^search/', include('haystack.urls')),
    url(r'^all/$', views.ListArticles.as_view()),

    url(r'^get/(?P<article_id>\d+)/$', 'task.views.article'),
)

