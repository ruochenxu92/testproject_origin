from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from task.models import Description,Task
from models import Article,Note
import datetime
class AnimalTestCase(TestCase):
    def test_generate_Article(self):
        article1 = Article(title='Amazon', body='Amazon is one the best company in the world')
        article1.save()
        article2 = Article(title='Facebook', body='Facebook is one the best company in the world')
        article2.save()
        article3 = Article(title='Dropbox', body='Dropbox is one the best company in the world')
        article3.save()


    def test_generate_Note(self):
        Note1 = Note(title="Amazon", body="Amazon is great", pub_date=datetime.now())
        Note1.save()




