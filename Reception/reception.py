from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
from tkcalendar import Calendar
from Database.database import insert_appointment, get_doctor_names, fetch_patients, search_patient_records


# Create a window to open_reception_dashboard
def open_reception_dashboard(login_window):
    reception_dashboard = Toplevel()
    reception_dashboard.title("Reception Dashboard - Hospital Management System")
    reception_dashboard.geometry("1000x600")
    reception_dashboard.maxsize(1000, 600)
    reception_dashboard.minsize(1000, 600)

    # hide the login window
    login_window.withdraw()

    # Add the background image in Reception Dashboard
    bg_image = Image.open(r"E:\Python(HMS)\Reception.png")
    bg_image = bg_image.resize((1000, 600))
    bg = ImageTk.PhotoImage(bg_image)
    bg_label = Label(reception_dashboard, image=bg)
    bg_label.image = bg
    bg_label.place(x=0, y=0, relheight=1, relwidth=1)

    # Button design settings
    button_width = 280
    button_height = 60
    button_font = ("Arial", 16, "bold")

    def create_glass_button(text, y, command=None):
        button = customtkinter.CTkButton(reception_dashboard, text=text, text_color="#FFFFFF", font=button_font,
                                         fg_color="#2C3E50", hover_color="#34495E", corner_radius=15,
                                         width=button_width, height=button_height, border_width=2, border_color="#FFFFFF",
                                         command=command)
        button.place(x=360, y=y)
        return button

    # Appointment of New Patient
    create_glass_button("\ud83d\udcc5 Appointment Schedule", y=130, command=open_appointment_schedule)

    # Search Patient Records
    create_glass_button("\ud83d\udd0d Search Patient Records", y=230, command=search_patient_window)

    # Show All Records
    create_glass_button("\ud83d\udcc3 Show All Records", y=330, command=show_all_records)

    # Cashier
    create_glass_button("\ud83d\udcb5 Cashier", y=430, command=open_cashier)

    # Exit
    def close_dashboard():
        reception_dashboard.destroy()
        login_window.deiconify()

    create_glass_button("🚪 Exit", y=530, command=close_dashboard)

