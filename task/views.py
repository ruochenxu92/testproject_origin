from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from task.models import Task, Description
from django.core.urlresolvers import reverse
from django.contrib import auth
from .forms import ContactForm, MyRegistrationForm, ArticleForm
from .models import Article
from django.contrib import messages

class TaskUpdate(UpdateView):
    model = Task
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = '../tasks'

class TaskDelete(DeleteView):
    model = Task
    success_url = '../tasks'

class ContactView(FormView):
    template_name = 'task/contact.html'
    form_class = ContactForm
    success_url = '../tasks'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

class ListTasksView(ListView):
    model = Task

    queryset = Task.objects.all()

class TaskCreate(CreateView):
    model = Task
    fields = ['name']  #list of field need to fill in

    success_url = '../tasks'

class ListDescriptionView(ListView):
    model = Description

    def get_queryset(self):
        self.task = get_object_or_404(Task, name=self.args[0])
        context = Description.objects.filter(taskName=self.task)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(ListTasksView,self).get_context_data(kwargs)
    #     context['name'] = Task.objects.filter(name=kwargs)
    #     return context
#
#
# from haystack.query import SearchQuerySet
#
# def search_titles(request):
#     tasks = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text'), '')
#
#     return render_to_response('ajax_search.html', {'tasks', tasks})
#



class ListArticles(ListView):
    model = Article
    queryset = Article.objects.all()



def article(request, article_id = 1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})


def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Article.objects.filter(title_contains=search_text)
    return render_to_response('ajax_search.html', {'articles': articles})


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    full_name = request.user.username
    return render_to_response('loggedin.html',
                             locals(),context_instance=RequestContext(request))

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    else:
        form = MyRegistrationForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')



def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "You Article was added")
            return HttpResponseRedirect('/all')
    else:
        form = ArticleForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('create_article.html', args)



def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        a.likes += 1
        a.save()

    return HttpResponseRedirect('../../get/%s' % article_id)


