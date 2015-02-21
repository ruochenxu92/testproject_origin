# import datetime
#
# from haystack import indexes
# from task.models import Task
#
#
# class TaskIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     pub_date = indexes.DateTimeField(model_attr='pub_date')
#
#     content_auto = indexes.EdgeNgramField(model_attr='title')
#
#     def get_model(self):
#         return Task
#
#     """
#     return all the objects
#     """
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()
import datetime
from haystack import indexes
from task.models import Job,cs499Item


# class NoteIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     author = indexes.CharField(model_attr='user')
#     pub_date = indexes.DateTimeField(model_attr='pub_date')
#
#     def get_model(self):
#         return Note
#
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


# class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     title = indexes.CharField(model_attr='title')
#     body = indexes.CharField(model_attr='body')
#
#     def get_model(self):
#         return Article
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()

class cs499itemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    abstract = indexes.CharField(model_attr='abstract')

    def get_model(self):
        return cs499Item

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


# class JobIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     type = indexes.CharField(model_attr='type', faceted=True)
#     location = indexes.CharField(model_attr='location', faceted=True)
#
#     def get_model(self):
#         return Job
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()