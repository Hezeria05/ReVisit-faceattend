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

def insert_visitor_data(visit_name, res_id, log_purpose, sec_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        # Prepare the current date and time
        current_datetime = datetime.now()
        log_day = current_datetime.date()
        login_time = current_datetime.strftime('%H:%M:%S')

        # Prepare SQL query to insert data
        query_insert = """
        INSERT INTO visitor_data (
            visit_name,
            res_id,
            log_purpose,
            log_day,
            login_time,
            log_stat,
            sec_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        # Values to be inserted
        data_tuple = (visit_name, res_id, log_purpose, log_day, login_time, True, sec_id)

        # Execute the query
        cursor.execute(query_insert, data_tuple)

        # Commit changes
        conn.commit()
        print("Visitor data successfully inserted.")
        success = True
    except mysql.connector.Error as err:
        print(f"Failed to insert visitor data: {err}")
        success = False
    finally:
        cursor.close()
        conn.close()
    return success


def logout_visitor(visit_name, sec_id, Existinglabel):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        query_check = """
        SELECT login_time, logout_time FROM visitor_data WHERE visit_name = %s AND sec_id = %s ORDER BY log_day DESC, login_time DESC LIMIT 1
        """
        cursor.execute(query_check, (visit_name, sec_id))
        result = cursor.fetchone()

        if result:
            login_time, logout_time = result
            if login_time is not None and logout_time is None:
                current_datetime = datetime.now()
                logout_time = current_datetime.strftime('%H:%M:%S')
                log_day = current_datetime.date()

                query_update = """
                UPDATE visitor_data SET logout_time = %s, log_stat = %s, log_day = %s WHERE visit_name = %s AND login_time = %s AND sec_id = %s
                """
                cursor.execute(query_update, (logout_time, False, log_day, visit_name, login_time, sec_id))
                conn.commit()
                return True  # Logout was successful
            elif logout_time is not None:
                Existinglabel.configure(text='Logged out already.')
            else:
                Existinglabel.configure(text='Log in first.')
        else:
            Existinglabel.configure(text='Visitor not found or never logged in.')
        return False  # Logout was not successful

    except mysql.connector.Error as err:
        Existinglabel.configure(text=f"Failed to update visitor data: {err}")
        return False  # Logout failed due to an error
    finally:
        cursor.close()
        conn.close()
