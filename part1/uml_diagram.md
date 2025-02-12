````mermaid
classDiagram
class User {
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
    +place_title: String
    +place_description: String
    +place_price: Int
    +place_latitude: formated string
    +place_longitude : 
    +place_owner
    +place_create()
    +place_update()
    +place_delete()
    +place_listed()
}
class Review {
    +review_rating
    +review_comment
    +review_create()
    +review_delete()
    +review_listed_by_place()
}

class Amenity {
    +amenity_name
    +amenity_description
    +amenity_create()
    +amenity_delete()
    +amenity_listed()
}
Place -- Amenity
User -- Place
User -- Review
Place -- Review

```

