# Product Requirements Documentation

**Summary**
| Field | Detail |
|-------|--------|
| Project Name | I-Commerce Application|
| Description | Ecommerce platform to browse products and place orders.  |
| Developers | Izzy Zinxhirija |
| Live Website |  |
| Repo | https://github.com/Izzy-2023/seir-seal-unit4-project4-backend |

## Problem Being Solved and Target Market

The ecommerce app is a platform that allows users to browse, purchase, and manage products online. It offers a user-friendly interface for customers to view products, add them to a shopping cart, and securely complete transactions. The app also provides administrative tools for managing inventory, processing orders, and analyzing sales data.

## Dependencies

List of dependecies using the application.

- Django Rest Framework
- dj-database-ur
- psycopg2-binary
- django-environ
- Users can see all their items on the dashboard
- Users can update items
- User can delete items

## ERD (Entity Relationship Diagram)

| Field Name | Type | Description |
| ---------- | ---- | ----------- |
| id | Integer | Primary key |
| entity_type | CharField | Type of entity |
| name | CharField | Name of the entity |
| description | TextField | Description of the entity |
| price | DecimalField | Price of the entity (for products and order items) |
| image_url | URLField | URL of the image (for products) |
| total_price | DecimalField | Total price of the order (for orders) | 
| created_at | DateTimeField | Date and time when the entity was created | 
| user_id |	IntegerField | ID of the user (for orders and order items) | 
| quantity | IntegerField | Quantity of the entity (for order items) |
| username | CharField	| Username of the user (for users) |
| email	| EmailField | Email of the user (for users) |
| password | CharField | Password of the user (for users) |
| is_admin | BooleanField | Indicates if the user is an admin (for users) |

## Route Tables

|Route Name | Endpoint | Method | Description |
|---------- | -------- | ------ | ----------- |
| List Products | /products/ | GET | Retrieve a list of all products |
| Create Product | /products/ |	POST | Create a new product |
| Retrieve Product | /products/{id}/ | GET | Retrieve details of a specific product |
| Update Product | /products/{id}/ | PUT | Update details of a specific product |
| Delete Product | /products/{id}/ | DELETE	| Delete a specific product |
| List Orders | /orders/ | GET | Retrieve a list of all orders |
| Create Order | /orders/ | POST | Create a new order | 
| Retrieve Order | /orders/{id}/ | GET | Retrieve details of a specific order | 
| Update Order | /orders/{id}/ | PUT | Update details of a specific order |
| Delete Order | /orders/{id}/ | DELETE	| Delete a specific order |
| Signup | /auth/signup | POST |creates new user account returns user JSON | 
| Login | /auth/login | POST |logs in user and returns user JSON |


