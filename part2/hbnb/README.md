# HBnB - Project Setup and Package Initialization
This project is the initial setup for the **HBnB** application, an Airbnb-like platform designed for managing users, places, reviews, and amenities. This README describes the structure of the project and provides instructions for installing dependencies and running the application locally.

## :pencil2: The Project Directory Structure:<br>
```txt
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── tests/
│   ├── test_users.py
│   ├── test_amenities.py
│   ├── test_places.py
│   ├── test_reviews.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
├── Testing.md

```
<br>

**:red_circle:run.py**<br>
The entry point for running the Flask application.<br>
**:red_circle:config.py**<br>
It is used for configuring environment variables and application settings.<br>
**:red_circle:requirements.txt**<br>
List all the Python packages needed for the project.<br>
**:red_circle:README.md**<br>
It explains the project overview and how to use it.<br>
**:red_circle:Testing.md**<br>
Testing Process Documentation<br>


## :file_folder: app/ 

Main application package that organizes the system into modular components.<br>
**:small_orange_diamond:app/\_\_init\_\_.py<br>**
Initializes the app package and typically contains the factory function for creating the Flask application.<br>
<br>

## :file_folder: app/api/ 
This package defines the RESTful API endpoints for the HBnB application.<br>
**:small_orange_diamond: app/api/\_\_init\_\_.py<br>**
Initializes the api package.<br>
 **:small_blue_diamond: app/api/v1<br>**
Contains version 1 of the API routes. This modular versioning allows the project to support future upgrades without breaking existing clients.<br>
**:small_blue_diamond: app/api/v1/\_\_init\_\_.py<br>**
 Initializes the v1 API package. <br>
 It is used to group and register all v1 API blueprints into the main app.
<br>
**:small_blue_diamond:app/api/v1/users.py<br>**
Defines all API routes related to User resources.<br>
**:small_blue_diamond:app/api/v1/places.py<br>**
Defines API routes related to Place resources.<br>
**:small_blue_diamond:app/api/v1/reviews.py<br>**
Defines routes for handling User Reviews.<br>
**:small_blue_diamond:app/api/v1/amenities.py<br>**
Defines API routes for Amenity resources.<br>
<br>
## :file_folder: app/models/
This directory contains the core business logic classes (domain models) for the application. <br>These classes define the attributes, relationships, and validation logic for the key entities of the HBnB system.<br>
 **:small_orange_diamond:app/models/\_\_init\_\_.py<br>**
 Initializes the models package.<br>
  **:small_orange_diamond:app/models/user.py<br>**
  Defines the User class, representing a registered user in the system.<br>
  **:small_orange_diamond:app/models/place.py<br>**
  Defines the Place class, representing a property that users can list or book.<br>
   **:small_orange_diamond:app/models/review.py<br>**
   Defines the Review class, which stores feedback and ratings left by users on places.<br>
   **:small_orange_diamond:app/models/amenity.py<br>**
   Defines the Amenity class, representing features or services available in a place (e.g., "Wi-Fi", "Parking")<br>
## :file_folder: app/services/
This directory contains service-layer logic that acts as an intermediary between the API and the core business models.<br> It encapsulates application workflows and provides a clean, unified interface to perform business operations.<br>
 **:small_orange_diamond: app/services/\_\_init\_\_.py<br>**
 Initializes the services package.<br>
  **:small_orange_diamond: app/services/facade.py<br>**
 This file uses the Facade pattern to simplify complex operations by providing easy-to-use functions that handle multiple parts of the app behind the scenes.<br>
 ## :file_folder: app/persistence/
 This directory handles how data is saved and retrieved. <br>It separates data storage from business logic and can be updated later to use a database.<br>
 **:small_orange_diamond: app/persistence/\_\_init\_\_.py<br>**
 Marks persistence as a package so its code can be easily imported.
<br>
 **:small_orange_diamond:persistence/repository.py**
