from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from task.models import Description,Task
from models import Article

class AnimalTestCase(TestCase):
    # def setUp(self):
    #     Task.objects.filter(name="CS499")
    #     Animal.objects.create(name="cat", sound="meow")

    # def test_animals_can_speak(self):
    #     task = Task.objects.get(name="CS499")
    #     print(task.id)
    #
    #     set = Description.objects.filter(taskName=task)
    #     self.assertEqual(set.count(), 3)
    #
    #     #lion = Animal.objects.get(name="lion")
    #     #self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     #self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_generate(self):
        article1 = Article(title='Amazon', body='Amazon is one the best company in the world')
        article1.save()
        article2 = Article(title='Facebook', body='Facebook is one the best company in the world')
        article2.save()
        article3 = Article(title='Dropbox', body='Dropbox is one the best company in the world')
        article3.save()