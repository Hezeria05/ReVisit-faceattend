import mysql.connector
from datetime import datetime, timedelta


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="visitor_attendance"
    )





def register_security_admin(name, username, password):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        query_insert = "INSERT INTO security_admin (sec_name, sec_username, sec_password) VALUES (%s, %s, %s)"
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

    query = "SELECT sec_id, COUNT(*) FROM security_admin WHERE sec_username = %s AND sec_password = %s"
    cursor.execute(query, (username, password))

    # Fetch the result of the query
    result = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Check if result is not None
    if result is not None:
        # Extract sec_id and count from the result tuple
        sec_id, count = result
        # Return a boolean indicating success and sec_id
        return count > 0, sec_id
    else:
        # Handle the case when the query returns None (no result found)
        return False, None



# Now you can use this function in your login interface
