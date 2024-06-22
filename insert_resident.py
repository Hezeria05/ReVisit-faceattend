import sqlite3

def insert_resident_data():
    conn = sqlite3.connect('visitor_attendance.db')
    cursor = conn.cursor()

    # List of resident data to be inserted
    resident_data = [
        (32, 'John Doe', 'Block 1 Lot 1 Phase 1 Hydrogen', '09123456780'),
        (33, 'Jane Smith', 'Block 1 Lot 2 Phase 1 Helium', '09123456781'),
        (34, 'Alice Johnson', 'Block 1 Lot 3 Phase 1 Lithium', '09123456782'),
        (35, 'Michael Brown', 'Block 1 Lot 4 Phase 1 Beryllium', '09123456783'),
        (36, 'Chloe Davis', 'Block 1 Lot 5 Phase 1 Boron', '09123456784'),
        (37, 'Lucas Miller', 'Block 1 Lot 6 Phase 1 Carbon', '09123456785'),
        (38, 'Emma Wilson', 'Block 1 Lot 7 Phase 1 Nitrogen', '09123456786'),
        (39, 'Oliver Moore', 'Block 1 Lot 8 Phase 1 Oxygen', '09123456787'),
        (40, 'Sophia Young', 'Block 1 Lot 9 Phase 1 Fluorine', '09123456788'),
        (41, 'Ethan Johnson', 'Block 1 Lot 10 Phase 1 Neon', '09123456789'),
        (42, 'Mia Williams', 'Block 1 Lot 11 Phase 1 Hydrogen', '09123456790'),
        (43, 'Noah Jones', 'Block 1 Lot 12 Phase 1 Helium', '09123456791'),
        (44, 'Isabella Taylor', 'Block 1 Lot 13 Phase 1 Lithium', '09123456792'),
        (45, 'William White', 'Block 1 Lot 14 Phase 1 Beryllium', '09123456793'),
        (46, 'Ava Thompson', 'Block 1 Lot 15 Phase 1 Boron', '09123456794'),
        (47, 'Matthew Harris', 'Block 1 Lot 16 Phase 1 Carbon', '09123456795'),
        (48, 'Amelia Martin', 'Block 1 Lot 17 Phase 1 Nitrogen', '09123456796'),
        (49, 'James Lee', 'Block 1 Lot 18 Phase 1 Oxygen', '09123456797'),
        (50, 'Charlotte Hall', 'Block 2 Lot 1 Phase 2 Fluorine', '09123456798'),
        (51, 'Alexander Allen', 'Block 2 Lot 2 Phase 2 Neon', '09123456799'),
        (52, 'Harper Young', 'Block 2 Lot 3 Phase 2 Hydrogen', '09123456800'),
        (53, 'Elijah Scott', 'Block 2 Lot 4 Phase 2 Helium', '09123456801'),
        (54, 'Isabelle Edwards', 'Block 2 Lot 5 Phase 2 Lithium', '09123456802'),
        (55, 'Jack Wright', 'Block 2 Lot 6 Phase 2 Beryllium', '09123456803'),
        (56, 'Lily King', 'Block 2 Lot 7 Phase 2 Boron', '09123456804'),
        (57, 'Benjamin Moore', 'Block 2 Lot 8 Phase 2 Carbon', '09123456805'),
        (58, 'Zoe Miller', 'Block 2 Lot 9 Phase 2 Nitrogen', '09123456806'),
        (59, 'Logan Brown', 'Block 2 Lot 10 Phase 2 Oxygen', '09123456807'),
        (60, 'Grace Davis', 'Block 3 Lot 1 Phase 1 Fluorine', '09123456808'),
        (61, 'Ryan Wilson', 'Block 3 Lot 2 Phase 1 Neon', '09123456809'),
        (62, 'Jackson Wong', 'Block 3 Lot 3 Phase 1 Hydrogen', '09123456810'),
        (63, 'Ella Thompson', 'Block 3 Lot 4 Phase 1 Helium', '09123456811'),
        (64, 'Henry Anderson', 'Block 3 Lot 5 Phase 1 Lithium', '09123456812'),
        (65, 'Scarlett Lee', 'Block 3 Lot 6 Phase 1 Beryllium', '09123456813'),
        (66, 'David Martin', 'Block 3 Lot 7 Phase 1 Boron', '09123456814'),
        (67, 'Victoria Clark', 'Block 3 Lot 8 Phase 1 Carbon', '09123456815'),
        (68, 'Daniel Lewis', 'Block 3 Lot 9 Phase 1 Nitrogen', '09123456816'),
        (69, 'Abigail Walker', 'Block 3 Lot 10 Phase 1 Oxygen', '09123456817'),
        (70, 'Mason Young', 'Block 3 Lot 11 Phase 1 Fluorine', '09123456818'),
        (71, 'Hannah Hill', 'Block 3 Lot 12 Phase 1 Neon', '09123456819'),
        (72, 'Jacob Martinez', 'Block 3 Lot 13 Phase 1 Hydrogen', '09123456820'),
        (73, 'Sofia Wright', 'Block 3 Lot 14 Phase 1 Helium', '09123456821'),
        (74, 'William Robinson', 'Block 3 Lot 15 Phase 1 Lithium', '09123456822'),
        (75, 'Grace Mitchell', 'Block 3 Lot 16 Phase 1 Beryllium', '09123456823'),
        (76, 'James Harris', 'Block 3 Lot 17 Phase 1 Boron', '09123456824')
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
