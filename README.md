# Hotel Management System

## Project Overview

The Hotel Management System is designed to manage various aspects of hotel operations, including customer management, room management, booking processes, staff management, payment handling, and service offerings. This system ensures efficient and smooth operations by providing an integrated platform for managing hotel-related data and transactions.

## Database Schema

### Tables and Their Contents

#### Customers

- **customer_id** (INT, Primary Key, Auto Increment): Unique identifier for each customer.
- **first_name** (VARCHAR(50)): First name of the customer.
- **last_name** (VARCHAR(50)): Last name of the customer.
- **age** (INT): Age of the customer.
- **gender** (ENUM('Male', 'Female')): Gender of the customer.
- **email** (VARCHAR(100), UNIQUE): Email address of the customer.
- **phone** (VARCHAR(15)): Contact phone number of the customer.
- **address** (VARCHAR(255)): Residential address of the customer.

#### Rooms

- **room_id** (INT, Primary Key, Auto Increment): Unique identifier for each room.
- **room_number** (VARCHAR(10), UNIQUE): Unique number assigned to each room.
- **room_type** (VARCHAR(50)): Type of the room (e.g., Single, Double, Suite).
- **capacity** (INT): Capacity of the room (number of guests it can accommodate).
- **price_per_night** (DECIMAL(10, 2)): Price per night for the room.
- **status** (ENUM('Available', 'Booked', 'Maintenance')): Current status of the room.

#### Staff

- **staff_id** (INT, Primary Key, Auto Increment): Unique identifier for each staff member.
- **first_name** (VARCHAR(50)): First name of the staff member.
- **last_name** (VARCHAR(50)): Last name of the staff member.
- **age** (INT): Age of the staff member.
- **gender** (ENUM('Male', 'Female')): Gender of the staff member.
- **position** (VARCHAR(50)): Job position of the staff member.
- **hire_date** (DATE): Date when the staff member was hired.
- **salary** (DECIMAL(10, 2)): Salary of the staff member.

#### Services

- **service_id** (INT, Primary Key, Auto Increment): Unique identifier for each service.
- **service_name** (VARCHAR(100)): Name of the service offered by the hotel.
- **description** (TEXT): Description of the service.
- **price** (DECIMAL(10, 2)): Price of the service.
- **service_status** (ENUM('Available', 'Unavailable')): Availability status of the service.

#### Bookings

- **booking_id** (INT, Primary Key, Auto Increment): Unique identifier for each booking.
- **customer_id** (INT, Foreign Key): Reference to the customer making the booking.
- **room_id** (INT, Foreign Key): Reference to the room being booked.
- **staff_id** (INT, Foreign Key): Reference to the staff member assisting with the booking.
- **check_in_date** (DATE): Check-in date for the booking.
- **check_out_date** (DATE): Check-out date for the booking.
- **total_amount** (DECIMAL(10, 2)): Total amount for the booking.
- **booking_status** (ENUM('Confirmed', 'Cancelled', 'Completed')): Status of the booking.

#### Payments

- **payment_id** (INT, Primary Key, Auto Increment): Unique identifier for each payment.
- **booking_id** (INT, Foreign Key): Reference to the associated booking.
- **payment_date** (DATE): Date of the payment.
- **amount** (DECIMAL(10, 2)): Amount paid.
- **payment_method** (ENUM('Credit Card', 'Debit Card', 'Cash', 'Online')): Method of payment.
- **payment_status** (ENUM('Pending', 'Completed', 'Failed')): Status of the payment.

#### Booking_Services

- **booking_service_id** (INT, Primary Key, Auto Increment): Unique identifier for each booking service.
- **booking_id** (INT, Foreign Key): Reference to the associated booking.
- **service_id** (INT, Foreign Key): Reference to the associated service.
- **quantity** (INT): Quantity of the service booked.
- **total_price** (DECIMAL(10, 2)): Total price for the services booked.

## Relationships Between Tables

- **Customers to Bookings**: One-to-Many (A customer can make multiple bookings)
- **Rooms to Bookings**: One-to-Many (A room can be associated with multiple bookings over time)
- **Staff to Bookings**: One-to-Many (A staff member can assist with multiple bookings)
- **Bookings to Payments**: One-to-Many (A booking can have multiple payments)
- **Bookings to Booking_Services**: One-to-Many (A booking can include multiple services)
- **Services to Booking_Services**: One-to-Many (A service can be included in multiple bookings)

## Outcomes and Insights

The Hotel Management System enables efficient management and analysis of various hotel operations. By utilizing the system, we can achieve the following outcomes:

- **Improved Customer Management**: Maintain detailed records of customers, including personal information, booking history, and contact details.
- **Efficient Room Management**: Track room availability, types, pricing, and maintenance status to optimize room allocation and management.
- **Streamlined Booking Process**: Facilitate seamless booking operations, from check-in to check-out, and manage booking statuses effectively.
- **Effective Staff Management**: Monitor staff details, positions, and performance, ensuring proper allocation of staff resources.
- **Comprehensive Payment Handling**: Manage payments efficiently, tracking payment methods, statuses, and amounts to ensure accurate financial records.
- **Enhanced Service Management**: Offer and manage a variety of services, tracking their availability, pricing, and usage to improve customer satisfaction.
- **Data Analysis and Insights**: Analyze data to uncover trends, such as booking patterns, revenue trends, and customer demographics, aiding in strategic decision-making.

By leveraging these capabilities, the Hotel Management System enhances operational efficiency, customer satisfaction, and financial performance of the hotel.
