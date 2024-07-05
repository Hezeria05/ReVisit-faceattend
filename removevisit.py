import sqlite3

def remove_dingdong():
    conn = sqlite3.connect('visitor_attendance.db')
    cursor = conn.cursor()
    try:
        # Delete records where visit_name is 'DINGDONG'
        cursor.execute("DELETE FROM visitor_data WHERE visit_name = 'DINGDONG'")
        
        # Commit the changes
        conn.commit()
    except sqlite3.Error as err:
        print(f"Failed to remove 'DINGDONG': {err}")
    finally:
        cursor.close()
        conn.close()

remove_dingdong()