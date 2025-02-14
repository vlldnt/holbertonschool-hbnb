### HbnB - sequenceDiagram
```mermaid
sequenceDiagram
    participant User
    participant PresentationLayer
    participant BusinessLogicLayer
    participant PersistenceLayer
    alt register user
        User->>PresentationLayer: Register User
        PresentationLayer->>BusinessLogicLayer: Validate and transform data
        BusinessLogicLayer->>PersistenceLayer: Store user data
        PersistenceLayer-->>BusinessLogicLayer: Confirmation
        BusinessLogicLayer-->>PresentationLayer: Response
        PresentationLayer-->>User: Registration success msg/error msg
    end
    alt Create a place
        User->>PresentationLayer: Create Place
        PresentationLayer->>BusinessLogicLayer: Validate place data
        BusinessLogicLayer->>PersistenceLayer: Insert place data
        PersistenceLayer-->>BusinessLogicLayer: Confirmation
        BusinessLogicLayer-->>PresentationLayer: Response
        PresentationLayer-->>User: Place creation success/failed
    end
    alt Submit review
        User->>PresentationLayer: Submit Review
        PresentationLayer->>BusinessLogicLayer: Validate review data
        BusinessLogicLayer->>PersistenceLayer: Save review data
        PersistenceLayer-->>BusinessLogicLayer: Confirmation
        BusinessLogicLayer-->>PresentationLayer: Response
        PresentationLayer-->>User: Review submitted/failed
    end
    alt List of places
        User->>PresentationLayer: Request List of Places
        PresentationLayer->>BusinessLogicLayer: Fetch places
        BusinessLogicLayer->>PersistenceLayer: Retrieve place data
        PersistenceLayer-->>BusinessLogicLayer: Places data
        BusinessLogicLayer-->>PresentationLayer: List of Places
        PresentationLayer-->>User: Display list of places
    end