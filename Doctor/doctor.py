from tkinter import *
import customtkinter
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox, ttk
import datetime
import Database.database as database


# Create a new window to open_doctor_dashboard
def open_doctor_dashboard():
    management_dashboard = Toplevel()
    management_dashboard.title("Doctor Dashboard - Hospital Management System")
    management_dashboard.geometry("1000x600")
    management_dashboard.resizable(False, False)

    # Add the background image
    bg_image = Image.open(r"E:\Python(HMS)\Doctor.png")
    bg_image = bg_image.resize((1000, 600))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(management_dashboard, image=bg_photo)
    bg_label.image = bg_photo  # Keep reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Button Style Configuration
    button_style = {
        "fg_color": "#007BFF",
        "hover_color": "#0056b3",
        "text_color": "white",
        "corner_radius": 10,
        "width": 220,
        "height": 50,
        "font": ("Arial", 16, "bold")
    }

    # OPD Button
    btn_opd = customtkinter.CTkButton(management_dashboard, text="OPD", command= open_opd_dashboard, **button_style)
    btn_opd.place(x=100, y=200)

    # IPD Button
    btn_ipd = customtkinter.CTkButton(management_dashboard, text="IPD", command= open_ipd_dashboard, **button_style)
    btn_ipd.place(x=100, y=350)

    # ICU Button
    btn_icu = customtkinter.CTkButton(management_dashboard, text="ICU", command= open_icu_dashboard, **button_style)
    btn_icu.place(x=700, y=200)

    # Emergency Button
    emergency_button = customtkinter.CTkButton(management_dashboard, text="Emergency", command= open_emergency_dashboard, **button_style)
    emergency_button.place(x=700, y=350)

    # Exit Button (NO CHANGES)
    btn_exit = customtkinter.CTkButton(management_dashboard, text="Exit", fg_color="red", hover_color="darkred", command=management_dashboard.destroy)
    btn_exit.place(x=420, y=555)  # Same position as before

# Function to show a message when a button is clicked
def show_section(section):
    messagebox.showinfo("Section Clicked", f"You selected {section} section!")


# Create a window to open_OPD_dashboard
def open_opd_dashboard():
    opd_dashboard = Toplevel()
    opd_dashboard.title("Outpatient Department (OPD)")
    opd_dashboard.geometry("800x600")
    opd_dashboard.maxsize(800, 600)
    opd_dashboard.minsize(800, 600)
    bg_image = Image.open(r"E:\Python(HMS)\OPD.png")
    bg_image = bg_image.resize((800, 600))
    bg = ImageTk.PhotoImage(bg_image)

    bg_label = Label(opd_dashboard, image= bg)
    bg_label.image = bg
    bg_label.place(x= 0, y= 0, relheight= 1, relwidth= 1)

    Label(opd_dashboard, text="Patient Name:", font=("Arial", 14), bg="#f0f8ff").place(x=50, y=150)
    patient_name_entry = Entry(opd_dashboard, font=("Arial", 12), width=30)
    patient_name_entry.place(x=250, y=150)

    Label(opd_dashboard, text="Symptoms:", font=("Arial", 14), bg="#f0f8ff").place(x=50, y=200)
    symptoms_entry = Entry(opd_dashboard, font=("Arial", 12), width=30)
    symptoms_entry.place(x=250, y=200)

    Label(opd_dashboard, text="Doctor Assigned:", font=("Arial", 14), bg="#f0f8ff").place(x=50, y=250)
    doctor_entry = Entry(opd_dashboard, font=("Arial", 12), width=30)
    doctor_entry.place(x=250, y=250)

    # Save OPD record
    from Database.database import add_opd_record
    def save_opd_record():
        patient_name = patient_name_entry.get()
        symptoms = symptoms_entry.get()
        doctor_assigned = doctor_entry.get()
        date_of_visit = datetime.date.today().strftime("%Y-%m-%d")

        if not patient_name or not symptoms or not doctor_assigned:
            messagebox.showerror("Error", "All fields are required!")
        else:
            add_opd_record(patient_name, symptoms, doctor_assigned, date_of_visit)
            messagebox.showinfo("Success", "OPD record added successfully!")
            opd_dashboard.destroy()

    Button(opd_dashboard, text="Save Record", font=("Arial", 14), bg="#4CAF50", fg="white",
           command=save_opd_record).place(x=200, y=350, width=150, height=40)
    
    # View OPD Records
    from Database.database import fetch_opd_records
    def view_opd_records():
        records_window = Toplevel()
        records_window.title("OPD Records")
        records_window.geometry("800x400")
        records_window.config(bg="#f0f8ff")

        records_table = ttk.Treeview(records_window, columns=("ID", "Patient Name", "Symptoms", "Doctor", "Date"), show="headings")
        records_table.heading("ID", text="ID")
        records_table.heading("Patient Name", text="Patient Name")
        records_table.heading("Symptoms", text="Symptoms")
        records_table.heading("Doctor", text="Doctor")
        records_table.heading("Date", text="Date of Visit")
        records_table.pack(fill=BOTH, expand=True)

        records = fetch_opd_records()
        for record in records:
            records_table.insert("", END, values=record)

    Button(opd_dashboard, text="View OPD Records", font=("Arial", 14), bg="#2196F3", fg="white",
           command=view_opd_records).place(x=400, y=350, width=200, height=40)


