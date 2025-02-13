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
    PresentationLayer-->>User: Registration success message

    User->>PresentationLayer: Create Place
    PresentationLayer->>BusinessLogicLayer: Validate place data
    BusinessLogicLayer->>PersistenceLayer: Insert place data
    PersistenceLayer-->>BusinessLogicLayer: Confirmation
    BusinessLogicLayer-->>PresentationLayer: Response
    PresentationLayer-->>User: Place creation success

    User->>PresentationLayer: Submit Review
    PresentationLayer->>BusinessLogicLayer: Validate review data
    BusinessLogicLayer->>PersistenceLayer: Save review data
    PersistenceLayer-->>BusinessLogicLayer: Confirmation
    BusinessLogicLayer-->>PresentationLayer: Response
    PresentationLayer-->>User: Review submitted

    User->>PresentationLayer: Request List of Places
    PresentationLayer->>BusinessLogicLayer: Fetch places
    BusinessLogicLayer->>PersistenceLayer: Retrieve place data
    PersistenceLayer-->>BusinessLogicLayer: Places data
    BusinessLogicLayer-->>PresentationLayer: List of Places
    PresentationLayer-->>User: Display list of places
