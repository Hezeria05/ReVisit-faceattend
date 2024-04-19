import mysql.connector
from datetime import datetime, timedelta


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="visitor_attendance"
    )

def login_visitor(pred_name, sec_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    now = datetime.now()
    shift_id = 1 if now.hour < 12 else 2

    try:
        # Check if the visitor has already logged in today without logging out
        cursor.execute("SELECT COUNT(*) FROM visitor_data WHERE visit_name = %s AND log_day = CURDATE() AND logout_time IS NULL", (pred_name,))
        if cursor.fetchone()[0] > 0:
            print(f"Visitor {pred_name} has already logged in today and hasn't logged out yet.")
            return
        
        # Additional validation: Check if the visitor already exists with a login_time for any day
        cursor.execute("SELECT COUNT(*) FROM visitor_data WHERE visit_name = %s AND login_time IS NOT NULL", (pred_name,))
        if cursor.fetchone()[0] > 0:
            print(f"Visitor {pred_name} already has a login record.")
            return
        
        # Insert new login record
        query = "INSERT INTO visitor_data (visit_name, log_day, login_time, sec_id, shift_id) VALUES (%s, CURDATE(), NOW(), %s, %s)"
        cursor.execute(query, (pred_name, sec_id, shift_id))
        conn.commit()
        print(f"Visitor {pred_name} logged in successfully.")
    except mysql.connector.Error as err:
        print(f"Error logging in visitor: {err}")
    finally:
        cursor.close()
        conn.close()

def logout_visitor(pred_name):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        # Check if the visitor exists and has logged in but not logged out
        cursor.execute("""
            SELECT COUNT(*)
            FROM visitor_data
            WHERE visit_name = %s
            AND login_time IS NOT NULL
            AND logout_time IS NULL
            """, (pred_name,))
        count = cursor.fetchone()[0]

        if count == 0:
            # Check if the visitor has never logged in or already logged out
            cursor.execute("""
                SELECT COUNT(*)
                FROM visitor_data
                WHERE visit_name = %s
                AND login_time IS NOT NULL
                """, (pred_name,))
            logged_in_count = cursor.fetchone()[0]
            if logged_in_count == 0:
                print(f"Visitor {pred_name} has not logged in yet. Please log in first.")
            else:
                print(f"Visitor {pred_name} has already logged out.")
        else:
            # Update logout_time for the visitor
            cursor.execute("""
                UPDATE visitor_data
                SET logout_time = NOW()
                WHERE visit_name = %s
                AND logout_time IS NULL
                """, (pred_name,))
            conn.commit()
            print(f"Visitor {pred_name} logged out successfully.")
    except mysql.connector.Error as err:
        print(f"Error logging out visitor: {err}")
    finally:
        cursor.close()
        conn.close()



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

    # Adjust your SQL query to also select sec_id
    query = "SELECT sec_id, COUNT(*) FROM security_admin WHERE sec_username = %s AND sec_password = %s"
    cursor.execute(query, (username, password))

    # Fetch sec_id along with the result
    result, sec_id = cursor.fetchone()

    cursor.close()
    conn.close()
    return result > 0, sec_id


# Now you can use this function in your login interface
