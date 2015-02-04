from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from task.models import Task, Description
from django.core.urlresolvers import reverse

from .forms import ContactForm
from .models import Article

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
#
# #
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

