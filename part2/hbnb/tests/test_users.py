import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "Doe",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_get_non_existent_user(self):
        response = self.client.get('/api/v1/users/nonexixtent_id')
        self.assertEqual(response.status_code, 404)

    def test_get_all_users(self):
        response = self.client.get('api/v1/users/')
        self.assertEqual(response.status_code, 200)
        users = response.get_json()
        self.assertIsInstance(users, list)
        self.assertGreaterEqual(len(users), 1)
    
    def test_put_user_update(self):
        create_response = self.client.post('/api/v1/users/', json={
            "first_name": ":Michel",
            "last_name": "Smithr",
            "email": "michel.smith@example.com"
        })
        self.assertEqual(create_response.status_code, 201)
        user = create_response.get_json()
        user_id = user['id']
        update_data = {
            "first_name": "Mary",
            "last_name": "Smith",
            "email": "mary.smith@example.com"
        }
        update_response = self.client.put(f'/api/v1/users/{user_id}', json=update_data)
        self.assertEqual(update_response.status_code, 200)
        updated_user = update_response.get_json()
        self.assertEqual(updated_user['first_name'], "Mary")
        self.assertEqual(updated_user['email'], "mary.smith@example.com")


if __name__ == '__main__':
    unittest.main()