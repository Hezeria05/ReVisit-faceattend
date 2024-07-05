import sqlite3

def insert_resident_data():
    conn = sqlite3.connect('visitor_attendance.db')
    cursor = conn.cursor()

    # Delete the current data in resident_data table
    cursor.execute("DELETE FROM resident_data")

    # List of resident data to be inserted
    resident_data = [
        (32, 'John Doe', 'B1 L1 Phase 1 Hydrogen', '09123456780'),
        (33, 'Jane Smith', 'B1 L2 Phase 1 Helium', '09123456781'),
        (34, 'Alice Johnson', 'B1 L3 Phase 1 Lithium', '09123456782'),
        (35, 'Michael Brown', 'B1 L4 Phase 1 Beryllium', '09123456783'),
        (36, 'Chloe Davis', 'B1 L5 Phase 1 Boron', '09123456784'),
        (37, 'Lucas Miller', 'B1 L6 Phase 1 Carbon', '09123456785'),
        (38, 'Emma Wilson', 'B1 L7 Phase 1 Nitrogen', '09123456786'),
        (39, 'Oliver Moore', 'B1 L8 Phase 1 Oxygen', '09123456787'),
        (40, 'Sophia Young', 'B1 L9 Phase 1 Fluorine', '09123456788'),
        (41, 'Ethan Johnson', 'B1 L10 Phase 1 Neon', '09123456789'),
        (42, 'Mia Williams', 'B1 L11 Phase 1 Hydrogen', '09123456790'),
        (43, 'Noah Jones', 'B1 L12 Phase 1 Helium', '09123456791'),
        (44, 'Isabella Taylor', 'B1 L13 Phase 1 Lithium', '09123456792'),
        (45, 'William White', 'B1 L14 Phase 1 Beryllium', '09123456793'),
        (46, 'Ava Thompson', 'B1 L15 Phase 1 Boron', '09123456794'),
        (47, 'Matthew Harris', 'B1 L16 Phase 1 Carbon', '09123456795'),
        (48, 'Amelia Martin', 'B1 L17 Phase 1 Nitrogen', '09123456796'),
        (49, 'James Lee', 'B1 L18 Phase 1 Oxygen', '09123456797'),
        (50, 'Charlotte Hall', 'B2 L1 Phase 2 Fluorine', '09123456798'),
        (51, 'Alexander Allen', 'B2 L2 Phase 2 Neon', '09123456799'),
        (52, 'Harper Young', 'B2 L3 Phase 2 Hydrogen', '09123456800'),
        (53, 'Elijah Scott', 'B2 L4 Phase 2 Helium', '09123456801'),
        (54, 'Isabelle Edwards', 'B2 L5 Phase 2 Lithium', '09123456802'),
        (55, 'Jack Wright', 'B2 L6 Phase 2 Beryllium', '09123456803'),
        (56, 'Lily King', 'B2 L7 Phase 2 Boron', '09123456804'),
        (57, 'Benjamin Moore', 'B2 L8 Phase 2 Carbon', '09123456805'),
        (58, 'Zoe Miller', 'B2 L9 Phase 2 Nitrogen', '09123456806'),
        (59, 'Logan Brown', 'B2 L10 Phase 2 Oxygen', '09123456807'),
        (60, 'Grace Davis', 'B3 L1 Phase 1 Fluorine', '09123456808'),
        (61, 'Ryan Wilson', 'B3 L2 Phase 1 Neon', '09123456809'),
        (62, 'Jackson Wong', 'B3 L3 Phase 1 Hydrogen', '09123456810'),
        (63, 'Ella Thompson', 'B3 L4 Phase 1 Helium', '09123456811'),
        (64, 'Henry Anderson', 'B3 L5 Phase 1 Lithium', '09123456812'),
        (65, 'Scarlett Lee', 'B3 L6 Phase 1 Beryllium', '09123456813'),
        (66, 'David Martin', 'B3 L7 Phase 1 Boron', '09123456814'),
        (67, 'Victoria Clark', 'B3 L8 Phase 1 Carbon', '09123456815'),
        (68, 'Daniel Lewis', 'B3 L9 Phase 1 Nitrogen', '09123456816'),
        (69, 'Abigail Walker', 'B3 L10 Phase 1 Oxygen', '09123456817'),
        (70, 'Mason Young', 'B3 L11 Phase 1 Fluorine', '09123456818'),
        (71, 'Hannah Hill', 'B3 L12 Phase 1 Neon', '09123456819'),
        (72, 'Jacob Martinez', 'B3 L13 Phase 1 Hydrogen', '09123456820'),
        (73, 'Sofia Wright', 'B3 L14 Phase 1 Helium', '09123456821'),
        (74, 'William Robinson', 'B3 L15 Phase 1 Lithium', '09123456822'),
        (75, 'Grace Mitchell', 'B3 L16 Phase 1 Beryllium', '09123456823'),
        (76, 'James Harris', 'B3 L17 Phase 1 Boron', '09123456824')
    ]

    # Insert data into resident_data table
    cursor.executemany('''
    INSERT INTO resident_data (res_id, res_name, res_address, res_phonenumber)
    VALUES (?, ?, ?, ?)
    ''', resident_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the function to insert resident data
insert_resident_data()
