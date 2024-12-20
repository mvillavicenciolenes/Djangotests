from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    
    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))  # The 'index' view is routed to ''
        self.assertEqual(response.status_code, 200)  # Check that the page loads with a status code of 200
    
    def test_index_view_template_used(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'myapp/index.html')  # Check if the correct template is used