# 🏠 HBnB Project – Documentation  

## 📌 Introduction  

### 🎯 Objective  
This document provides a detailed plan for the **HBnB Evolution** application. It consolidates all diagrams and explanatory notes into a comprehensive technical reference, guiding the implementation phases and clarifying the system's architecture and design.  

### 📍 Project Scope  
**HBnB Evolution** is a simplified application inspired by Airbnb that allows users to:  
✔️ Register 🔑  
✔️ Add properties 🏡  
✔️ Associate amenities 🏕️  
✔️ Submit reviews ⭐  

This documentation covers:  
📂 **General architecture** (package diagram)  
🛠 **Business model** (detailed class diagram)  
🔄 **API interactions** (sequence diagrams)  

---

## 🏗️ General Architecture  

### 🔍 **Package Diagram**  
The architecture follows a **layered model**, integrating the **facade pattern** to simplify interactions between components.  

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
````

📌 **The 3 main layers**:  

1️⃣ **Presentation Layer** 🎨  
- Manages the user interface and interactions.  
- Receives requests and returns responses after processing.  

2️⃣ **Business Logic Layer** ⚙️  
- Contains key models (**User, Place, Review, Amenity**).  
- Implements business rules and orchestrates operations.  
- Acts as a **facade** for communication with the persistence layer.  

3️⃣ **Persistence Layer** 🗄️  
- Manages the database and CRUD operations.  
- Structures data to ensure integrity and consistency.  

### High-Level Architecture - classDiagram

Presentation --> BusinessLogic : Facade Pattern
BusinessLogic --> Persistence : Database Access

The **facade pattern** ensures that the **Presentation Layer** never interacts directly with the database, ensuring better modularity and maintainability.  

---

## 🛠️ Business Logic Layer  


### 📌 **Class Diagram**  
The core of the application relies on several **key entities**:  

### High-Level Architecture - classDiagram

```mermaid
classDiagram
class User {
  #UID: String
  +user_first_name: String
  +user_last_name: String
  +user_email: String
  -user_password: String
  -user_administrator: boolean
  +user_register()
  +user_update()
  +user_delete()
}
class Place {
  #UID: String
  +place_title: String
  +place_description: String
  +place_price: int
  -place_latitude: float
  -place_longitude: float
  #place_owner: String
  +place_create()
  +place_update()
  +place_delete()
  +place_fetch()
}
class Review {
  #UID: String
  +review_rating: int
  +review_comment: String
  +review_create()
  +review_delete()
  +review_listed_by_place()
}
class Amenity {
  #UID: String
  +amenity_name: String
  +amenity_description: String
  +amenity_create()
  +amenity_delete()
  +amenity_listed()
}
Place --> Amenity : has
User --> Place : owns
User --> Place : searches
User --> Review : makes
Place --> Review : has

```

- **User** 👤  
  📌 `id`, `first_name`, `last_name`, `email`, `password`  
  🛠 `register()`, `update_profile()`, `delete_account()`  

- **Place** 🏡  
  📌 `id`, `title`, `description`, `price`, `latitude`, `longitude`, `createdAt`, `updatedAt`  
  🛠 `create()`, `update()`, `delete()`  

- **Review** ⭐  
  📌 `id`, `user_id`, `place_id`, `rating`, `comment`, `createdAt`, `updatedAt`  
  🛠 `submit()`, `update()`, `delete()`  

- **Amenity** 🏕️  
  📌 `id`, `name`, `description`, `createdAt`, `updatedAt`  
  🛠 `add()`, `update()`, `delete()`  

### 🔗 **Entity Relationships**  
✔️ **A user** can own multiple **places** and leave multiple **reviews**.  
✔️ **A place** can receive multiple **reviews** and be associated with multiple **amenities**.  

The architecture of the business logic layer ensures **consistency, scalability, and modularity**.  

---

## 🔄 API Interaction Flow  

### 📊 **Sequence Diagrams for API calls**  

````mermaid
sequenceDiagram
  participant User
  participant PresentationLayer
  participant BusinessLogicLayer
  participant PersistenceLayer

  User->>PresentationLayer: Register User
  PresentationLayer->>BusinessLogicLayer: Validate and transform data
  BusinessLogicLayer->>PersistenceLayer: Store user data
  PersistenceLayer-->>BusinessLogicLayer: Confirmation
  BusinessLogicLayer-->>PresentationLayer: Response
  PresentationLayer-->>User: Registration success msg/error msg

  User->>PresentationLayer: Create Place
  PresentationLayer->>BusinessLogicLayer: Validate place data
  BusinessLogicLayer->>PersistenceLayer: Insert place data
  PersistenceLayer-->>BusinessLogicLayer: Confirmation
  BusinessLogicLayer-->>PresentationLayer: Response
  PresentationLayer-->>User: Place creation success/failed

  User->>PresentationLayer: Submit Review
  PresentationLayer->>BusinessLogicLayer: Validate review data
  BusinessLogicLayer->>PersistenceLayer: Save review data
  PersistenceLayer-->>BusinessLogicLayer: Confirmation
  BusinessLogicLayer-->>PresentationLayer: Response
  PresentationLayer-->>User: Review submitted/failed

  User->>PresentationLayer: Request List of Places
  PresentationLayer->>BusinessLogicLayer: Fetch places
  BusinessLogicLayer->>PersistenceLayer: Retrieve place data
  PersistenceLayer-->>BusinessLogicLayer: Places data
  BusinessLogicLayer-->>PresentationLayer: List of Places
  PresentationLayer-->>User: Display list of places
````

#### 📝 **1. User Registration**  
1️⃣ The user sends their information (**name, email, password**) to the **Presentation Layer**.  
2️⃣ It validates and forwards them to the **Business Logic Layer**.  
3️⃣ After validation, the data is stored via the **Persistence Layer**.  
4️⃣ A success or failure response is returned.  

#### 🏡 **2. Place Creation**  
1️⃣ The user submits a creation request (**title, description, etc.**).  
2️⃣ The **Presentation Layer** forwards the request to the **Business Logic Layer**.  
3️⃣ After validation, the data is inserted via the **Persistence Layer**.  
4️⃣ A confirmation is returned.  

#### ⭐ **3. Review Submission**  
1️⃣ The user wants to leave a review for a place.  
2️⃣ The **Presentation Layer** sends the details (**rating, comment, etc.**) to the **Business Logic Layer**.  
3️⃣ The review is stored via the **Persistence Layer**, and a response is returned.  

#### 📍 **4. Retrieving Available Places**  
1️⃣ The user requests the list of available places.  
2️⃣ The **Presentation Layer** queries the **Business Logic Layer**, which consults the **Persistence Layer**.  
3️⃣ The results are returned and displayed to the user.  

---

## 📌 Conclusion  

This document is a **comprehensive technical guide** for **HBnB Evolution**. It provides:  

📂 **An overview of the architecture** and the **facade pattern** 🏗️  
📊 **A structured business model** with a class diagram 🔍  
🔄 **A detailed API interaction schema** outlining the main operations  

🔹 **Readability and professionalism** ensure a clear understanding for developers throughout the implementation.  
🔹 This document will evolve to reflect project updates.  
