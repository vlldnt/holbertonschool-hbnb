# <img src="https://cdn.prod.website-files.com/6105315644a26f77912a1ada/63eea844ae4e3022154e2878_Holberton-p-800.png" width="150" /> - HbnB Project - C#25
The HBnB project in Holberton is a simplified full-stack clone of Airbnb, designed to cover backend development, database management, front-end integration, and deployment.

### 📘 [Part 1: UML Diagrams](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1)
We launched the development of the HBnB Evolution application by creating a detailed blueprint. This technical document compiles all essential diagrams and explanations, serving as a comprehensive guide to the system’s architecture, design, and implementation phases detailing the steps from the user to the database.


1. [The high-level architecture of the application](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1/00-architecture_diagram.md) with a package diagram that outlines the three layers and the use of the Facade Pattern.

2. [Detailed diagrams representing the business logic layer](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1/01-class_diagram.md) with a detailed class diagram illustrating key entities and their relationships.

3. [Sequence diagrams for key API interactions](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1/02-sequence_diagram.md) depicting critical operations such as :
    - [user registration](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1/02-detailed_sequence_diagrams/2-user_registration.md)
    - [place creation](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1/02-detailed_sequence_diagrams/2-place_creation.md)
    - [review submission](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1/02-detailed_sequence_diagrams/2-review_submission.md)
    - [fetching places](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part1/02-detailed_sequence_diagrams/2-place_fetching.md)

### ⚙️ [Part 2: Implementation of Business Logic and API Endpoints](https://github.com/vlldnt/holbertonschool-hbnb/blob/main/part2/hbnb)

This part is focused on creating a functional and scalable foundation for the application. You will be working on:

**Business Logic Layer:** Building the core models and logic that drive the application's functionality. This includes defining relationships, handling data validation, and managing interactions between different components.

**Presentation Layer:** Defining the services and API endpoints using Flask and flask-restx. You will structure the endpoints logically, ensuring clear paths and parameters for each operation.

0. _**Project Setup and Package Initialization:**_ Set up the project structure with Presentation, Business Logic, and Persistence layers, using in-memory storage and the Facade pattern.
1. _**Core Business Logic Classes:**_ Implement core business logic classes (User, Place, Review, Amenity) with attributes, relationships, and validations.
2. _**User Endpoints:**_ Develop API endpoints for user management (POST, GET, PUT) while ensuring sensitive data security.
3. _**Amenity Endpoints:**_ Implement API endpoints for managing amenities (POST, GET, PUT) via the Facade pattern.
4. _**Place Endpoints:**_ Create API endpoints for managing places (POST, GET, PUT) with attribute validation and integration with users and amenities.
5. _**Review Endpoints:**_ Develop API endpoints for managing reviews (POST, GET, PUT, DELETE) while maintaining associations with users and places.
6. _**Testing and Validation:**_ Perform validation, manual and automated testing using cURL and unittest/pytest, and document the results.





### 👤 Authors:
- [@Madjiguene Elodie Mbaye](https://github.com/Elodie-mbaye)
- [@Hamza Karkouch](https://github.com/SoliraZ)
- [@Adrien Vieilledent](https://github.com/vlldnt)