# Create window to open_IPD_dahboard
def open_ipd_dashboard():
    ipd_dashboard = Toplevel()
    ipd_dashboard.title("Inpatient Department (IPD)")
    ipd_dashboard.geometry("800x600")
    ipd_dashboard.maxsize(800, 600)
    ipd_dashboard.minsize(800, 600)
    bg_image = Image.open(r"E:\Python(HMS)\IPD.png")
    bg_image = bg_image.resize((800, 600))
    #bg_image = bg_image.filter(ImageFilter.GaussianBlur(5))
    bg = ImageTk.PhotoImage(bg_image)

    bg_label = Label(ipd_dashboard, image= bg)
    bg_label.image = bg
    bg_label.place(x= 0, y= 0, relheight= 1, relwidth= 1)
    

    Label(ipd_dashboard, text="Patient Name:", font=("Arial", 14), bg="#f0f4c3").place(x=50, y=150)
    patient_name_entry = Entry(ipd_dashboard, font=("Arial", 12), width=30)
    patient_name_entry.place(x=250, y=150)

    Label(ipd_dashboard, text="Room No:", font=("Arial", 14), bg="#f0f4c3").place(x=50, y=200)
    room_no_entry = Entry(ipd_dashboard, font=("Arial", 12), width=30)
    room_no_entry.place(x=250, y=200)

    Label(ipd_dashboard, text="Doctor In Charge:", font=("Arial", 14), bg="#f0f4c3").place(x=50, y=250)
    doctor_entry = Entry(ipd_dashboard, font=("Arial", 12), width=30)
    doctor_entry.place(x=250, y=250)

    Label(ipd_dashboard, text="Admission Date:", font=("Arial", 14), bg="#f0f4c3").place(x=50, y=300)
    admission_date_entry = Entry(ipd_dashboard, font=("Arial", 12), width=30)
    admission_date_entry.place(x=250, y=300)

    Label(ipd_dashboard, text="Discharge Date:", font=("Arial", 14), bg="#f0f4c3").place(x=50, y=350)
    discharge_date_entry = Entry(ipd_dashboard, font=("Arial", 12), width=30)
    discharge_date_entry.place(x=250, y=350)

    # Save IPD record
    from Database.database import add_ipd_record
    def save_ipd_record():
        patient_name = patient_name_entry.get()
        room_no = room_no_entry.get()
        admission_date = admission_date_entry.get()
        discharge_date = discharge_date_entry.get()
        doctor_in_charge = doctor_entry.get()

        if not patient_name or not room_no or not doctor_in_charge:
            messagebox.showerror("Error", "All fields are required!")
        else:
            add_ipd_record(patient_name, room_no, admission_date, discharge_date, doctor_in_charge)
            messagebox.showinfo("Success", "IPD record added successfully!")
            ipd_dashboard.destroy()

    Button(ipd_dashboard, text="Save Record", font=("Arial", 14), bg="#4CAF50", fg="white",
           command=save_ipd_record).place(x=200, y=450, width=150, height=40)

    # View IPD Records
    from Database.database import fetch_ipd_records
    def view_ipd_records():
        records_window = Toplevel()
        records_window.title("IPD Records")
        records_window.geometry("800x400")
        records_window.config(bg="#f0f4c3")

        records_table = ttk.Treeview(records_window, columns=("ID", "Patient Name", "Room No", "Admission Date", "Discharge Date", "Doctor"), show="headings")
        records_table.heading("ID", text="ID")
        records_table.heading("Patient Name", text="Patient Name")
        records_table.heading("Room No", text="Room No")
        records_table.heading("Admission Date", text="Admission Date")
        records_table.heading("Discharge Date", text="Discharge Date")
        records_table.heading("Doctor", text="Doctor")
        records_table.pack(fill=BOTH, expand=True)

        records = fetch_ipd_records()
        for record in records:
            records_table.insert("", END, values=record)

    Button(ipd_dashboard, text="View IPD Records", font=("Arial", 14), bg="#2196F3", fg="white",
           command=view_ipd_records).place(x=400, y=450, width=200, height=40)


