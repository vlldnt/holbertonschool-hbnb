````mermaid
classDiagram
class Presentation {
    +Services
    +API
}
class Business Logic {
    <<Core Models>>
    +User
    +Place
    +Review
    +Amenity
}
class Persistence {
    +Database
}

Presentation ..> Business Logic
Business Logic ..> Persistence
```