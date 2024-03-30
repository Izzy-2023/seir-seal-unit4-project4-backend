# Product Requirements Documentation

**Summary**
| Field | Detail |
|-------|--------|
| Project Name | Tech Consulting Application|
| Description | Tech consulting platform to browse for services and book appointments.  |
| Developers | Izzy Zinxhirija |
| Live Website |  |
| Repo | https://github.com/Izzy-2023/seir-seal-unit4-project4-backend |

## Problem Being Solved and Target Market

The tech consulting website provides a platform for customers to explore and book various consulting services offered. Customers can browse through a list of services, view detailed descriptions, and book appointments for specific services. The website also includes user authentication for customers to manage their bookings and an admin dashboard for managing services and appointments.

## Dependencies

List of dependecies using the application.

- Django Rest Framework
- dj-database-ur
- psycopg2-binary
- django-environ
- django.contrib.auth

## ERD (Entity Relationship Diagram)

# Service
| Field Name | Type	| Description |
| ---------- | ---- | ----------- |
| id | Integer | Primary key |
| name | CharField | Name of the service |
| description |	TextField |	Description of the service| 
| price	| DecimalField | Price of the service |
| duration |	Duration | Field	| Duration of the service |

# Appointment
| Field Name | Type	| Description |
| ---------- | ---- | ----------- |
| id | Integer | Primary key |
| service_id | ForeignKEy | Foreign key to the service for which the appointment is made |
| customer_name |	CharField |	Name of the customer booking the appointment| 
| customer_email	| EmailField | Email of the customer booking the appointment |
| appointment_date |	DateTimeField	| Date and time of the appointment |
| status | CharField	| Status of the appointment |

# User
| Field Name | Type	| Description |
| ---------- | ---- | ----------- |
| id | Integer | Primary key |
| username | CharField | Username of the user |
| email |	EmailField |	Email of the user| 
| password	| CharField | Password of the user |
| is_admin |	BooleanField	| Flag indicating if the user is an admin |

## Route Tables

|Route Name | Endpoint | Method | Description |
|---------- | -------- | ------ | ----------- |
| Home	| /home/ | GET	| Displays a list of consulting services |
| Service Detail |	/services/:id	| GET	| Displays details of a specific service |
| Book Appointment Form	| /services/:id/book | GET |	Form to book an appointment for a service |
|              |          | POST	| Submits the appointment booking form |
| Confirmation |	/confirmation	|GET	| Confirmation page after booking appointment |
| Login	| /login	| GET	| Login page for customers |
|        |        | POST |	Submits the login form |
| Register | /register |	GET |	Registration page for new customers |
|        |            | POST | Submits the registration form |
| Profile	| /profile | GET | User profile page |
| Admin Dashboard	| /admin/dashboard | GET | Dashboard for admin to manage services |
| Admin Services	| /admin/services |	GET |	Displays a list of services for admin |
|         |            |  POST	| Creates a new service |
|         | /admin/services/:id |	GET	| Displays details of a specific service |
|         | /admin/services/:id | PUT |	Updates a service |
|         | /admin/services/:id | DELETE |	Deletes a service |
| Admin Appointments	| /admin/appointments |	GET	| Displays a list of appointments for admin |
|         | /admin/appointments/:id |	GET |	Displays details of a specific appointment |
|         | /admin/appointments/:id | PUT	| Updates an appointment | 
|         | /admin/appointments/:id | DELETE | Deletes an appointment|

![Mockups]

### Services Page
(https://i.imgur.com/NgG4TxO.png))
