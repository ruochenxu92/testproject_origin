from django.utils import unittest
from django.test.client import RequestFactory
from haystack.views import SearchView


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.


        from django.test.client import RequestFactory
        from haystack.views import SearchView
        import urllib2
        url = '/search/?q=information'
        request = urllib2.Request(url)
        #request.add_header("Content-Type", "application/json") #
        sv = SearchView(request)
        sv.build_form()
        results = sv.get_results()
        # Test my_view() as if it were deployed at /customer/details
        self.assertEqual(len(results), 35)