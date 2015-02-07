from django.db import models
from django.contrib.auth.models import User

class Task (models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class  Description(models.Model):
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