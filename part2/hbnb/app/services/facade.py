from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if user:
            user.update(user_data)
            self.user_repo.save(user)
            return user
        else:
            raise ValueError("User not found")

    def get_all_users(self):
        return self.user_repo.get_all()
    
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)
        
    def get_all_amenities(self):
        return self.amenity_repo.get_all() 

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if amenity:
            amenity.update(amenity_data)
            self.amenity_repo.save(amenity)
            return amenity
        else:
            raise ValueError("Amenity not found")

    def get_amenity_by_name(self, name):
        return self.amenity_repo.get_by_attribute('name', name)
    
    def create_place(self, title, description, price, latitude, longitude, owner_id, amenities):
        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError("Owner not found.")
        
        place = Place(
            title=title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner
        )
        
        for amenity_id in amenities:
            amenity = self.get_amenity(amenity_id)
            if amenity:
                place.add_amenity(amenity)
        
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if place:
            owner = self.get_user(place.owner.id)
            amenities = [self.get_amenity(amenity.id) for amenity in place.amenities if amenity is not None]
            place.owner = owner
            place.amenities = amenities
            return place
        else:
            raise ValueError("Place not found")

    def get_all_places(self):
        places = self.place_repo.get_all()
        for place in places:
            owner = self.get_user(place.owner.id)
            amenities = [self.get_amenity(amenity.id) for amenity in place.amenities if amenity is not None]
            place.owner = owner
            place.amenities = amenities
        return places

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            if 'price' in place_data and place_data['price'] < 0:
                raise ValueError("Price cannot be negative")
            if 'latitude' in place_data and not (-90 <= place_data['latitude'] <= 90):
                raise ValueError("Latitude must be between -90 and 90")
            if 'longitude' in place_data and not (-180 <= place_data['longitude'] <= 180):
                raise ValueError("Longitude must be between -180 and 180")
            if 'amenities' in place_data:
                place_data['amenities'] = [self.get_amenity(amenity_id) for amenity_id in place_data['amenities']]
            place.update(place_data)
            self.place_repo.save(place)
            return place
        else:
            raise ValueError("Place not found")

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found, please enter a valid review title")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return "Place not found, please enter a valid place"
        return [review for review in self.review_repo.get_all() if review.place == place_id]

    def update_review(self, review_id, review_update):
        review = self.review_repo.get(review_id)
        if not review:
            return ("Review not found, please enter a valid review title")
        for key, value in review_update.items():
            if hasattr(review, key):
                setattr(review, key, value)
        self.review_repo.update(review_id, review.__dict__)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return ("Review not found, please enter a valid review title")
        self.review_repo.delete(review_id)
        return {'message': 'Review deleted succesessfully'}
