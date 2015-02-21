from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from task.models import Task, Description,cs499Item
from django.core.urlresolvers import reverse
from django.contrib import auth
from .forms import ContactForm, MyRegistrationForm, ArticleForm
from .models import Article
from django.contrib import messages
import time
from django.conf import settings
from django.core.mail import send_mail,send_mass_mail

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

def cs499item(request, article_id = 1):
    return render_to_response('cs499item.html', {'article': cs499Item.objects.get(id=article_id)})



def search_titles1(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    articles = Article.objects.filter(title_contains=search_text)
    return render_to_response('ajax_search.html', {'articles': articles})


def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    cs499items = cs499Item.objects.filter(title_contains=search_text)
    return render_to_response('ajax_search.html', {'cs499items':cs499items})


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
        a = cs499Item.objects.get(id=article_id)
        a.likes += 1
        a.save()
    return HttpResponseRedirect('../../get/%s' % article_id)







'''
TODO make recommendations for all people base the requirements
'''
def getcs499Item():
    field = 'Information Theory'
    result = cs499Item.objects.filter(category__icontains=field)
    return result




    # from haystack.views import SearchView
    # sv = SearchView()
    # sv.build_form('information')
    # result = sv.get_results()
    # print("results=",len(result))
    # from django.test.client import RequestFactory
    # from haystack.views import SearchView
    # request = RequestFactory.get('/search/?q=information')


    #
    # from haystack.views import SearchView
    # import urllib2
    # url = '/search/?q=information'
    # request = urllib2.Request(url)
    # #request.add_header("Content-Type", "application/json") #
    # sv = SearchView(request)
    # sv.build_form()
    # result = sv.get_results()
    #
    #
    # # sv = SearchView(request)
    # # sv.build_form()
    # # result = sv.get_results()
    # print("result=",len(result))
    # return result

def getRecommendation():
    return ['xxu46@illinois.edu']

def send_email(request):
        items = getcs499Item()
        subject = ''
        messages =''
        i = 1

        for item in items:

            paper = 'Here is the ' + str(i) + ' paper\n\n'
            paper += 'This is link for detail information '+ str(item.urllink) + '\n'
            paper += 'The pdf link is here '+str(item.pdflink)+'\n'
            paper += 'The title:' + str(item.title) + '\n'
            #safe_str = str(item.authors).encode('ascii', 'ignore')
            #paper += 'The authors: ' +   str(item.authors) + '\n'
            paper += 'The subject: ' + str(item.subjects) + '\n'
            paper += 'The abstract:\n '+ str(item.abstract)+ '\n'
            paper += 'The date: ' + str(item.date) + '\n\n\n\n\n\n'
            messages += paper
            subject = 'recommendation for recent paper from ' + str(item.category) + 'field'
            i += 1
        send_mail(subject, messages, settings.EMAIL_HOST_USER, getRecommendation, fail_silently=False)
        #
        # connection = SMTPConnection(username=auth_user, password=auth_password, fail_silently=fail_silently)
        # email = EmailMessage(subject, message, from_email, recipient_list, connection=connection, encoding='utf8').send()
        #

        return render_to_response('register_success.html')








def autoGenerateQueries():
    pass

def GetEmailList():
    pass






from datetime import date
from haystack.views import SearchView
from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystack.query import EmptySearchQuerySet
class MySearchView(SearchView):
    """My custom search view."""

    # def get_queryset(self):
    #     queryset = super(MySearchView, self).get_queryset()
    #     # further filter queryset based on some set of criteria
    #     return queryset.filter(pub_date__gte=date(2015, 1, 1))
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super(MySearchView, self).get_context_data(*args, **kwargs)
    #     # do something
    #     return context

    # def basic_search(request, template='search/search.html', load_all=True, form_class=ModelSearchForm, searchqueryset=None, context_class=RequestContext, extra_context=None, results_per_page=None):
    #     query = ''
    #     results = EmptySearchQuerySet()
    #     if request.GET.get('q'):
    #         form = form_class(request.GET, searchqueryset=searchqueryset, load_all=load_all)
    #         if form.is_valid():
    #             query = form.cleaned_data['q']
    #             results = form.search()
    #     else:
    #         form = form_class(searchqueryset=searchqueryset, load_all=load_all)


    def get_results(self):
        """
        Fetches the results via the form.
        Returns an empty list if there's no query to search with.
        """
        results =  self.form.search()
        print("results",len(results))

        items = getcs499Item()
        subject = ''
        messages =''
        i = 1
        for item in items:
            paper = 'Here is the ' + str(i) + ' paper\n\n'
            paper += 'This is link for detail information '+ str(item.urllink) + '\n'
            paper += 'The pdf link is here '+str(item.pdflink)+'\n'
            paper += 'The title:' + str(item.title) + '\n'
            #safe_str = str(item.authors).encode('ascii', 'ignore')
            #paper += 'The authors: ' +   str(item.authors) + '\n'
            paper += 'The subject: ' + str(item.subjects) + '\n'
            paper += 'The abstract:\n '+ str(item.abstract)+ '\n'
            paper += 'The date: ' + str(item.date) + '\n\n\n\n\n\n'
            messages += paper
            subject = 'recommendation for recent paper from ' + str(item.category) + 'field'
            i += 1
        send_mail(subject, messages, settings.EMAIL_HOST_USER,  ['xxu46@illinois.edu'], fail_silently=False)
        #
        # connection = SMTPConnection(username=auth_user, password=auth_password, fail_silently=fail_silently)
        # email = EmailMessage(subject, message, from_email, recipient_list, connection=connection, encoding='utf8').send()
        return results







'''
I think the only way to improve the results is to know
1. add more records to database(already solved by automatically insert records into db)
2. collect keywords from professors
3. use keywords to do query on whoosh.
4. return back the results to users.
'''