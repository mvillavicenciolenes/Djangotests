from django.test import TestCase
from myapp.models import Item

class TestModels(TestCase):
    
    def test_item_string_representation(self):
        item = Item(name='Test Item')
        self.assertEqual(str(item), 'Test Item')  # Check that the string representation is correct

    def test_item_name_field(self):
        item = Item(name='Test Item')
        self.assertEqual(item.name, 'Test Item')  # Check that the name field is being set correctly