<br>
Provides functions to manage data (create, read, update, delete) without exposing storage details.<br>
## :file_folder: tests/<br>
This directory contains files with unit tests written for each entity<br>
**:small_orange_diamond:tests/test_users.py**<br>
**:small_orange_diamond:tests/test_amenities.py**<br>
**:small_orange_diamond:tests/test_places.py**<br>
**:small_orange_diamond:tests/test_reviews.py**<br>


## :key: Environment Requirements

 - Python 3.8+<br>
 - pip (Python package manager)<br>

## :bulb:Installation

 1. Clone the repository:<br>
 ``` 
    https://github.com/C4lice/holbertonschool-hbnb.git 
 ``` 

 2. Create a Virtual Environment (Recommended) <br>
```  
python3 -m venv venv  
source venv/bin/activate  
``` 
 3. Install Dependencies<br>
  ```
pip install -r requirements.txt
```

## :mag_right:Usage

 1. Run the application using this command<br>

 ```
 python run.py
 ```

 2. Open a browser and visit http://localhost:5000
# Business Logic Layer - Core Classes

This directory contains the core business logic classes for the HBnB application, implementing the main entities and their relationships. These classes form the foundation of the application's domain model, handling data attributes, validation, and interactions between objects.

---

## Overview

The core entities are:

- **User**  
- **Place**  
- **Review**  
- **Amenity**

Each class inherits from a common `BaseModel` that provides shared attributes such as UUID `id`, `created_at`, and `updated_at` timestamps.

UUIDs are used as unique identifiers to ensure global uniqueness, scalability, and improved security.

---

## Class Descriptions

### User

Represents a user of the application.

**Attributes:**

- `id` (str): UUID unique identifier.
- `first_name` (str): User's first name. Required, max length 50.
- `last_name` (str): User's last name. Required, max length 50.
- `email` (str): User's email address. Required, unique, validated format.
- `is_admin` (bool): Flag indicating admin privileges. Defaults to False.
- `created_at` (datetime): Creation timestamp.
- `updated_at` (datetime): Last update timestamp.

---

### Place

Represents a lodging place.

**Attributes:**

- `id` (str): UUID unique identifier.
- `title` (str): Title of the place. Required, max length 100.
- `description` (str): Optional detailed description.
- `price` (float): Price per night. Must be positive.
- `latitude` (float): Geographic latitude (-90 to 90).
- `longitude` (float): Geographic longitude (-180 to 180).
- `owner` (User): Reference to the User who owns the place. Must exist.
- `created_at` (datetime): Creation timestamp.
- `updated_at` (datetime): Last update timestamp.
- `reviews` (list[Review]): List of associated reviews.
- `amenities` (list[Amenity]): List of associated amenities.

**Methods:**

- `add_review(review)`: Add a Review instance to the place.
- `add_amenity(amenity)`: Add an Amenity instance to the place.

---

### Review

Represents a review for a place.

**Attributes:**

- `id` (str): UUID unique identifier.
- `text` (str): Content of the review. Required.
- `rating` (int): Rating between 1 and 5 inclusive.
- `place` (Place): Reference to the reviewed Place. Must exist.
- `user` (User): Reference to the User who wrote the review. Must exist.
- `created_at` (datetime): Creation timestamp.
- `updated_at` (datetime): Last update timestamp.

---

### Amenity

Represents an amenity offered at a place.

**Attributes:**

- `id` (str): UUID unique identifier.
- `name` (str): Name of the amenity (e.g., "Wi-Fi"). Required, max length 50.
- `created_at` (datetime): Creation timestamp.
- `updated_at` (datetime): Last update timestamp.

---

## Implementation Details

- All classes inherit from `BaseModel` which handles UUID generation, timestamps, and attribute updating.
- Validation is performed on attribute setters to ensure data integrity (e.g., email format, string length, rating ranges).
- Relationships are maintained via object references and lists.
- Timestamps are updated whenever an object is modified.
- The many-to-many relationship between `Place` and `Amenity` is managed via a list of amenity instances in the `Place` class.

---
## Authors
[Laura Aupetit](https://github.com/C4lice)<br>
[Emi Hatano](https://github.com/Emi-H106)
