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
    +data_save()
    +data_fetch()
}

Presentation ..> Business Logic : Facade Pattern
Business Logic ..> Persistence
```

### High-Level Architechture 
    1. Presentation Layer
    2. Buissness Layer
    3. Persistance Layer