import mysql.connector
from faker import Faker
import random

fake = Faker()

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sharfoddin@28",
        database="hotelmanagementsystem"
    )

def insert_customers(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    used_emails = set()
    
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(18, 75)
        gender = random.choice(['Male', 'Female'])
        email = fake.email()
        
        while email in used_emails:  # Ensure unique email
            email = fake.email()
        
        used_emails.add(email)
        
        phone = fake.phone_number()
        if len(phone) > 15:  # Ensure phone number fits in the database field
            phone = phone[:15]
        address = fake.address().replace("\n", ", ")
        
        query = "INSERT INTO customers (first_name, last_name, age, gender, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, age, gender, email, phone, address))
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_rooms(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    room_types = ['Single', 'Double', 'Suite', 'Deluxe']
    used_room_numbers = set()
    
    for _ in range(n):
        room_number = fake.bothify(text='###')
        
        while room_number in used_room_numbers:  # Ensure unique room number
            room_number = fake.bothify(text='###')
        
        used_room_numbers.add(room_number)
        
        room_type = random.choice(room_types)
        capacity = random.randint(1, 4)
        price_per_night = round(random.uniform(50.0, 500.0), 2)
        status = random.choice(['Available', 'Booked', 'Maintenance'])
        
        query = "INSERT INTO rooms (room_number, room_type, capacity, price_per_night, status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (room_number, room_type, capacity, price_per_night, status))
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_staff(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    positions = ['Manager', 'Receptionist', 'Housekeeping', 'Chef']
    
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(18, 65)
        gender = random.choice(['Male', 'Female'])
        position = random.choice(positions)
        hire_date = fake.date_between(start_date='-3y', end_date='today')
        salary = round(random.uniform(15000.0, 80000.0), 2)
        
        query = "INSERT INTO staff (first_name, last_name, age, gender, position, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, age, gender, position, hire_date, salary))
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_services(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    service_names = ['Spa', 'Gym', 'Breakfast', 'Airport Shuttle']
    
    for _ in range(n):
        service_name = random.choice(service_names)
        description = fake.sentence(nb_words=10)
        price = round(random.uniform(50.0, 1000.0), 2)
        service_status = random.choice(['Available', 'Unavailable'])
        
        query = "INSERT INTO services (service_name, description, price, service_status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (service_name, description, price, service_status))
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_bookings(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    for _ in range(n):
        customer_id = random.randint(1, 500)
        room_id = random.randint(1, 500)
        staff_id = random.randint(1, 500)
        check_in_date = fake.date_between(start_date='-1y', end_date='today')
        check_out_date = fake.date_between(start_date=check_in_date, end_date='+15d')
        total_amount = round(random.uniform(100.0, 5000.0), 2)
        booking_status = random.choice(['Confirmed', 'Cancelled', 'Completed'])
        
        query = "INSERT INTO bookings (customer_id, room_id, staff_id, check_in_date, check_out_date, total_amount, booking_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (customer_id, room_id, staff_id, check_in_date, check_out_date, total_amount, booking_status))
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_payments(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    payment_methods = ['Credit Card', 'Debit Card', 'Cash', 'Online']
    
    for _ in range(n):
        booking_id = random.randint(1, 500)
        payment_date = fake.date_between(start_date='-1y', end_date='today')
        amount = round(random.uniform(100.0, 5000.0), 2)
        payment_method = random.choice(payment_methods)
        payment_status = random.choice(['Pending', 'Completed', 'Failed'])
        
        query = "INSERT INTO payments (booking_id, payment_date, amount, payment_method, payment_status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (booking_id, payment_date, amount, payment_method, payment_status))
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_booking_services(n):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    for _ in range(n):
        booking_id = random.randint(1, 500)
        service_id = random.randint(1, 500)
        quantity = random.randint(1, 10)
        total_price = round(random.uniform(50.0, 500.0), 2) * quantity
        
        query = "INSERT INTO booking_services (booking_id, service_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (booking_id, service_id, quantity, total_price))
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_customers(500)
    insert_rooms(500)
    insert_staff(500)
    insert_services(500)
    insert_bookings(500)
    insert_payments(500)
    insert_booking_services(500)
