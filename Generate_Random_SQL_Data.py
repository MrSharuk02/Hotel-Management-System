import mysql.connector
from faker import Faker
import random

# Instantiate Faker object with Indian locale
fake = Faker('en_IN')

# Function to connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sharfoddin@28",
        database="hotelmanagementsystem"
    )

# Function to generate fake customer data and insert into database
def generate_customers(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    used_emails = set()
    
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        gender = random.choice(['Male', 'Female'])
        email = fake.email()
        
        # Ensure unique email addresses
        while email in used_emails:
            email = fake.email()
        used_emails.add(email)
        
        phone = fake.phone_number()
        address = fake.address().replace("\n", ", ")
        
        # SQL query to insert customer data into the database
        query = "INSERT INTO customers (first_name, last_name, gender, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, gender, email, phone, address))
    
    # Commit changes to the database
    conn.commit()
    cursor.close()
    conn.close()

# Function to generate fake room data and insert into database
def generate_rooms(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    room_types = ['Single', 'Double', 'Suite', 'Deluxe']
    used_room_numbers = set()
    
    for _ in range(n):
        room_number = fake.bothify(text='###')
        
        # Ensure unique room numbers
        while room_number in used_room_numbers:
            room_number = fake.bothify(text='###')
        used_room_numbers.add(room_number)
        
        room_type = random.choice(room_types)
        capacity = random.randint(1, 4)
        price_per_night = round(random.uniform(50.0, 500.0), 2)
        status = random.choice(['Available', 'Booked', 'Maintenance'])
        
        # SQL query to insert room data into the database
        query = "INSERT INTO rooms (room_number, room_type, capacity, price_per_night, status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (room_number, room_type, capacity, price_per_night, status))
    
    # Commit changes to the database
    conn.commit()
    cursor.close()
    conn.close()

# Function to generate fake booking data and insert into database
def generate_bookings(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    for _ in range(n):
        customer_id = random.randint(1, 100)
        room_id = random.randint(1, 100)
        check_in_date = fake.date_between(start_date='-1y', end_date='today')
        check_out_date = fake.date_between(start_date=check_in_date, end_date='+15d')
        total_amount = round(random.uniform(100.0, 5000.0), 2)
        booking_status = random.choice(['Confirmed', 'Cancelled', 'Completed'])
        
        # SQL query to insert booking data into the database
        query = "INSERT INTO bookings (customer_id, room_id, check_in_date, check_out_date, total_amount, booking_status) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (customer_id, room_id, check_in_date, check_out_date, total_amount, booking_status))
    
    # Commit changes to the database
    conn.commit()
    cursor.close()
    conn.close()

# Function to generate fake payment data and insert into database
def generate_payments(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    payment_methods = ['Credit Card', 'Debit Card', 'Cash', 'Online']
    for _ in range(n):
        booking_id = random.randint(1, 100)
        payment_date = fake.date_between(start_date='-1y', end_date='today')
        amount = round(random.uniform(100.0, 5000.0), 2)
        payment_method = random.choice(payment_methods)
        payment_status = random.choice(['Pending', 'Completed', 'Failed'])
        
        # SQL query to insert payment data into the database
        query = "INSERT INTO payments (booking_id, payment_date, amount, payment_method, payment_status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (booking_id, payment_date, amount, payment_method, payment_status))
    
    # Commit changes to the database
    conn.commit()
    cursor.close()
    conn.close()

# Function to generate fake staff data and insert into database
def generate_staff(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    positions = ['Manager', 'Receptionist', 'Housekeeping', 'Chef']
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        gender = random.choice(['Male', 'Female'])
        position = random.choice(positions)
        hire_date = fake.date_between(start_date='-3y', end_date='today')
        salary = round(random.uniform(15000.0, 80000.0), 2)
        
        # SQL query to insert staff data into the database
        query = "INSERT INTO staff (first_name, last_name, gender, position, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, gender, position, hire_date, salary))
    
    # Commit changes to the database
    conn.commit()
    cursor.close()
    conn.close()

# Function to generate fake service data and insert into database
def generate_services(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    service_names = ['Spa', 'Gym', 'Breakfast', 'Airport Shuttle']
    for _ in range(n):
        service_name = random.choice(service_names)
        description = fake.sentence(nb_words=10)
        price = round(random.uniform(50.0, 1000.0), 2)
        service_status = random.choice(['Available', 'Unavailable'])
        
        # SQL query to insert service data into the database
        query = "INSERT INTO services (service_name, description, price, service_status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (service_name, description, price, service_status))
    
    # Commit changes to the database
    conn.commit()
    cursor.close()
    conn.close()

# Main function to generate fake data for all tables
if __name__ == "__main__":
    # Generate fake data for each table
    generate_customers(1000)
    generate_rooms(1000)
    generate_bookings(1000)
    generate_payments(1000)
    generate_staff(1000)
    generate_services(1000)