# Create window to open_Emergency_Dashboard
def open_emergency_dashboard():
    emergency_dashboard = Toplevel()
    emergency_dashboard.title("Emergency Cases")
    emergency_dashboard.geometry("800x600")
    emergency_dashboard.maxsize(800, 600)
    emergency_dashboard.minsize(800, 600)
    bg_image = Image.open(r"E:\Python(HMS)\Emergency.png")
    bg_image = bg_image.resize((800, 600))
    bg = ImageTk.PhotoImage(bg_image)

    bg_label = Label(emergency_dashboard, image= bg)
    bg_label.image = bg
    bg_label.place(x= 0, y= 0, relheight= 1, relwidth= 1)

    Label(emergency_dashboard, text="Patient Name:", font=("Arial", 14), bg="#f8d7da").place(x=50, y=150)
    patient_name_entry = Entry(emergency_dashboard, font=("Arial", 12), width=30)
    patient_name_entry.place(x=250, y=150)

    Label(emergency_dashboard, text="Emergency Type:", font=("Arial", 14), bg="#f8d7da").place(x=50, y=200)
    emergency_type_entry = Entry(emergency_dashboard, font=("Arial", 12), width=30)
    emergency_type_entry.place(x=250, y=200)

    Label(emergency_dashboard, text="Contact:", font=("Arial", 14), bg="#f8d7da").place(x=50, y=250)
    contact_entry = Entry(emergency_dashboard, font=("Arial", 12), width=30)
    contact_entry.place(x=250, y=250)

    Label(emergency_dashboard, text="Doctor Assigned:", font=("Arial", 14), bg="#f8d7da").place(x=50, y=300)
    doctor_entry = Entry(emergency_dashboard, font=("Arial", 12), width=30)
    doctor_entry.place(x=250, y=300)

    # Save Emergency Case
    from Database.database import add_emergency_case
    def save_emergency_case():
        patient_name = patient_name_entry.get()
        emergency_type = emergency_type_entry.get()
        contact = contact_entry.get()
        doctor_assigned = doctor_entry.get()
        arrival_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not patient_name or not emergency_type or not contact or not doctor_assigned:
            messagebox.showerror("Error", "All fields are required!")
        else:
            add_emergency_case(patient_name, emergency_type, contact, doctor_assigned, arrival_time)
            messagebox.showinfo("Success", "Emergency case added successfully!")
            emergency_dashboard.destroy()

    Button(emergency_dashboard, text="Save Record", font=("Arial", 14), bg="#c9302c", fg="white",
           command=save_emergency_case).place(x=200, y= 400, width=150, height=40)

    # View Emergency Records
    from Database.database import get_emergency_cases
    def view_emergency_cases():
        records_window = Toplevel()
        records_window.title("Emergency Cases")
        records_window.geometry("800x400")
        records_window.config(bg="#f8d7da")

        records_table = ttk.Treeview(records_window, columns=("ID", "Patient Name", "Emergency Type", "Contact", "Doctor", "Arrival Time"), show="headings")
        records_table.heading("ID", text="ID")
        records_table.heading("Patient Name", text="Patient Name")
        records_table.heading("Emergency Type", text="Emergency Type")
        records_table.heading("Contact", text="Contact")
        records_table.heading("Doctor", text="Doctor")
        records_table.heading("Arrival Time", text="Arrival Time")
        records_table.pack(fill=BOTH, expand=True)

        # Fetch records from the database
        records = get_emergency_cases()
        for record in records:
            records_table.insert("", END, values=record)

    Button(emergency_dashboard, text="View Records", font=("Arial", 14), bg="#6c757d", fg="white",
           command=view_emergency_cases).place(x=400, y=400, width=150, height=40)
    

