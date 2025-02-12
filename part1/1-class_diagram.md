````mermaid
classDiagram
class User {
    +UID: String
    +user_first_name: String
    +user_last_name: String
    +user_email: String
    +user_password: String
    +user_administrator: boolean
    +user_register()
    +user_update()
    +user_delete()
}
class Place {
    +UID: String
    +place_title: String
    +place_description: String
    +place_price: int
    +place_latitude: float
    +place_longitude: float
    +place_owner: String
    +place_create()
    +place_update()
    +place_delete()
    +place_listed()
}
class Review {
    +UID: String
    +review_rating: int
    +review_comment: String
    +review_create()
    +review_delete()
    +review_listed_by_place()
}

class Amenity {
    +UID: String
    +amenity_name: String
    +amenity_description: String
    +amenity_create()
    +amenity_delete()
    +amenity_listed()
}
Place --> Amenity : has
User --> Place : owns
User --> Place : searchs
User --> Review : makes
Place --> Review : has

```

