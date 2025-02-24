import sqlite3


# connect database to the hospital management system
def connect_db():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()

    # Create 'Doctor' Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctors (
        Id TEXT PRIMARY KEY,
        Name TEXT NOT NULL,
        Specialization TEXT NOT NULL,
        Contact TEXT,
        Address TEXT
    )
    """)
    # Create 'patients' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        Id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        contact TEXT,
        address TEXT,
        date_of_registration TEXT
    )
    """)
     # Create 'opd_records' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS opd_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        symptoms TEXT NOT NULL,
        doctor_assigned TEXT NOT NULL,
        date_of_visit TEXT NOT NULL
    )
    """)
    # Create 'ipd_records' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ipd_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        room_no TEXT NOT NULL,
        admission_date TEXT NOT NULL,
        discharge_date TEXT,
        doctor_in_charge TEXT NOT NULL
    )
    """)
    # Create 'icu_records' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS icu_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    room_no TEXT NOT NULL,
    admission_date TEXT NOT NULL,
    discharge_date TEXT,
    doctor_in_charge TEXT NOT NULL
    )
    """)
    # Create Emergency table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emergency_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        emergency_type TEXT NOT NULL,
        contact TEXT NOT NULL,
        doctor_assigned TEXT NOT NULL,
        arrival_time TEXT NOT NULL
    )
    """)
    # Create 'Housekeeping' Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Housekeeping (
        Id TEXT PRIMARY KEY,
        Name TEXT NOT NULL,
        Duty TEXT NOT NULL,
        Contact TEXT,
        Shift TEXT NOT NULL
    )
    """)
    # Create 'appointment' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        doctor_name TEXT,
        appointment_date TEXT, 
        appointment_time TEXT
    )
    """)
    # Create 'Payment' Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        amount_paid REAL NOT NULL, 
        payment_date TEXT NOT NULL,
        payment_mode TEXT NOT NULL
    )
    """)

    con.commit()
    con.close()


# function to insert_doctor details
def insert_doctor(Id, Name, Specialization, Contact, Address):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO Doctors (Id, Name, Specialization, Contact, Address) VALUES (?, ?, ?, ?, ?)
    """, (Id, Name, Specialization, Contact, Address))
    con.commit()
    con.close()


# Create function to fetch_doctor details
def fetch_doctors():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Doctors")
    doctors = cursor.fetchall()
    con.close()
    return doctors


# Create function to validate_doctor details
def is_valid_doctor(doctor_name):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM Doctors WHERE Name = ?", (doctor_name,))
    result = cursor.fetchone()[0]
    con.close()
    return result > 0


# Create function to update_doctor details
def update_doctor(Id, Name, Specialization, Contact, Address):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    UPDATE Doctors SET Name = ?, Specialization = ?, Contact = ?, Address = ? WHERE Id = ?
    """, (Name, Specialization, Contact, Address, Id))
    con.commit()
    con.close()


# Create function to delete_doctor details
def delete_doctor(Id):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM Doctors WHERE Id = ?", (Id,))
    con.commit()
    con.close()


# Create function to check wether doctor id is exist or not?
def id_exists(table_name, Id):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    query = f"SELECT COUNT(*) FROM {table_name} WHERE Id = ?"
    cursor.execute(query, (Id,))
    result = cursor.fetchone()[0]
    con.close()
    return result > 0


# Function to register a new patient
def register_patient_in_db(Id, name, age, gender, contact, address, date_of_registration):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO patients (Id, name, age, gender, contact, address, date_of_registration)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (Id, name, age, gender, contact, address, date_of_registration))
    con.commit()
    con.close()


# Create function to fetch_patients details
def fetch_patients():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    con.close()
    return patients


# Create function to update_patients details
def update_patient(Id, name, age, gender, contact, address):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    UPDATE patients
    SET name = ?, age = ?, gender = ?, contact = ?, address = ?
    WHERE Id = ?
    """, (name, age, gender, contact, address, Id))
    con.commit()
    con.close()


# Create function to delete_patients details
def delete_patient(Id):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM patients WHERE Id = ?", (Id,))
    con.commit()
    con.close()


# Create function to check if patient_id_exist or not?
def patient_id_exists(Id):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM patients WHERE Id = ?", (Id,))
    result = cursor.fetchone()[0]
    con.close()
    return result > 0


# Insert a new housekeeping staff member
def insert_housekeeping(Id, Name, Duty, Contact, Shift):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO Housekeeping (Id, Name, Duty, Contact, Shift)
    VALUES (?, ?, ?, ?, ?)
    """, (Id, Name, Duty, Contact, Shift))
    con.commit()
    con.close()


# Create function to add_duty_coloumn
def add_duty_column():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    ALTER TABLE Housekeeping ADD COLUMN Duty TEXT NOT NULL DEFAULT '';
    """)
    con.commit()
    con.close()


# Create function to Fetch all housekeeping staff
def fetch_housekeeping():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Housekeeping")
    housekeeping = cursor.fetchall()
    con.close()
    return housekeeping


