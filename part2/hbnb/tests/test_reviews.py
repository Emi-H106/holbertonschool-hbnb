import unittest
from app import create_app


class TestReviewEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        # Test creating a review with valid data
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place to stay!",
            "rating": 5,
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_review_invalid_rating(self):
        # Test creating a review with an invalid rating
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place to stay!",
            "rating": 6,  # Invalid rating
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_review_missing_fields(self):
        # Test creating a review with missing required fields
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place to stay!",
            "rating": 5,
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            # Missing place_id
        })
        self.assertEqual(response.status_code, 400)

    def test_get_nonexistent_review(self):
        # Test retrieving a non-existent review
        response = self.client.get('/api/v1/reviews/nonexistent_id')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
