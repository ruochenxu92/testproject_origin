from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from task.models import Task, Description
from django.core.urlresolvers import reverse

from .forms import ContactForm


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

