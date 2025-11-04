#  Cultural Food Passport API (Backend)

This is the backend REST API for **Cultural Food Passport**, built with **Django REST Framework**.  
It provides endpoints for managing users, dishes, locations, and tags — with **JWT authentication** and a **PostgreSQL** database.

---

##  Overview

The backend handles:
- User registration, login, and JWT authentication  
- CRUD operations for Dishes, Tags, and Locations  
- Filtering dishes by tag or location  
- Secure access control with permissions  

---

##  Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django, Django REST Framework |
| Language | Python |
| Database | PostgreSQL |
| Authentication | JSON Web Token (JWT) |
| Testing | Django TestCase |
| Version Control | Git & GitHub |

---

##  Models & Relationships

| Model | Fields | Relationships |
|--------|---------|----------------|
| **User** | (built-in) | One user can create many dishes |
| **Dish** | name, origin, description, photo, user, tags | Belongs to one Location and one User; can have many Tags |
| **Location** | name, country_code | One location can have many dishes |
| **Tag** | name | A tag can belong to many dishes |

**Relationships Summary**
- User → Dish = One-to-Many  
- Dish → Location = Many-to-One  
- Dish ↔ Tag = Many-to-Many  

---


| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `//` | Welcome message |
| GET | `/dishes/` | List all dishes for logged-in user |
| POST | `/dishes/` | Create a new dish |
| GET | `/dishes/:dish_id/` | Retrieve details for a specific dish |
| PUT | `/dishes/:dish_id/` | Update a dish |
| DELETE | `/dishes/:dish_id/` | Delete a dish |
| GET | `/locations/` | List all locations |
| POST | `/locations/` | Create a location |
| GET | `/locations/:location_id/dishes/` | Filter dishes by location |
| GET | `/tags/` | List all tags |
| POST | `/tags/` | Create a tag |
| GET | `/tags/:tag_id/` | Retrieve a specific tag |
| PUT | `/tags/:tag_id/` | Update a tag |
| DELETE | `/tags/:tag_id/` | Delete a tag |
| GET | `/tags/:tag_name/dishes/` | Filter dishes by tag |
| POST | `/user/signup/` | Register a new user |
| POST | `/user/login/` | Login user and return JWT token |
| GET | `/user/verify/` | Verify JWT token and return user data |

---

<!-- git clone <backend-repo-url>
cd backend-finelproject -->


## Future Improvements / Icebox Features

Add a commenting system where users can interact with dishes posted by others — similar to comment sections on social platforms or Google Maps.

Add likes and reactions for each dish to increase community engagement.

Integrate geo-location features to detect the user’s location and show nearby restaurants offering similar dishes from different countries.

Create a social feed where users can explore and discuss international cuisines shared by the community.

Add AI-based recommendations suggesting dishes or restaurants based on user interests and location.

