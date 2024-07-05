import sqlite3
import random
from datetime import datetime, timedelta

def generate_random_data(num_records):
    names = [
        'John Doe', 'Jane Smith', 'Alice Johnson', 'Michael Brown', 'Chloe Davis',
        'Lucas Miller', 'Emma Wilson', 'Oliver Moore', 'Sophia Young', 'Ethan Johnson',
        'Mia Williams', 'Noah Jones', 'Isabella Taylor', 'William White', 'Ava Thompson',
        'Matthew Harris', 'Amelia Martin', 'James Lee', 'Charlotte Hall', 'Alexander Allen',
        'Harper Young', 'Elijah Scott', 'Isabelle Edwards', 'Jack Wright', 'Lily King',
        'Benjamin Moore', 'Zoe Miller', 'Logan Brown', 'Grace Davis', 'Ryan Wilson',
        'Jackson Wong', 'Ella Thompson', 'Henry Anderson', 'Scarlett Lee', 'David Martin',
        'Victoria Clark', 'Daniel Lewis', 'Abigail Walker', 'Mason Young', 'Hannah Hill',
        'Jacob Martinez', 'Sofia Wright', 'William Robinson', 'Grace Mitchell', 'James Harris'
    ]

    purposes = [
        'Will make a visit.', 'Scheduled appointment.', 'Delivery received.', 'Meeting with staff.',
        'Inspection visit.', 'Maintenance check.', 'Guest arrival.', 'Package pickup.',
        'Service repair.', 'Consultation meeting.', 'Training session.', 'Personal visit.',
        'Vendor visit.', 'Document submission.', 'Repair request.', 'Health checkup.',
        'Equipment setup.', 'Special event visit.', 'Emergency visit.', 'Other.'
    ]

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 7, 5)  # Latest date is July 05, 2024

    random_data = []
    for _ in range(num_records):
        visit_name = random.choice(names)
        res_id = random.randint(32, 76)  # Choose randomly from your resident IDs
        log_purpose = random.choice(purposes)
        log_day = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        login_time = datetime(log_day.year, log_day.month, log_day.day, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)).strftime('%H:%M:%S')
        logout_time = datetime(log_day.year, log_day.month, log_day.day, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)).strftime('%H:%M:%S')
        log_stat = random.choice([0, 1])
        sec_id = random.choice([1, 2])  # Choose randomly from your security IDs

        random_data.append((visit_name, res_id, log_purpose, log_day.strftime('%Y-%m-%d'), login_time, logout_time, log_stat, sec_id))

    return random_data

def update_visitor_data(num_records):
    conn = sqlite3.connect('visitor_attendance.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM visitor_data")

    new_data = generate_random_data(num_records)

    for data in new_data:
        cursor.execute("""
            INSERT INTO visitor_data (visit_name, res_id, log_purpose, log_day, login_time, logout_time, log_stat, sec_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)

    conn.commit()
    conn.close()

update_visitor_data(100)
