from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter
from Database.database import fetch_opd_records, fetch_ipd_records, fetch_icu_records, get_emergency_cases, fetch_patients, fetch_payments, fetch_doctors, fetch_housekeeping


# Create a new window to display data
def display_data(title, records, columns):
    """Function to display fetched data in a new window with a treeview."""
    data_window = Toplevel()
    data_window.title(title)
    data_window.geometry("800x400")
    data_window.resizable(False, False)

    # Create a treeview to display data
    tree = ttk.Treeview(data_window, columns=columns, show='headings', height=20)
    tree.pack(fill=BOTH, expand=True)

    # Configure columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=100)

    # Insert data into the treeview
    for record in records:
        tree.insert('', END, values=record)

    # Add a vertical scrollbar
    scrollbar = ttk.Scrollbar(data_window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)


# Create a new window to open_admin_dashboard
def open_admin_dashboard(login_window):
    Admin_dashboard = Toplevel()
    Admin_dashboard.title("Doctor Dashboard - Hospital Management System")
    Admin_dashboard.geometry("1000x600")
    Admin_dashboard.resizable(False, False)

    # Hide the login window
    login_window.withdraw()

    # Add the background image
    bg_image = Image.open(r"E:\Python(HMS)\Admin.png")
    bg_image = bg_image.resize((1000, 600))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(Admin_dashboard, image=bg_photo)
    bg_label.image = bg_photo  # Keep reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define button style
    button_font = ("Arial", 14, "bold")
    button_width = 200
    button_height = 40

    # Button Functions
    def show_opd_records():
        records = fetch_opd_records()
        columns = ["ID", "Patient Name", "Symptoms", "Doctor Assigned", "Date of Visit"]
        display_data("OPD Records", records, columns)

    def show_ipd_records():
        records = fetch_ipd_records()
        columns = ["ID", "Patient Name", "Room No", "Admission Date", "Discharge Date", "Doctor In Charge"]
        display_data("IPD Records", records, columns)

    def show_icu_records():
        records = fetch_icu_records()
        columns = ["ID", "Patient Name", "Room No", "Admission Date", "Discharge Date", "Doctor In Charge"]
        display_data("ICU Records", records, columns)

    def show_emergency_records():
        records = get_emergency_cases()
        columns = ["ID", "Patient Name", "Emergency Type", "Contact", "Doctor Assigned", "Arrival Time"]
        display_data("Emergency Records", records, columns)

    def show_all_patients():
        records = fetch_patients()
        columns = ["ID", "Name", "Age", "Gender", "Contact", "Address", "Date of Registration"]
        display_data("All Patients", records, columns)

    def show_payments():
        records = fetch_payments()
        columns = ["ID", "Patient Name", "Amount Paid", "Payment Date", "Payment Mode"]
        display_data("Payments", records, columns)

    def show_doctors():
        records = fetch_doctors()
        columns = ["ID", "Name", "Specialization", "Contact", "Address"]
        display_data("Doctors", records, columns)

    def show_housekeeping():
        records = fetch_housekeeping()
        columns = ["ID", "Name", "Duty", "Contact", "Shift"]
        display_data("Housekeeping Staff", records, columns)

    # Create buttons for different admin functionalities (4 on the left and 4 on the right)
    btn_opd_details = customtkinter.CTkButton(
        Admin_dashboard, text="OPD Patient Details", font=button_font, width=button_width, height=button_height,
        command=show_opd_records
    )
    btn_opd_details.place(x=50, y=150)

    btn_ipd_details = customtkinter.CTkButton(
        Admin_dashboard, text="IPD Patient Details", font=button_font, width=button_width, height=button_height,
        command=show_ipd_records
    )
    btn_ipd_details.place(x=50, y=250)

    btn_icu_details = customtkinter.CTkButton(
        Admin_dashboard, text="ICU Patient Details", font=button_font, width=button_width, height=button_height,
        command=show_icu_records
    )
    btn_icu_details.place(x=50, y=350)

    btn_emergency_details = customtkinter.CTkButton(
        Admin_dashboard, text="Emergency Patient Details", font=button_font, width=button_width, height=button_height,
        command=show_emergency_records
    )
    btn_emergency_details.place(x=50, y=450)

    btn_all_patients = customtkinter.CTkButton(
        Admin_dashboard, text="All Patients Records", font=button_font, width=button_width, height=button_height,
        command=show_all_patients
    )
    btn_all_patients.place(x=750, y=150)

    btn_billing_details = customtkinter.CTkButton(
        Admin_dashboard, text="Billing/Cashier Details", font=button_font, width=button_width, height=button_height,
        command=show_payments
    )
    btn_billing_details.place(x=750, y=250)

    btn_doctor_details = customtkinter.CTkButton(
        Admin_dashboard, text="Doctor Details", font=button_font, width=button_width, height=button_height,
        command=show_doctors
    )
    btn_doctor_details.place(x=750, y=350)

    btn_staff_details = customtkinter.CTkButton(
        Admin_dashboard, text="Housekeeping Staff Details", font=button_font, width=button_width, height=button_height,
        command=show_housekeeping
    )
    btn_staff_details.place(x=750, y=450)

    # Exit button at the center
    def close_dashboard():
        Admin_dashboard.destroy()
        login_window.deiconify()

    customtkinter.CTkButton(Admin_dashboard, text="Exit", fg_color="red", hover_color="darkred",
                            width=200, height=40, command=close_dashboard).place(x=370, y=530)
