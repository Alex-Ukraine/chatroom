import json

from django.utils import timezone
from rest_framework.test import APITestCase

from chatapi.models import Message


class URLTests(APITestCase):
    def test_list_messages(self):
        response = self.client.get('/api/list/0/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_single_post_message(self):
        data = {
            "email": "string@gmail.com",
            "text": "string"
        }
        response = self.client.post('/api/single/', format='json', data=data)

        self.assertEqual(response.status_code, 201)

    def test_single_update_message(self):
        post = Message(email="string@gmail.com", text="string", create_date=timezone.now(), update_date=timezone.now())
        post.save()

        data = json.dumps({
            "email": "string@gmail.com",
            "text": "string1"
        })

        headers = {"accept: application/json"}
        response = self.client.patch(f'/api/single/{post.id}/', data=data,
                                     headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_single_delete_message(self):
        post = Message(email="string@gmail.com", text="string", create_date=timezone.now(), update_date=timezone.now())
        post.save()

        response = self.client.delete(f'/api/single/{post.id}/', format='json')
        self.assertEqual(response.status_code, 204)


