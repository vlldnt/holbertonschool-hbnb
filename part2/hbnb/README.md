# HbnB Project - Implementation of Business Logic and API Endpoints 🚀

- This phase of the HBnB project focuses on implementing the application's core structure, including the Presentation and Business Logic layers using Python and Flask.
- It involves developing key classes (User, Place, Review, Amenity) and setting up RESTful API endpoints with flask-restx to manage CRUD operations. While authentication and access control will be handled later, the emphasis is on creating a scalable, modular, and well-structured foundation for future enhancements.


## Project Structure 📂

```plaintext
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

### Explanation 📝

- The `app/` directory contains the core application code.
- The `api/` subdirectory houses the API endpoints, organized by version (`v1/`).
- The `models/` subdirectory contains the business logic classes (e.g., `user.py`, `place.py`).
- The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
- The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
- `run.py` is the entry point for running the Flask application.
- `config.py` will be used for configuring environment variables and application settings.
- `requirements.txt` will list all the Python packages needed for the project.
- `README.md` will contain a brief overview of the project.

## Business Logic Layer 🧠

The Business Logic layer is responsible for implementing the core functionality of the application. It includes the following key entities:

- **User**: Represents a user of the application.
- **Place**: Represents a place listed by a user.
- **Review**: Represents a review of a place by a user.
- **Amenity**: Represents an amenity available at a place.

### Entities and Responsibilities 📋

#### User 👤
- **Attributes**: `id`, `name`, `email`, `password`
- **Methods**:
    - `create_user(name, email, password)`: Creates a new user.
    - `get_user_by_id(user_id)`: Retrieves a user by their ID.
    - `update_user(user_id, **kwargs)`: Updates user attributes.
    - `delete_user(user_id)`: Deletes a user.

#### Place 🏠
- **Attributes**: `id`, `name`, `description`, `user_id`
- **Methods**:
    - `create_place(name, description, user_id)`: Creates a new place.
    - `get_place_by_id(place_id)`: Retrieves a place by its ID.
    - `update_place(place_id, **kwargs)`: Updates place attributes.
    - `delete_place(place_id)`: Deletes a place.

#### Review 📝
- **Attributes**: `id`, `text`, `user_id`, `place_id`
- **Methods**:
    - `create_review(text, user_id, place_id)`: Creates a new review.
    - `get_review_by_id(review_id)`: Retrieves a review by its ID.
    - `update_review(review_id, **kwargs)`: Updates review attributes.
    - `delete_review(review_id)`: Deletes a review.

#### Amenity 🛠️
- **Attributes**: `id`, `name`
- **Methods**:
    - `create_amenity(name)`: Creates a new amenity.
    - `get_amenity_by_id(amenity_id)`: Retrieves an amenity by its ID.
    - `update_amenity(amenity_id, **kwargs)`: Updates amenity attributes.
    - `delete_amenity(amenity_id)`: Deletes an amenity.

### Examples 💡

#### Creating a User
```python
from app.models.user import User

user = User.create_user(name="John Doe", email="john@example.com", password="securepassword")
print(user.id)  # Output: User ID
```

#### Creating a Place
```python
from app.models.place import Place

place = Place.create_place(name="Beach House", description="A lovely beach house.", user_id=user.id)
print(place.id)  # Output: Place ID
```

#### Creating a Review
```python
from app.models.review import Review

review = Review.create_review(text="Great place!", user_id=user.id, place_id=place.id)
print(review.id)  # Output: Review ID
```

#### Creating an Amenity
```python
from app.models.amenity import Amenity

amenity = Amenity.create_amenity(name="WiFi")
print(amenity.id)  # Output: Amenity ID
```

#### Unittests
We made 20 Unit tests to validate the creation of users, amenities, places, and reviews with various valid and invalid inputs.

```python
def test_create_user_valid_data(): # Creating a user with valid data ✅
def test_create_user_invalid_first_name_none(): # Creating a user with an empty first name ✅
def test_create_user_invalid_first_name_out_of_range(): # Creating a user with a too long first name ✅
def test_create_user_invalid_first_name_bad_character(): # Creating a user with invalid characters in the first name ✅
def test_create_user_invalid_last_name_none(): # Creating a user with an empty last name ✅
def test_create_user_invalid_last_name_out_of_range(): # Creating a user with a too long last name ✅
def test_create_user_invalid_last_name_bad_character(): # Creating a user with invalid characters in the last name ✅
def test_create_user_invalid_email_format(): # Creating a user with an invalid email format ✅
def test_create_user_invalid_email_none(): # Creating a user with an empty email ✅
def test_amenity_create_valid(): # Creating an amenity with valid data ✅
def test_amenity_create_name_none(): # Creating an amenity with an empty name ✅
def test_amenity_create_name_out_of_range(): # Creating an amenity with a too long name ✅
def test_place_create_valid_data(): # Creating a place with valid data ✅
def test_place_create_invalid_price(): # Creating a place with a negative price ✅
def test_place_create_invalid_latitude(): # Creating a place with an invalid latitude ✅
def test_place_create_invalid_longitude(): # Creating a place with an invalid longitude ✅
def test_place_create_invalid_user_id(): # Creating a place with an invalid user ID ✅
def test_review_create_valid_data(): # Creating a review with valid data ✅
def test_review_create_no_text(): # Creating a review without text ✅
def test_review_create_invalid_user_id(): # Creating a review with an invalid user ID ✅
def test_review_create_invalid_place_id(): # Creating a review with an invalid place ID ✅

    ....................
----------------------------------------------------------------------
Ran 20 tests in 0.311s

OK
```
