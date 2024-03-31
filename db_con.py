import mysql.connector
from datetime import datetime, timedelta

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="visitor_attendance"
    )

def login_attendance(name, logout=False):
    conn = connect_to_database()
    cursor = conn.cursor()

    if not logout:
        # Check if the name exists in the login table
        query_check = "SELECT COUNT(*) FROM login WHERE v_name = %s"
        cursor.execute(query_check, (name,))
        count = cursor.fetchone()[0]

        if count > 0:
            print("Attendance already recorded for", name)
            cursor.close()
            conn.close()
            return False

        # Insert the attendance record
        query_insert = "INSERT INTO login (v_name, timestamp) VALUES (%s, NOW())"
        success_message = "Attendance recorded for"
    else:
        # First, ensure the name exists in the login table and hasn't logged out yet
        query_check_login = "SELECT COUNT(*) FROM login WHERE v_name = %s"
        cursor.execute(query_check_login, (name,))
        if cursor.fetchone()[0] == 0:
            print("No login record found for", name)
            cursor.close()
            conn.close()
            return False

        # Check if the name already exists in the logout table
        query_check_logout = "SELECT COUNT(*) FROM logout WHERE v_name = %s"
        cursor.execute(query_check_logout, (name,))
        if cursor.fetchone()[0] > 0:
            print("Logout already recorded for", name)
            cursor.close()
            conn.close()
            return False

        # Insert the logout record
        query_insert = "INSERT INTO logout (v_name, timestamp) VALUES (%s, NOW())"
        success_message = "Logout recorded for"

    try:
        cursor.execute(query_insert, (name,))
        conn.commit()
        print(success_message, name)
        success = True
    except Exception as e:
        print(f"An error occurred: {e}")
        success = False
    finally:
        cursor.close()
        conn.close()

    return success


def register_security_admin(name, username, password):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        query_insert = "INSERT INTO security_admin (name, username, password) VALUES (%s, %s, %s)"
        cursor.execute(query_insert, (name, username, password))
        conn.commit()
        print(f"Successfully registered {name}.")
        success = True
    except mysql.connector.Error as err:
        print(f"Failed to insert into security_admin: {err}")
        success = False
    finally:
        cursor.close()
        conn.close()
    return success

def validate_login_credentials(username, password):
    conn = connect_to_database()
    cursor = conn.cursor()

    # This query should be adjusted to match the schema of your user or admin table
    query = "SELECT COUNT(*) FROM security_admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()[0] > 0  # True if a matching record was found
    cursor.close()
    conn.close()
    return result

# Now you can use this function in your login interface
