import unittest
from app import create_app


class TestUserEndpoints(unittest.TestCase):
    '''Unitest for UserEndPoints'''
    def setUp(self):
        """Initialize the app and client before each test"""
        self.app = create_app()
        self.client = self.app.test_client()

    # POST Tests
    def test_create_user_valid_data(self):
        """Test user creation with valid data"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("error"), None)

    def test_create_user_invalid_first_name_none(self):
        """Test user creation with an empty first name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "Elodie",
            "email": "elo@elo.elo"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "First name can only contain letters and spaces")

    def test_create_user_invalid_first_name_out_of_range(self):
        """Test user creation with a first name that's too long"""
        response = self.client.post('/api/v1/users/', json={
            "first_name":
            "rtgfrtgfrtrtgfrtgfrtrtgfrtgfrtrtgfrtgfrtrtgfrtgfrtde",
            "last_name": "Elodie",
            "email": "elo@elo.elo"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "First name must be present with a maximum"
                         " of 50 characters and can only"
                         " contain letters and spaces '-' and '''.")

    def test_create_user_invalid_first_name_bad_character(self):
        """Test user creation with invalid characters in the first name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Elodi3@/%",
            "email": "elo@elo.elo"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "The email format is invalid.")

    def test_create_user_invalid_last_name_none(self):
        """Test user creation with an empty last name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Elodie",
            "last_name": "",
            "email": "elo@elo.elo"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Last name can only contain letters and spaces")

    def test_create_user_invalid_last_name_out_of_range(self):
        """Test user creation with a first name that's too long"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Elodie",
            "last_name":
            "ElodieElodieElodieExzddedededdedloediElodieElodieElodieEdloedi",
            "email": "elo@elo.elo"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Last name must be present with a maximum of 50"
                         " characters and can only contain letters "
                         "and spaces.")

    def test_create_user_invalid_first_name_bad_character(self):
        """Test user creation with invalid characters in the first name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Elodie",
            "last_name": "Elodi3@/%",
            "email": "elo@elo.elo"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Last name can only contain letters and spaces")

    def test_create_user_invalid_email_format(self):
        """Test user creation with an invalid email format"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Elodie",
            "last_name": "Elodie",
            "email": "elo@elo."
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "The email format is invalid.")

    def test_create_user_invalid_email_none(self):
        """Test user creation with an invalid email format"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Elodie",
            "last_name": "Elodie",
            "email": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "The email format is invalid.")


class TestAmenityEndpoints(unittest.TestCase):
    '''Unitest for AmenityEndPoints'''
    def setUp(self):
        """Initialize the app and client before each test"""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_amenity_create_valid(self):
        """Test amenity creation with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Piscine"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("error"), None)

    def test_amenity_create_name_none(self):
        """Test amenity creation with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Amenity name must be a string "
                         "of 1 to 50 characters.")

    def test_amenity_create_name_oput_of_range(self):
        """Test amenity creation with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "stringstringstringstringstri"
            "ngstringstringstringstringstringstring"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Amenity name must be a string "
                         "of 1 to 50 characters.")


# Code to run the tests with detailed output
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
