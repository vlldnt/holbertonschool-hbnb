import re
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    """Facade for managing users, places, amenities, and reviews."""

    def __init__(self):
        """Initialize repositories for different models."""
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User Facade
    def create_user(self, user_data):
        """Create a new user with validation."""
        if not re.fullmatch(r'^[A-Za-zÀ-ÖØ-öø-ÿ -\']+$',
                            user_data['first_name']):
            raise ValueError("First name can only contain letters and spaces")
        if not re.fullmatch(r'^[A-Za-zÀ-ÖØ-öø-ÿ -\']+$',
                            user_data['last_name']):
            raise ValueError("Last name can only contain letters and spaces")

        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve a user by ID."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Retrieve a user by email."""
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        """Update user details with validation."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        if ('first_name' in user_data and
            (len(user_data['first_name']) > 50 or
             not re.fullmatch(r'^[A-Za-zÀ-ÖØ-öø-ÿ -\']+$',
                              user_data['first_name']))):
            raise ValueError(
                "Updated first name must be present with a maximum of 50 "
                "characters and can only contain letters and spaces."
            )
        if ('last_name' in user_data and
            (len(user_data['last_name']) > 50 or
             not re.fullmatch(r'^[A-Za-zÀ-ÖØ-öø-ÿ -\']+$',
                              user_data['last_name']))):
            raise ValueError(
                "Updated last name must be present with a maximum of 50 "
                "characters and can only contain letters and spaces."
            )
        if ('email' not in user_data or
            ('email' in user_data and not re.fullmatch(
                r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                user_data['email']))):
            raise ValueError("Email format for update is invalid")

        user.update(user_data)
        self.user_repo.save(user)
        return user

    def get_all_users(self):
        """Retrieve all users."""
        return self.user_repo.get_all()

    # Amenity Facade
    def create_amenity(self, amenity_data):
        """Create a new amenity."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by ID."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity."""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            raise ValueError("Amenity not found")

        amenity.update(amenity_data)
        self.amenity_repo.save(amenity)
        return amenity

    def get_amenity_by_name(self, name):
        """Retrieve an amenity by name."""
        return self.amenity_repo.get_by_attribute('name', name)

    # Place Facade
    def create_place(self, title, description, price, latitude,
                     longitude, owner_id, amenities=None):
        """Create a new place with validation."""
        owner = self.get_user(owner_id)

        if not owner:
            raise ValueError("Owner not found.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180.0 and 180.0")

        place = Place(
            title=title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner
        )

        if amenities:
            for amenity_id in amenities:
                amenity = self.get_amenity(amenity_id)
                if not amenity:
                    raise ValueError(
                        f"Amenity with ID {amenity_id} not found."
                    )
                place.add_amenity(amenity)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieve a place by ID."""
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        """Retrieve all places."""
        return self.place_repo.get_all()

    # Review Facade
    def create_review(self, text, user_id, place_id, rating):
        """Create a new review."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found.")

        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found.")

        review = Review(
            text=text,
            user_id=user.id,
            place_id=place.id,
            rating=rating,
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return "Place not found"
        return [review for review in
                self.review_repo.get_all() if review.place == place_id]

    def update_review(self, review_id, review_update):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        for key, value in review_update.items():
            if hasattr(review, key):
                setattr(review, key, value)
        self.review_repo.update(review_id, review.__dict__)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        self.review_repo.delete(review_id)
        return {'message': 'Review deleted succesessfully'}
