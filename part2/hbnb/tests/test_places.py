import unittest
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        # Test creating a place with valid data
        response = self.client.post('/api/v1/places/', json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_latitude(self):
        # Test creating a place with missing required fields
        response = self.client.post('/api/v1/places/', json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 200.0,  # Invalid latitude
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_missing_fields(self):
        # Test creating a place with missing required fields
        response = self.client.post('/api/v1/places/', json={
            "title": "", #Missing title
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 400)

    def test_get_nonexistent_place(self):
        # Test retrieving a non-existent place
        response = self.client.get('/api/v1/places/nonexistent_id')
        self.assertEqual(response.status_code, 404)

    def test_get_all_places(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
        places = response.get_json()
        self.assertIsInstance(places, list)
        self.assertGreaterEqual(len(places), 1)
    
    def test_put_place_update(self):
        create_response = self.client.post('/api/v1/places/', json={
        "title": "The luxury hotel of your dreams",
        "description": "Enjoy top class rooms",
        "price": 300.0,
        "latitude": 40.0,
        "longitude": -70.0,
        "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    })
        self.assertEqual(create_response.status_code, 201)
        place = create_response.get_json()
        place_id = place["id"]
        
        update_data = {
            "title": "The luxury hotel of your dreams",
            "description": "Enjoy top class rooms",
            "price": 500.0,
            "latitude": 40.0,
            "longitude": -70.0,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
        update_response = self.client.put(f'/api/v1/places/{place_id}', json=update_data)
        self.assertEqual(update_response.status_code, 200)
        updated_place = update_response.get_json()
        self.assertEqual(updated_place["price"], 500.0)


if __name__ == '__main__':
    unittest.main()
