````mermaid
classDiagram
class User {
    +user_first_name
    +user_last_name
    +user_email
    +user_password
    +user_administrator
    +user_register()
    +user_update()
    +user_delete()
}
class Place {
    +place_title
    +place_description
    +place_price
    +place_latitude
    +place_longitude
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

