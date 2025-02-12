````mermaid
classDiagram
class User {
    +UID
    +user_first_name: String
    +user_last_name: String
    +user_email: Formated String
    +user_password: String (private)
    +user_administrator: boolean (private)
    +user_register()
    +user_update()
    +user_delete()
}
class Place {
    +UID
    +place_title: String
    +place_description: String
    +place_price: Int
    +place_latitude: Formated Int
    +place_longitude : Formated Int
    +place_owner: String
    +place_create()
    +place_update()
    +place_delete()
    +place_listed()
}
class Review {
    +UID
    +review_rating: Int
    +review_comment: String
    +review_create()
    +review_delete()
    +review_listed_by_place()
}

class Amenity {
    +UID
    +amenity_name: String
    +amenity_description: String
    +amenity_create()
    +amenity_delete()
    +amenity_listed()
}
Place --> Amenity : has
User --> Place : owns
User --> Review : makes
Place <-- Review

```

