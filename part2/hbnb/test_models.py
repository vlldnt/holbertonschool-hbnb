import unittest
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.services.facade import HBnBFacade

class TestUserModel(unittest.TestCase):
    def test_user_creation(self):
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            User(first_name="John123", last_name="Doe", email="john.doe@example.com")

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            User(first_name="John", last_name="Doe123", email="john.doe@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User(first_name="John", last_name="Doe", email="john.doe@com")

class TestAmenityModel(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

class TestPlaceModel(unittest.TestCase):
    def setUp(self):
        self.facade = HBnBFacade()
        self.owner = User(first_name="John", last_name="Doe", email="john.doe@example.com")

    def test_place_creation(self):
        place = Place(title="Nice Place", description="A very nice place", price=100, latitude=40.71, longitude=-74.01, owner=self.owner)
        self.assertEqual(place.title, "Nice Place")
        self.assertEqual(place.description, "A very nice place")
        self.assertEqual(place.price, 100)
        self.assertEqual(place.latitude, 40.71)
        self.assertEqual(place.longitude, -74.01)
        self.assertEqual(place.owner, self.owner)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Place(title="Nice Place", description="A very nice place", price=-100, latitude=40.7128, longitude=-74.0060, owner=self.owner)

    def test_invalid_latitude(self):
        with self.assertRaises(ValueError):
            Place(title="Nice Place", description="A very nice place", price=100, latitude=100, longitude=-74.0060, owner=self.owner)

    def test_invalid_longitude(self):
        with self.assertRaises(ValueError):
            Place(title="Nice Place", description="A very nice place", price=100, latitude=40.7128, longitude=-200, owner=self.owner)

    def test_add_amenity(self):
        place = Place(title="Nice Place", description="A very nice place", price=100, latitude=40.7128, longitude=-74.0060, owner=self.owner)
        amenity = Amenity(name="WiFi")
        place.add_amenity(amenity)
        self.assertIn(amenity, place.amenities)

class TestReviewModel(unittest.TestCase):
    def setUp(self):
        self.facade = HBnBFacade()

    def test_review_creation(self):
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        place = Place(title="Nice Place", description="A very nice place", price=100, latitude=40.7128, longitude=-74.0060, owner=user)
        review = Review(text="Great place!", user_id=user.id, place_id=place.id, rating=5)
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.user_id, user.id)
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.rating, 5)

    def test_invalid_rating(self):
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        place = Place(title="Nice Place", description="A very nice place", price=100, latitude=40.7128, longitude=-74.0060, owner=user)
        with self.assertRaises(ValueError):
            Review(text="Great place!", user_id=user.id, place_id=place.id, rating=6)

    def test_create_review_with_invalid_user(self):
        place = Place(title="Nice Place", description="A very nice place", price=100, latitude=40.7128, longitude=-74.0060, owner=None)
        with self.assertRaises(ValueError):
            self.facade.create_review(text="Great place!", user_id=999, place_id=place.id, rating=5)

if __name__ == '__main__':
    unittest.main()
