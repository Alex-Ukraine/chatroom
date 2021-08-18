import json

from django.test import TestCase


class URLTests(TestCase):
    number = 0

    def test_list_messages(self):
        response = self.client.get('/api/list/0/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_single_post_message(self):
        data = {
            "email": "string@gmail.com",
            "text": "string"
        }
        response = self.client.post('/api/single/', format='json', data=data)
        URLTests.number = response.data['id']
        print(URLTests.number)
        self.assertEqual(response.status_code, 201)

    def test_single_update_message(self):
        data = json.dumps({
            "email": "string@gmail.com",
            "text": "string1"
        })
        headers = {"accept: application/json"}
        response = self.client.patch('/api/single/1/', data, headers=headers, content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_single_delete_message(self):
        response = self.client.delete('/api/single/1/', format='json')
        self.assertEqual(response.status_code, 204)


