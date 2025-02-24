classDiagram
class User {
    +UUID id
    +string firstName
    +string lastName
    +string email
    +string password
    +bool isAdmin
    +DateTime createdAt
    +DateTime updatedAt
    +register()
    +updateProfile()
    +delete()
}

class Place {
    +UUID id
    +string title
    +string description
    +float price
    +float latitude
    +float longitude
    +DateTime createdAt
    +DateTime updatedAt
    +create()
    +update()
    +delete()
}

class Review {
    +UUID id
    +User user
    +Place place
    +int rating
    +string comment
    +DateTime createdAt
    +DateTime updatedAt
    +submit()
    +update()
    +delete()
}

class Amenity {
    +UUID id
    +string name
    +string description
    +DateTime createdAt
    +DateTime updatedAt
    +add()
    +update()
    +delete()
}

User --> Place : owns
User --> Review : writes
Place --> Review : has
Place --> Amenity : has many