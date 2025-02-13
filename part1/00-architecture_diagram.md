### High-Level Architecture - classDiagram

````mermaid
classDiagram
class Presentation {
    +Services
    +API endpoints
}
class BusinessLogic {
    <<Core Models>>
    +User
    +Place
    +Review
    +Amenity
}
class Persistence {
    +Database
    +Repository
    +data_save()
    +data_fetch()
}

Presentation --> BusinessLogic : Facade Pattern
BusinessLogic --> Persistence : Database Access