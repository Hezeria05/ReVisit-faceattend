import mysql.connector
from datetime import datetime, timedelta

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="visitor_attendance"
    )



def register_security_admin(name, username, password, shift):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        query_insert = "INSERT INTO security_admin (sec_name, sec_username, sec_password, shift_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(query_insert, (name, username, password, shift))
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
