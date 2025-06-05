# Detailed Class Diagram for Business Logic Layer

## 📌Overview
This class diagram represents the structure and relationships of the four core entities in the business logic layer of the HBnB application.


## **Class Diagram (Mermaid.js Representation)**
```mermaid
classDiagram
class User {
    +UUID id
    +string first_name
    +string last_name
    +string email
    +string password
    +bool is_admin
    +datetime created_at
    +datetime updated_at
    +register()
    +update_profile()
    +delete_account()
}
class Place {
    +UUID id
    +string title
    +string description
    +float price
    +float latitude
    +float longitude
    +User owner
    +List amenities
    +datetime created_at
    +datetime updated_at
    +create_place()
    +update_place()
    +delete_place()
}
class Review {
    +UUID id
    +User user
    +Place place
    +int rating
    +string comment
    +datetime created_at
    +datetime updated_at
    +create_review()
    +update_review()
    +delete_review()
}
class Amenity {
    +UUID id
    +string name
    +string description
    +datetime created_at
    +datetime updated_at
    +create_amenity()
    +update_amenity()
    +delete_amenity()
}
User "1" --> "*" Place : owns
Place "*" --> "*" Amenity : contains
User "1" --> "*" Review : writes
Place "1" --> "*" Review : has
```


## 🔍Explanatory Notes

## Entities
#### 👨 User
A user has a first name, last name, email, and password, with an optional administrator status. Users can register, update their profile, and be deleted.

#### 🏠 Place
A place has a title, description, price, latitude, and longitude, and is owned by a user. It can include multiple amenities and supports creation, update, deletion, and listing.

#### ✍️ Review
A review belongs to a specific user and place, containing a rating and comment. Reviews can be created, updated, deleted, and listed by place.

#### 🧴Amenity
An amenity has a name and description, and can be created, updated, deleted, and listed.

## Relationships
● User :left_right_arrow: Place<br>
One user can own multiple places, representing a one-to-many relationship.

● Place :left_right_arrow: Amenity<br>
A place can have multiple amenities, and each amenity can be shared by multiple places, forming a many-to-many relationship.

● User :left_right_arrow: Review<br>
One user can write multiple reviews, which is a one-to-many relationship.

● Place :left_right_arrow: Review<br>
 A place can have multiple reviews, also representing a one-to-many relationship.

## Conclusion
This class diagram provides a clear representation of the core entities and their relationships in the business logic layer of the HBnB application.<br>It establishes a solid foundation for implementing consistent and well-structured business rules throughout the system.