# Update housekeeping staff details
def update_housekeeping(Id, Name, Duty, Contact, Shift):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    UPDATE Housekeeping
    SET Name = ?, Shift = ?, Contact = ?, Duty = ?
    WHERE Id = ?
    """, (Name, Duty, Contact, Shift, Id))
    con.commit()
    con.close()


# Register housekeeping staff
def register_housekeeping_in_db(Id, Name, Duty, Contact, Shift):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO Housekeeping (Id, Name, Duty, Contact, Shift)
    VALUES (?, ?, ?, ?, ?)
    """, (Id, Name, Duty, Contact, Shift))
    con.commit()
    con.close()


# Delete housekeeping staff by ID
def delete_housekeeping(Id):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM Housekeeping WHERE Id = ?", (Id,))
    con.commit()
    con.close()


# Check if housekeeping staff ID exists
def housekeeping_id_exists(Id):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM Housekeeping WHERE Id = ?", (Id,))
    result = cursor.fetchone()[0]
    con.close()
    return result > 0


# Add an Emergency Case
def add_emergency_case(patient_name, emergency_type, contact, doctor_assigned, arrival_time):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO emergency_cases (patient_name, emergency_type, contact, doctor_assigned, arrival_time)
    VALUES (?, ?, ?, ?, ?)
    """, (patient_name, emergency_type, contact, doctor_assigned, arrival_time))
    con.commit()
    con.close()


# Fetch all Emergency Cases
def get_emergency_cases():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM emergency_cases")
    records = cursor.fetchall()
    con.close()
    return records


# Function to add OPD record
def add_opd_record(patient_name, symptoms, doctor_assigned, date_of_visit):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO opd_records (patient_name, symptoms, doctor_assigned, date_of_visit)
    VALUES (?, ?, ?, ?)
    """, (patient_name, symptoms, doctor_assigned, date_of_visit))
    con.commit()
    con.close()


# Fetch OPD Records 
def fetch_opd_records():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM opd_records")
    records = cursor.fetchall()
    con.close()
    return records


# Function to add IPD record
def add_ipd_record(patient_name, room_no, admission_date, discharge_date, doctor_in_charge):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO ipd_records (patient_name, room_no, admission_date, discharge_date, doctor_in_charge)
    VALUES (?, ?, ?, ?, ?)
    """, (patient_name, room_no, admission_date, discharge_date, doctor_in_charge))
    con.commit()
    con.close()


# Fetch IPD Records 
def fetch_ipd_records():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ipd_records")
    records = cursor.fetchall()
    con.close()
    return records


# Create function to add_icu_records
def add_icu_records(patient_name, room_no, admission_date, discharge_date, doctor_in_charge):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO icu_records (patient_name, room_no, admission_date, discharge_date, doctor_in_charge)
    VALUES (?, ?, ?, ?, ?)
    """, (patient_name, room_no, admission_date, discharge_date, doctor_in_charge))
    con.commit()
    con.close()


# Fetch IPD Records 
def fetch_icu_records():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM icu_records")
    records = cursor.fetchall()
    con.close()
    return records


# 🏥 Add Doctor
def add_doctor(name):
    try:
        con = sqlite3.connect("hospital.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO doctors (name) VALUES (?)", (name,))
        con.commit()
    except sqlite3.IntegrityError:
        print("Doctor already exists!")


# 🏥 Get Doctor Names (For dropdown)
def get_doctor_names():
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT name FROM doctors")
    return [row[0] for row in cursor.fetchall()]


# 🏥 Validate Doctor Name
def is_valid_doctor(name):
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM doctors WHERE name = ?", (name,))
    return cursor.fetchone() is not None


# Function to insert an appointment into the database
def insert_appointment(patient_name, doctor_name, appointment_date, appointment_time):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO appointments (patient_name, doctor_name, appointment_date, appointment_time)
                      VALUES (?, ?, ?, ?)''',
                   (patient_name, doctor_name, appointment_date, appointment_time))
    conn.commit()
    conn.close()


# Function to fetch all appointments
def fetch_appointments():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    conn.close()
    return rows


# Create function to search_patient_records
def search_patient_records(patient_id=None, patient_name=None):
    """
    Search for patient records by ID (optional) and Name (mandatory).
    """
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()

    if patient_id:
        # Search by both ID and Name
        query = "SELECT Id, name, age, gender, contact, address, date_of_registration FROM patients WHERE Id = ? AND name LIKE ?"
        cursor.execute(query, (patient_id, f"%{patient_name}%"))
    else:
        # Search by Name only
        query = "SELECT Id, name, age, gender, contact, address, date_of_registration FROM patients WHERE name LIKE ?"
        cursor.execute(query, (f"%{patient_name}%",))

    results = cursor.fetchall()
    con.close()
    return results


# Create function to fetch_payments details
def fetch_payments():
    """
    Fetch all payment records.
    """
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM payments")
    records = cursor.fetchall()
    con.close()
    return records


# Create function to add_payment
def add_payment(patient_name, amount_paid, payment_date, payment_mode):
    """
    Add a new payment record.
    """
    con = sqlite3.connect("hospital.db")
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO payments (patient_name, amount_paid, payment_date, payment_mode)
    VALUES (?, ?, ?, ?)
    """, (patient_name, amount_paid, payment_date, payment_mode))
    con.commit()
    con.close()


connect_db()
