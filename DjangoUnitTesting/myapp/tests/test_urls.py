from django.test import TestCase
from django.urls import reverse

class TestUrls(TestCase):
    
    def test_index_url(self):
        url = reverse('index')  # This will resolve to the URL for the 'index' view
        self.assertEqual(url, '/')  # Check that the 'index' URL is the root URL