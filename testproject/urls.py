from django.conf.urls import patterns, include, url
from django.contrib import admin
from task import views
import haystack
from task.views import MySearchView

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

    url(r'^mysearchview/$', MySearchView(), name='search_view'),

    url(r'^accounts/register/$', 'task.views.register_user'),
    url(r'^accounts/register_success/$', 'task.views.register_success'),

    url(r'^accounts/login/$', 'task.views.login'),
    url(r'^accounts/auth/$', 'task.views.auth_view'),
    url(r'^accounts/logout/$', 'task.views.logout'),
    url(r'^accounts/loggedin/$', 'task.views.loggedin'),
    url(r'^accounts/invalid/$', 'task.views.invalid_login'),


    # url(r'^search/', include('haystack.urls')),
    url(r'^all/$', views.ListArticles.as_view()),
    url(r'^create/$', 'task.views.create'),

    #url(r'^get/(?P<article_id>\d+)/$', 'task.views.article'),
    url(r'^get/(?P<article_id>\d+)/$', 'task.views.cs499item'),

    url(r'^send_email/$', 'task.views.send_email'),

    url(r'^like/(?P<article_id>\d+)/$', 'task.views.like_article'),
)

