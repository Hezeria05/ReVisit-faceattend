import mysql.connector
from datetime import datetime, timedelta

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="visitor_attendance"
    )
#Registration of Account Page_____________________________________________________________________________________________________________
def register_security_admin(name, username, password, register_window, FnExistlabel, UnExistlabel):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        # Check if the full name already exists in the database
        cursor.execute("SELECT COUNT(*) FROM security_admin WHERE LOWER(sec_name) = LOWER(%s)", (name,))
        if cursor.fetchone()[0] > 0:
            FnExistlabel.configure(text='Name is already taken.')
            return False  # Early exit if the name exists

        # Check if the username already exists in the database
        cursor.execute("SELECT COUNT(*) FROM security_admin WHERE LOWER(sec_username) = LOWER(%s)", (username,))
        if cursor.fetchone()[0] > 0:
            UnExistlabel.configure(text='Username is already taken.')
            return False  # Early exit if the username exists

        # If neither name nor username is taken, proceed to insert
        query_insert = "INSERT INTO security_admin (sec_name, sec_username, sec_password) VALUES (%s, %s, %s)"
        cursor.execute(query_insert, (name, username, password))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Failed to insert into security_admin: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

#Sign In Page_____________________________________________________________________________________________________________
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

#Home Page_____________________________________________________________________________________________________________
def count_logged_in():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        today = datetime.now().date()
        cursor.execute("SELECT COUNT(*) FROM visitor_data WHERE log_stat = 1 AND log_day = %s", (today,))
        count = cursor.fetchone()[0]
        return count
    except mysql.connector.Error as err:
        print(f"Failed to count logged in visitors: {err}")
        return 0
    finally:
        cursor.close()
        conn.close()

def count_logged_out():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        today = datetime.now().date()
        cursor.execute("SELECT COUNT(*) FROM visitor_data WHERE log_stat = 0 AND log_day = %s", (today,))
        count = cursor.fetchone()[0]
        return count
    except mysql.connector.Error as err:
        print(f"Failed to count logged out visitors: {err}")
        return 0
    finally:
        cursor.close()
        conn.close()

def count_total_today():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        today = datetime.now().date()
        cursor.execute("SELECT COUNT(*) FROM visitor_data WHERE log_day = %s", (today,))
        count = cursor.fetchone()[0]
        return count
    except mysql.connector.Error as err:
        print(f"Failed to count total visitors today: {err}")
        return 0
    finally:
        cursor.close()
        conn.close()

#Log in Visitor Page_____________________________________________________________________________________________________________
def insert_visitor_data(visit_name, res_id, log_purpose, sec_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        # Prepare the current date and time
        current_datetime = datetime.now()
        log_day = current_datetime.date()
        login_time = current_datetime.strftime('%H:%M:%S')

        # Check if the visitor with the same name is already logged in
        query_check_existing = """
        SELECT * FROM visitor_data 
        WHERE visit_name = %s AND log_stat = TRUE AND logout_time IS NULL
        """
        cursor.execute(query_check_existing, (visit_name,))
        existing_visitor = cursor.fetchone()

        if existing_visitor:
            # Visitor is already logged in
            success = False
        else:
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
            success = True
    except mysql.connector.Error as err:
        print(f"Failed to insert visitor data: {err}")
        success = False
    finally:
        cursor.close()
        conn.close()
    return success

def fetch_residents():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT res_id, res_address FROM resident_data")
        residents = cursor.fetchall()  # Fetch all rows
        return residents
    except mysql.connector.Error as err:
        print(f"Failed to fetch resident data: {err}")
        return []
    finally:
        cursor.close()
        conn.close()


#Log out Visitor Page_____________________________________________________________________________________________________________
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

#Visitor Page_____________________________________________________________________________________________________________
def fetch_visitor_data_desc():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT visit_name, log_day, login_time, logout_time, res_id, sec_id, log_purpose FROM visitor_data ORDER BY log_day DESC, login_time DESC LIMIT 15")
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        print(f"Failed to fetch visitor data: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def fetch_visitor_data_asc():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT visit_name, log_day, login_time, logout_time, res_id, sec_id, log_purpose FROM visitor_data ORDER BY log_day ASC, login_time ASC LIMIT 15")
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        print(f"Failed to fetch visitor data: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def fetch_visitor_data_name_asc():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT visit_name, log_day, login_time, logout_time, res_id, sec_id, log_purpose FROM visitor_data ORDER BY visit_name ASC LIMIT 15")
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        print(f"Failed to fetch visitor data: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def fetch_visitor_data_name_desc():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT visit_name, log_day, login_time, logout_time, res_id, sec_id, log_purpose FROM visitor_data ORDER BY visit_name DESC LIMIT 15")
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        print(f"Failed to fetch visitor data: {err}")
        return []
    finally:
        cursor.close()
        conn.close()


#Resident Page_____________________________________________________________________________________________________________
def fetch_resident_data():
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT res_id, res_name, res_address, res_phonenumber FROM resident_data")
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        print(f"Failed to fetch resident data: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def update_resident_data(window, res_id, name, address, phone):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        # Use res_id for the WHERE clause
        query = "UPDATE resident_data SET res_name = %s, res_address = %s, res_phonenumber = %s WHERE res_id = %s"
        cursor.execute(query, (name, address, phone, res_id))
        conn.commit()
        # print("Resident data updated successfully.")
    except mysql.connector.Error as err:
        print(f"Failed to update resident data: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()