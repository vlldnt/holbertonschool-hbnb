### High-Level Architechture 
1. Presentation Layer
2. Buissness Layer
3. Persistance Layer

````mermaid
classDiagram
class Presentation {
    +Services
    +API endpoints
}
class Business Logic {
    <<Core Models>>
    +User
    +Place
    +Review
    +Amenity
    +user_management()
    +place_management()
    +review_management()
    +amenity_management()

}
class Persistence {
    +Database
    +Repository
    +data_save()
    +data_fetch()
}

Presentation --> Business Logic : Facade Pattern
Business Logic --> Persistence : Database Acces
```

### High-Level Architechture 
    1. Presentation Layer
    2. Buissness Layer
    3. Persistance Layer