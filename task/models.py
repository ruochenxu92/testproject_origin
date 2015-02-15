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
    taskName = models.ForeignKey(Task)
    content = models.TextField()

    def __unicode__(self):
        return self.taskName

class Article(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")
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


class Field(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return smart_unicode(self.name)


class Interest(models.Model):
    name = models.CharField(max_length=80)
    field = models.ForeignKey(Field)

    def __unicode__(self):
        return smart_unicode(self.name)


class Author(models.Model):
    name = models.CharField(max_length=80)
    #coauthors = models.ForeignKey()
    institution = models.CharField(max_length=80)
    field = models.ForeignKey(Field)
    interest = models.ManyToManyField(Interest)
    authorUrl = models.CharField(max_length=200)

    def __unicode__(self):
        return smart_unicode(self.name)


class Paper(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    author = models.ManyToManyField(Author)
    pub_date = models.DateTimeField(null=True, blank=True)# auto_now=False, auto_now_add=False
    citedTimes = models.IntegerField(default=0)
    paperUrl = models.CharField(max_length=200)

    def __unicode__(self):
        return smart_unicode(self.title)




