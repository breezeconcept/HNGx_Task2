from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Person

class PersonAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_data = {
            'name': 'John Doe',  # Name with spaces
            'age': 30,
        }
        self.url = '/api/'  # Updated URL for your endpoints

    def test_create_person(self):
        response = self.client.post(self.url, self.person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().name, 'John Doe')

    def test_read_person(self):
        person = Person.objects.create(**self.person_data)
        response = self.client.get(f'{self.url}{person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_update_person(self):
        person = Person.objects.create(**self.person_data)
        updated_data = {
            'name': 'Updated Name with Spaces',  # Updated name with spaces
            'age': 35,
        }
        response = self.client.put(f'{self.url}{person.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get().name, 'Updated Name with Spaces')

    def test_delete_person(self):
        person = Person.objects.create(**self.person_data)
        response = self.client.delete(f'{self.url}{person.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
