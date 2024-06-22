import sqlite3

def create_database():
    conn = sqlite3.connect('visitor_attendance.db')
    cursor = conn.cursor()

    # Create security_admin table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS security_admin (
        sec_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sec_name TEXT NOT NULL,
        sec_username TEXT NOT NULL,
        sec_password TEXT NOT NULL
    )
    ''')

    # Create visitor_data table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitor_data (
        visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        visit_name TEXT NOT NULL,
        res_id INTEGER,
        log_purpose TEXT,
        log_day DATE,
        login_time TIME,
        logout_time TIME,
        log_stat BOOLEAN,
        sec_id INTEGER,
        FOREIGN KEY(sec_id) REFERENCES security_admin(sec_id)
    )
    ''')

    # Create resident_data table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS resident_data (
        res_id INTEGER PRIMARY KEY AUTOINCREMENT,
        res_name TEXT NOT NULL,
        res_address TEXT NOT NULL,
        res_phonenumber TEXT NOT NULL
    )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the function to create the database and tables
create_database()