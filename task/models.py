import django
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
import datetime

class Task (models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Description(models.Model):
    taskName = models.ForeignKey(Task, blank=True)
    content = models.TextField()

    def __unicode__(self):
        return self.taskName

class Article(models.Model):
    title = models.CharField(max_length=40, blank=True)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField("date published",blank=True)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    #user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=32)


'''
Start my real project models,@TODO need modify the specific in the Field()
class Article(models.Model):
    STATUS = Choices('draft', 'published')
    # ...
    status = StatusField()
'''

#
#
#
# class Field(models.Model):
#     name = models.CharField(max_length=80)
#
#     def __unicode__(self):
#         return smart_unicode(self.name)
#
#     class Meta:
#         ordering = ('name',)
#
# class Interest(models.Model):
#     name = models.CharField(max_length=80)
#     field = models.CharField
#
#     def __unicode__(self):
#         return smart_unicode(self.name)
#
#     class Meta:
#         ordering = ('name',)
#
# class Author(models.Model):
#     name = models.CharField(max_length=80)
#     institutions = models.CharField(max_length=80,null=True, blank=True)
#     field = models.ForeignKey(Field, blank=True)
#     interest = models.ManyToManyField(Interest, blank=True)
#     authorUrl = models.CharField(max_length=200,null = True,blank=True)
#
#     def __unicode__(self):
#         return smart_unicode(self.name)
#
#     class Meta:
#         ordering = ('field',)
#
# class Paper(models.Model):
#     title = models.CharField(max_length=80)
#     content = models.TextField(blank=True)
#     author = models.ManyToManyField(Author, blank=True)
#     pub_date = models.DateTimeField(blank=True, null=True)# auto_now=False, auto_now_add=False
#     citedTimes = models.IntegerField(blank=True, default=0)
#     paperUrl = models.CharField(max_length=200, null=True, blank=True)
#
#     def __unicode__(self):
#         return smart_unicode(self.title)
#
#     class Meta:
#         ordering = ('title',)
# # from task.models import Field, Interest, Author, Paper
# # f = Field.objects.filter(pk=1)[0]
# # i = Interest.objects.filter(pk=1)[0]
# # author = Author(name='Manoj Prabhakaran',institutions='Computer Science, University of Illinois Urbana-Champaign',field=f,authorUrl='http://web.engr.illinois.edu/~mmp/')
#


class Page(models.Model):
    title = models.CharField(max_length=80,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    pubDate = models.DateTimeField(blank=True, null=True)# auto_now=False, auto_now_add=False
    citedTimes = models.IntegerField(default=0)
    paperUrl = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=80,null = True,blank=True)
    institution = models.CharField(max_length=80,null=True, blank=True)
    field = models.CharField(max_length=80, null=True, blank=True)
    interest = models.CharField(max_length=80, null = True,blank=True)
    authorUrl = models.CharField(max_length=200, null = True,blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    class Meta:
        ordering = ('author',)






