import json
from rest_framework.test import APITestCase


class URLTests(APITestCase):
    number = 0

    def postmessage(self):
        data = {
            "email": "string@gmail.com",
            "text": "string"
        }
        return self.client.post('/api/single/', format='json', data=data)

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
        response = self.postmessage()
        URLTests.number = response.data['id']

        data = json.dumps({
            "email": "string@gmail.com",
            "text": "string1"
        })
        headers = {"accept: application/json"}
        response = self.client.patch(f'/api/single/{URLTests.number}/', data=data,
                                     headers=headers, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_single_delete_message(self):
        response = self.postmessage()
        URLTests.number = response.data['id']

        response = self.client.delete(f'/api/single/{URLTests.number}/', format='json')
        self.assertEqual(response.status_code, 204)