# Create a window to open_appointment_schedule
def open_appointment_schedule():
    appointment_window = Toplevel()
    appointment_window.title("Appointment Schedule")
    appointment_window.geometry("600x500")
    appointment_window.minsize(800, 600)
    appointment_window.maxsize(600, 500)

    # UI elements
    Label(appointment_window, text="Appointment Schedule", font=("Arial", 18, "bold")).pack(pady=10)

    # Patient Name
    Label(appointment_window, text="Patient Name:", font=("Arial", 12)).pack(anchor=W, padx=20)
    patient_name_entry = Entry(appointment_window, font=("Arial", 12), width=30)
    patient_name_entry.pack(pady=5)

    # Doctor Selection
    Label(appointment_window, text="Select Doctor:", font=("Arial", 12)).pack(anchor=W, padx=20)

    # Fetch doctor names from the database
    doctor_names = get_doctor_names()  # Function from your database file
    doctor_dropdown = ttk.Combobox(appointment_window, values=doctor_names, font=("Arial", 12), width=28, state="readonly")
    doctor_dropdown.set("Select Doctor")
    doctor_dropdown.pack(pady=5)

    # Calendar for Appointment Date
    Label(appointment_window, text="Select Date:", font=("Arial", 12)).pack(anchor=W, padx=20)
    calendar = Calendar(appointment_window, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.pack(pady=10)

    # Appointment Time
    Label(appointment_window, text="Select Time Slot:", font=("Arial", 12)).pack(anchor=W, padx=20)
    time_slots = ["10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM", "12:00 PM - 1:00 PM", "2:00 PM - 3:00 PM"]
    time_dropdown = ttk.Combobox(appointment_window, values=time_slots, font=("Arial", 12), width=28, state="readonly")
    time_dropdown.set("Select Time")
    time_dropdown.pack(pady=5)

    # Save Button
    def save_appointment():
        patient_name = patient_name_entry.get()
        doctor_name = doctor_dropdown.get()
        appointment_date = calendar.get_date()
        appointment_time = time_dropdown.get()

        if not patient_name or doctor_name == "Select Doctor" or appointment_time == "Select Time":
            Label(appointment_window, text="Please fill all fields!", fg="red", font=("Arial", 10)).pack(pady=5)
            return

        # Insert appointment into the database
        insert_appointment(patient_name, doctor_name, appointment_date, appointment_time)

        # Confirmation Message
        Label(appointment_window, text="Appointment Saved Successfully!", fg="green", font=("Arial", 10)).pack(pady=5)

        # Clear fields
        patient_name_entry.delete(0, END)
        doctor_dropdown.set("Select Doctor")
        time_dropdown.set("Select Time")

    # Create Button for 'Save Appointment'
    Button(appointment_window, text="Save Appointment", font=("Arial", 14, "bold"), bg="#27AE60", fg="#FFFFFF",
           width=20, command=save_appointment).place(x= 80, y= 470)

    # View Appointments Button
    def view_appointments():
        view_window = Toplevel()
        view_window.title("View Appointments")
        view_window.geometry("600x400")

        # Fetch all appointments from the database
        from Database.database import fetch_appointments
        appointments = fetch_appointments()

        # Display appointments
        Label(view_window, text="All Appointments", font=("Arial", 16, "bold")).pack(pady=10)
        columns = ("ID", "Patient Name", "Doctor Name", "Date", "Time")

        tree = ttk.Treeview(view_window, columns=columns, show="headings", height=15)
        tree.pack(fill=BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for appointment in appointments:
            tree.insert("", "end", values=appointment)

        # Close Button for view window
        Button(view_window, text="Close", font=("Arial", 12), bg="#C0392B", fg="#FFFFFF",
               command=view_window.destroy).pack(pady=10)

    Button(appointment_window, text="View Appointments", font=("Arial", 14, "bold"), bg="#3498DB", fg="#FFFFFF",
           width=20, command=view_appointments).place(x= 500, y= 470)

    # Close Button
    Button(appointment_window, text="Close", font=("Arial", 14, "bold"), bg="#C0392B", fg="#FFFFFF",
           width=20, command=appointment_window.destroy).place(x= 280, y= 540)


# Create a function to show_all_records
def show_all_records():
    records_window = Toplevel()
    records_window.title("All Patient Records")
    records_window.geometry("800x400")

    # Add a Treeview to display data in tabular form
    columns = ('ID', 'Name', 'Age', 'Gender', 'Contact', 'Address', 'Registration Date')
    tree = ttk.Treeview(records_window, columns=columns, show='headings')

    # Define column headings
    tree.heading('ID', text='ID')
    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')
    tree.heading('Gender', text='Gender')
    tree.heading('Contact', text='Contact')
    tree.heading('Address', text='Address')
    tree.heading('Registration Date', text='Registration Date')

    # Set column widths
    tree.column('ID', width=50, anchor=CENTER)
    tree.column('Name', width=150, anchor=W)
    tree.column('Age', width=50, anchor=CENTER)
    tree.column('Gender', width=100, anchor=CENTER)
    tree.column('Contact', width=120, anchor=W)
    tree.column('Address', width=200, anchor=W)
    tree.column('Registration Date', width=120, anchor=CENTER)

    # Fetch and insert data into the Treeview
    records = fetch_patients()
    for row in records:
        tree.insert('', END, values=row)

    tree.pack(fill=BOTH, expand=True)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(records_window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)


# Create a function to search_patitent window
def search_patient_window():
    search_window = Toplevel()
    search_window.title("Search Patient Records")
    search_window.geometry("700x450")

    # Header
    Label(search_window, text="Search Patient Records", font=("Arial", 18, "bold")).place(x=200, y=10)

    # Patient ID Input
    Label(search_window, text="Enter Patient ID (Optional):", font=("Arial", 12)).place(x=50, y=80)
    id_entry = Entry(search_window, font=("Arial", 12), width=30)
    id_entry.place(x=300, y=80)

    # Patient Name Input
    Label(search_window, text="Enter Patient Name:", font=("Arial", 12)).place(x=50, y=130)
    name_entry = Entry(search_window, font=("Arial", 12), width=30)
    name_entry.place(x=300, y=130)

    # Status Label
    status_label = Label(search_window, text="", font=("Arial", 10))
    status_label.place(x=200, y=180)

    def perform_search():
        # Clear any previous messages
        status_label.config(text="", fg="black")

        patient_id = id_entry.get().strip()
        patient_name = name_entry.get().strip()

        if not patient_name:
            status_label.config(text="Patient Name cannot be empty!", fg="red")
            return

        # Fetch search results based on input
        from Database.database import search_patient_records
        results = search_patient_records(patient_id, patient_name)

        if not results:
            status_label.config(
                text="No patient found with the given details. Please check the Name or ID.", fg="red"
            )
            return

        # Clear the status label on successful search
        status_label.config(text="")

        # Display results
        results_window = Toplevel()
        results_window.title("Search Results")
        results_window.geometry("900x400")

        # Table to Display Results
        columns = ('ID', 'Name', 'Age', 'Gender', 'Contact', 'Address', 'Registration Date')
        tree = ttk.Treeview(results_window, columns=columns, show='headings')

        tree.heading('ID', text='ID')
        tree.heading('Name', text='Name')
        tree.heading('Age', text='Age')
        tree.heading('Gender', text='Gender')
        tree.heading('Contact', text='Contact')
        tree.heading('Address', text='Address')
        tree.heading('Registration Date', text='Registration Date')

        tree.column('ID', width=50, anchor=CENTER)
        tree.column('Name', width=150, anchor=W)
        tree.column('Age', width=50, anchor=CENTER)
        tree.column('Gender', width=100, anchor=CENTER)
        tree.column('Contact', width=120, anchor=W)
        tree.column('Address', width=200, anchor=W)
        tree.column('Registration Date', width=120, anchor=CENTER)

        for row in results:
            tree.insert('', END, values=row)

        tree.place(x=10, y=10, width=850, height=350)

        # Scrollbar
        scrollbar = ttk.Scrollbar(results_window, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=860, y=10, height=350)

    # Search Button
    Button(search_window, text="Search", font=("Arial", 14, "bold"), bg="#27AE60", fg="#FFFFFF",
           width=15, command=perform_search).place(x=200, y=250)

    # Close Button
    Button(search_window, text="Close", font=("Arial", 14, "bold"), bg="#C0392B", fg="#FFFFFF",
           width=15, command=search_window.destroy).place(x=200, y=310)


# Create a window to open _cashier
def open_cashier():
    cashier_window = Toplevel()
    cashier_window.title("Cashier - Hospital Management System")
    cashier_window.geometry("1120x600")

    # Header Label
    header_label = Label(cashier_window, text="Cashier Dashboard", font=("Arial", 18, "bold"))
    header_label.place(x=300, y=10)

    # Add Payment Section
    add_payment_label = Label(cashier_window, text="Add New Payment", font=("Arial", 14, "bold"))
    add_payment_label.place(x=50, y=50)

    # Fetch patient names for the dropdown
    from Database.database import fetch_patients, add_payment, fetch_payments
    patient_records = fetch_patients()
    patient_names = [record[1] for record in patient_records]  # Extract patient names

    Label(cashier_window, text="Select Patient Name:", font=("Arial", 12)).place(x=50, y=100)
    patient_dropdown = ttk.Combobox(cashier_window, values=patient_names, font=("Arial", 12), width=28, state="readonly")
    patient_dropdown.set("Select Patient")
    patient_dropdown.place(x=280, y=100)

    # Display patient details when selected
    def display_patient_details(event):
        selected_name = patient_dropdown.get()
        for record in patient_records:
            if record[1] == selected_name:  # Match patient name
                patient_details_label.config(
                    text=f"ID: {record[0]}\n"
                         f"Age: {record[2]}\n"
                         f"Gender: {record[3]}\n"
                         f"Contact: {record[4]}\n"
                         f"Address: {record[5]}\n"
                         f"Registration Date: {record[6]}"
                )
                break

    patient_dropdown.bind("<<ComboboxSelected>>", display_patient_details)

    patient_details_label = Label(cashier_window, text="", font=("Arial", 12), justify=LEFT)
    patient_details_label.place(x=50, y=150)

    # Amount Paid
    Label(cashier_window, text="Amount Paid:", font=("Arial", 12)).place(x=50, y=300)
    amount_paid_entry = Entry(cashier_window, font=("Arial", 12), width=30)
    amount_paid_entry.place(x=280, y=300)

    # Payment Date
    Label(cashier_window, text="Payment Date (YYYY-MM-DD):", font=("Arial", 12)).place(x=50, y=350)
    payment_date_entry = Entry(cashier_window, font=("Arial", 12), width=30)
    payment_date_entry.place(x=280, y=350)

    # Payment Mode
    Label(cashier_window, text="Payment Mode (Cash/Card):", font=("Arial", 12)).place(x=50, y=400)
    payment_mode_entry = Entry(cashier_window, font=("Arial", 12), width=30)
    payment_mode_entry.place(x=280, y=400)

    # Save Payment Button
    def save_payment():
        patient_name = patient_dropdown.get()
        amount_paid = amount_paid_entry.get()
        payment_date = payment_date_entry.get()
        payment_mode = payment_mode_entry.get()

        if patient_name == "Select Patient" or not amount_paid or not payment_date or not payment_mode:
            error_label = Label(cashier_window, text="Please fill all fields!", fg="red", font=("Arial", 10))
            error_label.place(x=200, y=450)
            return

        try:
            amount_paid = float(amount_paid)  # Ensure the amount is numeric
            add_payment(patient_name, amount_paid, payment_date, payment_mode)
            success_label = Label(cashier_window, text="Payment Saved Successfully!", fg="green", font=("Arial", 10))
            success_label.place(x=200, y=450)
            amount_paid_entry.delete(0, END)
            payment_date_entry.delete(0, END)
            payment_mode_entry.delete(0, END)
        except ValueError:
            error_label = Label(cashier_window, text="Amount Paid must be a number!", fg="red", font=("Arial", 10))
            error_label.place(x=200, y=450)

    Button(cashier_window, text="Save Payment", font=("Arial", 14, "bold"), bg="#27AE60", fg="#FFFFFF",
           width=15, command=save_payment).place(x=200, y=500)

    # View Payments Section
    view_payments_label = Label(cashier_window, text="All Payment Records", font=("Arial", 14, "bold"))
    view_payments_label.place(x=700, y=40)

    columns = ('ID', 'Patient Name', 'Amount Paid', 'Payment Date', 'Payment Mode')
    tree = ttk.Treeview(cashier_window, columns=columns, show='headings')

    tree.heading('ID', text='ID')
    tree.heading('Patient Name', text='Patient Name')
    tree.heading('Amount Paid', text='Amount Paid')
    tree.heading('Payment Date', text='Payment Date')
    tree.heading('Payment Mode', text='Payment Mode')

    tree.column('ID', width=50, anchor=CENTER)
    tree.column('Patient Name', width=120, anchor=W)
    tree.column('Amount Paid', width=100, anchor=CENTER)
    tree.column('Payment Date', width=110, anchor=CENTER)
    tree.column('Payment Mode', width=120, anchor=CENTER)

    # Fetch and display payment records
    payment_records = fetch_payments()
    for record in payment_records:
        tree.insert('', END, values=record)

    tree.place(x=580, y=80, width=500, height=400)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(cashier_window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(x=1080, y=80, height=400)
