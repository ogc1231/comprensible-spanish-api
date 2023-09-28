from django.contrib.auth.models import User
from .models import Resource
from rest_framework import status
from rest_framework.test import APITestCase


class ResourceListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='sam', password='pass')

    def test_can_list_resources(self):
        sam = User.objects.get(username='sam')
        Resource.objects.create(owner=sam, title='How to Spanish')
        response = self.client.get('/resources/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_user_not_logged_in_cant_create_resource(self):
        response = self.client.post('/resources/', {'title': 'How to Spanish'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ResourceDetailViewTests(APITestCase):
    def setUp(self):
        sam = User.objects.create_user(username='sam', password='pass')
        tam = User.objects.create_user(username='tam', password='pass')
        Resource.objects.create(
            owner=sam, title='How to Spanish',
            desc='sams content',
            resource_url='www.dog.com'
        )
        Resource.objects.create(
            owner=tam, title='Dreaming Spanish',
            desc='tams content',
            resource_url='www.cat.com'
        )

    def test_can_retrieve_resource_using_valid_id(self):
        response = self.client.get('/resources/1/')
        self.assertEqual(response.data['title'], 'How to Spanish')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_resource_using_invalid_id(self):
        response = self.client.get('/resources/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cant_update_another_users_resource(self):
        self.client.login(username='sam', password='pass')
        response = self.client.put(
            '/resources/2/', {'title': 'Charlas Hispanas'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
