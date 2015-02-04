import datetime

from haystack import indexes
from task.models import Task


class TaskIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Task

    """
    return all the objects
    """
    def index_queryset(self, using=None):
        return self.get_model().objects.all()