# create window to open_ICU_dashboard
def open_icu_dashboard():
    icu_dashboard = Toplevel()
    icu_dashboard.title("Intensive Care Unit (ICU)")
    icu_dashboard.geometry("800x600")
    icu_dashboard.maxsize(800, 600)
    icu_dashboard.minsize(800, 600)

    # Load background image
    bg_image = Image.open(r"E:\Python(HMS)\ICU.png")  # Update with your actual image path
    bg_image = bg_image.resize((800, 600))
    bg = ImageTk.PhotoImage(bg_image)

    bg_label = Label(icu_dashboard, image=bg)
    bg_label.image = bg
    bg_label.place(x=0, y=0, relheight=1, relwidth=1)

    Label(icu_dashboard, text="Patient Name:", font=("Arial", 14), bg="#d1c4e9").place(x=50, y=150)
    patient_name_entry = Entry(icu_dashboard, font=("Arial", 12), width=30)
    patient_name_entry.place(x=250, y=150)

    Label(icu_dashboard, text="Room No:", font=("Arial", 14), bg="#d1c4e9").place(x=50, y=200)
    room_no_entry = Entry(icu_dashboard, font=("Arial", 12), width=30)
    room_no_entry.place(x=250, y=200)

    Label(icu_dashboard, text="Doctor In Charge:", font=("Arial", 14), bg="#d1c4e9").place(x=50, y=250)
    
    # Doctor dropdown
    from Database.database import get_doctor_names
    doctor_names = get_doctor_names()
    doctor_entry = ttk.Combobox(icu_dashboard, values=doctor_names, font=("Arial", 12), width=27)
    doctor_entry.place(x=250, y=250)

    Label(icu_dashboard, text="Admission Date:", font=("Arial", 14), bg="#d1c4e9").place(x=50, y=300)
    admission_date_entry = Entry(icu_dashboard, font=("Arial", 12), width=30)
    admission_date_entry.place(x=250, y=300)

    Label(icu_dashboard, text="Discharge Date:", font=("Arial", 14), bg="#d1c4e9").place(x=50, y=350)
    discharge_date_entry = Entry(icu_dashboard, font=("Arial", 12), width=30)
    discharge_date_entry.place(x=250, y=350)

    # Save ICU record
    from Database.database import is_valid_doctor, add_icu_records
    def save_icu_record():
        patient_name = patient_name_entry.get()
        room_no = room_no_entry.get()
        admission_date = admission_date_entry.get()
        discharge_date = discharge_date_entry.get()
        doctor_in_charge = doctor_entry.get()

        if not patient_name or not room_no or not doctor_in_charge:
            messagebox.showerror("Error", "All fields are required!")
        elif not is_valid_doctor(doctor_in_charge):
            messagebox.showerror("Error", "Invalid doctor name!")
        else:
            if discharge_date == "":
                discharge_date = None  # Handle optional discharge date
            add_icu_records(patient_name, room_no, admission_date, discharge_date, doctor_in_charge)
            messagebox.showinfo("Success", "ICU record added successfully!")
            icu_dashboard.destroy()

    Button(icu_dashboard, text="Save Record", font=("Arial", 14), bg="#4CAF50", fg="white",
           command=save_icu_record).place(x=200, y=450, width=150, height=40)

    # View ICU Records
    from Database.database import fetch_icu_records
    def view_icu_records():
        records_window = Toplevel()
        records_window.title("ICU Records")
        records_window.geometry("800x400")
        records_window.config(bg="#d1c4e9")

        records_table = ttk.Treeview(records_window, columns=("ID", "Patient Name", "Room No", "Admission Date", "Discharge Date", "Doctor"), show="headings")
        records_table.heading("ID", text="ID")
        records_table.heading("Patient Name", text="Patient Name")
        records_table.heading("Room No", text="Room No")
        records_table.heading("Admission Date", text="Admission Date")
        records_table.heading("Discharge Date", text="Discharge Date")
        records_table.heading("Doctor", text="Doctor")
        records_table.pack(fill=BOTH, expand=True)

        records = fetch_icu_records()
        for record in records:
            records_table.insert("", END, values=record)

    Button(icu_dashboard, text="View ICU Records", font=("Arial", 14), bg="#2196F3", fg="white",
           command=view_icu_records).place(x=400, y=450, width=200, height=40)


