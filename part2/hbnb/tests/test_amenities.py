import unittest
from app import create_app


class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        # Test creating an amenity with valid data
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_empty_name(self):
        # Test creating an amenity with an empty name
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""  # Empty name
        })
        self.assertEqual(response.status_code, 400)

    def test_get_nonexistent_amenity(self):
        # Test retrieving a non-existent amenity
        response = self.client.get('/api/v1/amenities/nonexistent_id')
        self.assertEqual(response.status_code, 404)
    
    def test_get_all_amenities(self):
        self.client.post('/api/v1/amenities/', json={"name": "Pool"})
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        amenities = response.get_json()
        self.assertIsInstance(amenities, list)
        self.assertGreaterEqual(len(amenities), 1)


if __name__ == '__main__':
    unittest.main()

