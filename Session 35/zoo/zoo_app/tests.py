from django.test import TestCase
from .models import Species

# Create your tests here.

class ZooTests(TestCase):
    def setUp(self):
        self.species = Species(name='Cobra', category='Reptile')

    def test_name(self):
        self.assertEqual(self.species.name, 'Cobra')

    def test_category(self):
        self.assertEqual(self.species.category, 'Reptile')

    def test_description(self):
        self.assertEqual(self.species.description, None)

    def test_index_status_code(self):
        response = self.client.get('/zoo_app/')
        self.assertEqual(response.status_code, 200)
