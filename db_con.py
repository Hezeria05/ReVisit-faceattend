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
    else:
        # Check if the name exists in the logout table
        query_check = "SELECT COUNT(*) FROM logout WHERE v_name = %s"
        cursor.execute(query_check, (name,))
        count = cursor.fetchone()[0]

        if count > 0:
            print("Logout already recorded for", name)
            cursor.close()
            conn.close()
            return False

        # Insert the logout record
        query_insert = "INSERT INTO logout (v_name, timestamp) VALUES (%s, NOW())"

    try:
        cursor.execute(query_insert, (name,))
        conn.commit()
        print("Attendance recorded for", name) if not logout else print("Logout recorded for", name)
        success = True
    except Exception as e:
        print(f"An error occurred: {e}")
        success = False
    finally:
        cursor.close()
        conn.close()

    return success
