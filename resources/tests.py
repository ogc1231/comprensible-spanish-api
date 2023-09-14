from django.contrib.auth.models import User
from .models import Resource
from rest_framework import status
from rest_framework.test import APITestCase


class ResourceListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_resources(self):
        adam = User.objects.get(username='adam')
        Resource.objects.create(owner=adam, title='a title')
        response = self.client.get('/resources/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    # def test_logged_in_user_can_create_resource(self):
    #     self.client.login(username='adam', password='pass')
    #     response = self.client.post('/resources/', {'title': 'a title'})
    #     count = Resource.objects.count()
    #     self.assertEqual(count, 1)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_resource(self):
        response = self.client.post('/resources/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ResourceDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Resource.objects.create(
            owner=adam, title='a title',
            description='adams content',
            resource_url='www.dog.com'
        )
        Resource.objects.create(
            owner=brian, title='another title',
            description='brians content',
            resource_url='www.cat.com'
        )

    def test_can_retrieve_resource_using_valid_id(self):
        response = self.client.get('/resources/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_resource_using_invalid_id(self):
        response = self.client.get('/resources/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_user_can_update_own_resource(self):
    #     self.client.login(username='adam', password='pass')
    #     response = self.client.put('/resources/1/', {'title': 'a new title'})
    #     resource = Resource.objects.filter(pk=1).first()
    #     self.assertEqual(resource.title, 'a new title')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_resource(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/resources/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
