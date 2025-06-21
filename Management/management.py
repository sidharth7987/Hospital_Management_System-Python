from tkinter import *
import customtkinter
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox, ttk
import tkinter as tk
import Database.database as database
import datetime


# Create window to Open_doctor_management
def open_doctor_management():
    doctor_window = Toplevel()
    doctor_window.title("Doctor Management")
    doctor_window.geometry("900x600")
    doctor_window.config(bg= '#161C25')
    doctor_window.minsize(900, 600)
    doctor_window.maxsize(900, 600)


    font1 = ('Arial', 20, 'bold')
    font2 = ('Arial', 16)

    # Clear all input fields
    def clear_fields():
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        specialization_entry.delete(0, END)
        contact_entry.delete(0, END)
        address_entry.delete(0, END)

    # Refresh TreeView to show updated data
    def refresh_treeview():
        doctors = database.fetch_doctors()  # Fetch all doctors from the database
        tree.delete(*tree.get_children())  # Clear the TreeView
        for doctor in doctors:
            tree.insert("", END, values=doctor)

    # Add a new doctor
    def add_doctor():
        Id = id_entry.get()
        Name = name_entry.get()
        Specialization = specialization_entry.get()
        Contact = contact_entry.get()
        Address = address_entry.get()
        
        if not (Id and Name and Specialization and Contact and Address):
            messagebox.showerror("Error", "All fields are required!")
        elif database.id_exists("Doctors", Id):  # Check if the doctor ID already exists
            messagebox.showerror("Error", "Doctor ID already exists!")
        else:
            database.insert_doctor(Id, Name, Specialization, Contact, Address)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Doctor added successfully!")

    # Update an existing doctor's details
    def update_doctor():
        Id = id_entry.get()
        Name = name_entry.get()
        Specialization = specialization_entry.get()
        Contact = contact_entry.get()
        Address = address_entry.get()
        
        if not (Id and Name and Specialization and Contact and Address):
            messagebox.showerror("Error", "All fields are required!")
        else:
            database.update_doctor(Id, Name, Specialization, Contact, Address)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Doctor updated successfully!")


    # Delete a doctor
    def delete_doctor():
        Id = id_entry.get()
        if not Id:
            messagebox.showerror("Error", "Enter Doctor ID to delete!")
        else:
            database.delete_doctor(Id)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Doctor deleted successfully!")

    # Show all doctors in the TreeView
    def show_all_doctors():
        refresh_treeview()
        messagebox.showinfo("Info", "All doctor details have been refreshed.")

    # Display selected doctor data in the input fields
    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            values = tree.item(selected_item, "values")
            clear_fields()
            id_entry.insert(0, values[0])
            name_entry.insert(0, values[1])
            specialization_entry.insert(0, values[2])
            contact_entry.insert(0, values[3])
            address_entry.insert(0, values[4])

    # Doctor_id Button
    id_label = customtkinter.CTkLabel(doctor_window, font= font1, text= 'Doctor_Id: ', text_color= '#fff', bg_color= '#161C25' )
    id_label.place(x= 10, y= 20)
    id_entry = customtkinter.CTkEntry(doctor_window, font= font2, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    id_entry.place(x= 160, y= 20)

    # Name Button
    name_label = customtkinter.CTkLabel(doctor_window, font= font1, text= 'Name: ', text_color= '#fff', bg_color= '#161C25')
    name_label.place(x= 10, y= 80)
    name_entry = customtkinter.CTkEntry(doctor_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    name_entry.place(x= 160, y= 80)

    # Specialization Button
    specialization_label = customtkinter.CTkLabel(doctor_window, font= font1, text= 'Specialization: ', text_color= '#fff', bg_color= '#161C25')
    specialization_label.place(x= 10, y= 140)
    specialization_entry = customtkinter.CTkEntry(doctor_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    specialization_entry.place(x= 160, y= 140)

    # Contact Button
    contact_label = customtkinter.CTkLabel(doctor_window, font= font1, text= 'Contact: ', text_color= '#fff', bg_color= '#161C25')
    contact_label.place(x= 10, y= 200)
    contact_entry = customtkinter.CTkEntry(doctor_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    contact_entry.place(x= 160, y= 200)

    # address Button
    address_label = customtkinter.CTkLabel(doctor_window, font= font1, text= 'Address: ', text_color= '#fff', bg_color= '#161C25')
    address_label.place(x=10, y= 260)
    address_entry = customtkinter.CTkEntry(doctor_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    address_entry.place(x= 160, y= 260)

    # add_doctor Button
    add_button = customtkinter.CTkButton(doctor_window, command= add_doctor, font = font1, text_color= '#fff',text= 'Add Doctor', fg_color= '#05A312', hover_color= '#00850B', bg_color= '#161C25', cursor= 'hand2', corner_radius= 15, width= 260)
    add_button.place(x= 450, y= 40)

    # Clear_field Button
    clear_button = customtkinter.CTkButton(doctor_window, command= clear_fields, font = font1, text_color= '#fff',text= 'New Doctor', fg_color= '#161C25', hover_color= '#FF5002', bg_color= '#161C25',border_color= '#F15704',border_width= 2, cursor= 'hand2', corner_radius= 15, width= 260)
    clear_button.place(x= 450, y= 100)

    # Update_doctor Button
    update_button = customtkinter.CTkButton(doctor_window, command=update_doctor, font = font1, text_color= '#fff',text= 'Update Doctor', fg_color= '#161C25', hover_color= '#FF5002', bg_color= '#161C25',border_color= '#F15704',border_width= 2, cursor= 'hand2', corner_radius= 15, width= 260)
    update_button.place(x= 450, y= 160)

    # Delete_doctor Button
    delete_button = customtkinter.CTkButton(doctor_window,command= delete_doctor,  font = font1, text_color= '#fff',text= 'Delete Doctor', fg_color= '#E40404', hover_color= '#AE0000', bg_color= '#161C25',border_color= '#F40404',border_width= 2, cursor= 'hand2', corner_radius= 15, width= 260)
    delete_button.place(x= 450, y= 220)


    style = ttk.Style(doctor_window)

    style.theme_use('clam')
    style.configure('Treeview', font = font2, foreground= '#fff', background= '#000', fieldbackground= '#313837')
    style.map('Treeview', background= [('selected', '#1A8F2D')])

    tree = ttk.Treeview(doctor_window, height= 13)

    tree['columns'] = ('ID', 'Name', 'Specialization', 'Contact', 'Address')

    tree.column('#0', width= 0, stretch= tk.NO)     # Hide the default first coloumn
    tree.column('ID', anchor= tk.CENTER, width= 100)
    tree.column('Name', anchor= tk.CENTER, width= 200)
    tree.column('Specialization', anchor= tk.CENTER, width= 150)
    tree.column('Contact', anchor= tk.CENTER, width= 180)
    tree.column('Address', anchor= tk.CENTER, width= 240)


    tree.heading('ID', text= 'ID')
    tree.heading('Name', text= 'Name')
    tree.heading('Specialization', text= 'Specialization')
    tree.heading('Contact', text= 'Contact')
    tree.heading('Address', text= 'Address')

    tree.place(x= 10, y= 310)

    tree.bind('<ButtonRelease>', display_data)

    refresh_treeview()


# Create window to open_patient_management
def open_patient_management():
    patient_window = Toplevel()
    patient_window.title("Patient Management")
    patient_window.geometry("1000x600")
    patient_window.config(bg= '#161C25')
    patient_window.minsize(900, 700)
    patient_window.maxsize(9000, 700)

    font1 = ('Arial', 20, 'bold')
    font2 = ('Arial', 16)

    # Clear all input fields
    def clear_fields():
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        gender_var.set("Male")
        contact_entry.delete(0, END)
        address_entry.delete(0, END)

    # Refresh TreeView to show updated data
    def refresh_treeview():
        patients = database.fetch_patients()  # Fetch all patients from the database
        tree.delete(*tree.get_children())  # Clear the TreeView
        for patient in patients:
            tree.insert("", END, values=patient)

    # Add a new patient
    def add_patient():
        Id = id_entry.get()
        Name = name_entry.get()
        Age = age_entry.get()
        Gender = gender_var.get()
        Contact = contact_entry.get()
        Address = address_entry.get()
        Date_of_Registration = datetime.date.today().strftime("%Y-%m-%d")
        
        if not (Id and Name and Age and Gender and Contact and Address):
            messagebox.showerror("Error", "All fields are required!")
        elif database.patient_id_exists(Id):  # Check if the patient ID already exists
            messagebox.showerror("Error", "Patient ID already exists!")
        else:
            database.register_patient_in_db(Id, Name, Age, Gender, Contact, Address, Date_of_Registration)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Patient added successfully!")


    # Update an existing patient's details
    def update_patient():
        Id = id_entry.get()
        Name = name_entry.get()
        Age = age_entry.get()
        Gender = gender_var.get()
        Contact = contact_entry.get()
        Address = address_entry.get()
        
        if not (Id and Name and Age and Gender and Contact and Address):
            messagebox.showerror("Error", "All fields are required!")
        else:
            database.update_patient(Id, Name, Age, Gender, Contact, Address)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Patient updated successfully!")

    # Delete a patient
    def delete_patient():
        Id = id_entry.get()
        if not Id:
            messagebox.showerror("Error", "Enter Patient ID to delete!")
        else:
            database.delete_patient(Id)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Patient deleted successfully!")

    # Show all patients in the TreeView
    def show_all_patients():
        refresh_treeview()
        messagebox.showinfo("Info", "All patient details have been refreshed.")

    # Display selected patient data in the input fields
    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            values = tree.item(selected_item, "values")
            clear_fields()
            id_entry.insert(0, values[0])
            name_entry.insert(0, values[1])
            age_entry.insert(0, values[2])
            gender_var.set(values[3])
            contact_entry.insert(0, values[4])
            address_entry.insert(0, values[5])


    # Patient_id Button
    id_label = customtkinter.CTkLabel(patient_window, font= font1, text= 'Patient_Id: ', text_color= '#fff', bg_color= '#161C25' )
    id_label.place(x= 10, y= 20)
    id_entry = customtkinter.CTkEntry(patient_window, font= font2, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    id_entry.place(x= 160, y= 20)

    # Name Button
    name_label = customtkinter.CTkLabel(patient_window, font= font1, text= 'Name: ', text_color= '#fff', bg_color= '#161C25')
    name_label.place(x= 10, y= 80)
    name_entry = customtkinter.CTkEntry(patient_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    name_entry.place(x= 160, y= 80)

    # Age Button
    age_label = customtkinter.CTkLabel(patient_window, font= font1, text= 'Age: ', text_color= '#fff', bg_color= '#161C25')
    age_label.place(x= 10, y= 140)
    age_entry = customtkinter.CTkEntry(patient_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    age_entry.place(x= 160, y= 140)

    # Gender Button
    gender_label = customtkinter.CTkLabel(patient_window, font= font1, text= 'Gender: ', text_color= '#fff', bg_color= '#161C25')
    gender_label.place(x= 10, y= 200)
    gender_var = StringVar(value= 'Male')
    gender_menu = OptionMenu(patient_window, gender_var, "Male", "Female", "Other")
    gender_menu.place(x= 160, y= 200)

    # Contact Button
    contact_label = customtkinter.CTkLabel(patient_window, font= font1, text= 'Contact: ', text_color= '#fff', bg_color= '#161C25')
    contact_label.place(x= 10, y= 260)
    contact_entry = customtkinter.CTkEntry(patient_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    contact_entry.place(x= 160, y= 260)

    # address Button
    address_label = customtkinter.CTkLabel(patient_window, font= font1, text= 'Address: ', text_color= '#fff', bg_color= '#161C25')
    address_label.place(x=10, y= 320)
    address_entry = customtkinter.CTkEntry(patient_window, font= font1, text_color= '#000', fg_color= '#fff', border_color= '#0C9295', border_width= 2, width= 180)
    address_entry.place(x= 160, y= 320)

    # add_patient Button
    add_button = customtkinter.CTkButton(patient_window, command= add_patient, font = font1, text_color= '#fff',text= 'Add Patient', fg_color= '#05A312', hover_color= '#00850B', bg_color= '#161C25', cursor= 'hand2', corner_radius= 15, width= 260)
    add_button.place(x= 450, y= 40)

    # Clear_fields Button
    clear_button = customtkinter.CTkButton(patient_window, command= clear_fields, font = font1, text_color= '#fff',text= 'New patient', fg_color= '#161C25', hover_color= '#FF5002', bg_color= '#161C25',border_color= '#F15704',border_width= 2, cursor= 'hand2', corner_radius= 15, width= 260)
    clear_button.place(x= 450, y= 100)

    # update_patient Button
    update_button = customtkinter.CTkButton(patient_window, command=update_patient, font = font1, text_color= '#fff',text= 'Update Patient', fg_color= '#161C25', hover_color= '#FF5002', bg_color= '#161C25',border_color= '#F15704',border_width= 2, cursor= 'hand2', corner_radius= 15, width= 260)
    update_button.place(x= 450, y= 160)

    # Delete_patient Button
    delete_button = customtkinter.CTkButton(patient_window,command= delete_patient,  font = font1, text_color= '#fff',text= 'Delete patient', fg_color= '#E40404', hover_color= '#AE0000', bg_color= '#161C25',border_color= '#F40404',border_width= 2, cursor= 'hand2', corner_radius= 15, width= 260)
    delete_button.place(x= 450, y= 220)


    style = ttk.Style(patient_window)

    style.theme_use('clam')
    style.configure('Treeview', font = font2, foreground= '#fff', background= '#000', fieldbackground= '#313837')
    style.map('Treeview', background= [('selected', '#1A8F2D')])

    tree = ttk.Treeview(patient_window, height= 13)

    tree['columns'] = ('ID', 'Name', 'Age', 'Gender', 'Contact', 'Address')

    tree.column('#0', width= 0, stretch= tk.NO)     # Hide the default first coloumn
    tree.column('ID', anchor= tk.CENTER, width= 80)
    tree.column('Name', anchor= tk.CENTER, width= 200)
    tree.column('Age', anchor= tk.CENTER, width= 80)
    tree.column('Gender', anchor= tk.CENTER, width= 100)
    tree.column('Contact', anchor= tk.CENTER, width= 180)
    tree.column('Address', anchor= tk.CENTER, width= 240)


    tree.heading('ID', text= 'ID')
    tree.heading('Name', text= 'Name')
    tree.heading('Age', text= 'Age')
    tree.heading('Gender', text= 'Gender')
    tree.heading('Contact', text= 'Contact')
    tree.heading('Address', text= 'Address')

    tree.place(x= 10, y= 380)

    tree.bind('<ButtonRelease>', display_data)

    refresh_treeview()


# Create a window to open_housekeeping_management
def open_housekeeping_management():
    housekeeping_window = Toplevel()
    housekeeping_window.title("Housekeeping Management")
    housekeeping_window.geometry("1000x600")
    housekeeping_window.config(bg='#161C25')
    housekeeping_window.minsize(900, 700)
    housekeeping_window.maxsize(9000, 700)

    font1 = ('Arial', 20, 'bold')
    font2 = ('Arial', 16)

    # Clear all input fields
    def clear_fields():
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        Duty_entry.delete(0, END)
        contact_entry.delete(0, END)
        Shift_var.set("Morning")

    # Refresh TreeView to show updated data
    def refresh_treeview():
        housekeeping_staff = database.fetch_housekeeping()  # Fetch all staff from the database
        tree.delete(*tree.get_children())  # Clear the TreeView
        for staff in housekeeping_staff:
            tree.insert("", END, values=staff)

    # Add a new staff member
    def add_staff():
        Id = id_entry.get()
        Name = name_entry.get()
        Duty = Duty_entry.get()
        Contact = contact_entry.get()
        Shift = Shift_var.get()

        if not (Id and Name and Shift and Contact and Duty):
            messagebox.showerror("Error", "All fields are required!")
        elif database.housekeeping_id_exists(Id):  # Check if the staff ID already exists
            messagebox.showerror("Error", "Staff ID already exists!")
        else:
            database.register_housekeeping_in_db(Id, Name, Duty, Contact, Shift)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Staff added successfully!")

    # Update an existing staff member's details
    def update_staff():
        Id = id_entry.get()
        Name = name_entry.get()
        Duty = Duty_entry.get()
        Contact = contact_entry.get()
        Shift = Shift_var.get()

        if not (Id and Name and Shift and Contact and Duty):
            messagebox.showerror("Error", "All fields are required!")
        else:
            database.update_housekeeping(Id, Name, Shift, Contact, Duty)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Staff updated successfully!")

    # Delete a staff member
    def delete_staff():
        Id = id_entry.get()
        if not Id:
            messagebox.showerror("Error", "Enter Staff ID to delete!")
        else:
            database.delete_housekeeping(Id)
            refresh_treeview()
            clear_fields()
            messagebox.showinfo("Success", "Staff deleted successfully!")

    # Show all staff members in the TreeView
    def show_all_staff():
        refresh_treeview()
        messagebox.showinfo("Info", "All housekeeping staff details have been refreshed.")

    # Display selected staff data in the input fields
    def display_data(event):
        selected_item = tree.focus()
        if selected_item:
            values = tree.item(selected_item, "values")
            clear_fields()
            id_entry.insert(0, values[0])
            name_entry.insert(0, values[1])
            Duty_entry.insert(0, values[2])
            contact_entry.insert(0, values[3])
            Shift_var.set(values[4])


    # Staff_id Button
    id_label = customtkinter.CTkLabel(housekeeping_window, font=font1, text='Staff ID: ', text_color='#fff', bg_color='#161C25')
    id_label.place(x=10, y=20)
    id_entry = customtkinter.CTkEntry(housekeeping_window, font=font2, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
    id_entry.place(x=160, y=20)

    # Name Button
    name_label = customtkinter.CTkLabel(housekeeping_window, font=font1, text='Name: ', text_color='#fff', bg_color='#161C25')
    name_label.place(x=10, y=80)
    name_entry = customtkinter.CTkEntry(housekeeping_window, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
    name_entry.place(x=160, y=80)

    # Duty button
    Duty_label = customtkinter.CTkLabel(housekeeping_window, font=font1, text='Duty: ', text_color='#fff', bg_color='#161C25')
    Duty_label.place(x=10, y=140)
    Duty_entry = customtkinter.CTkEntry(housekeeping_window, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
    Duty_entry.place(x=160, y=140)

    # Contact Button
    contact_label = customtkinter.CTkLabel(housekeeping_window, font=font1, text='Contact: ', text_color='#fff', bg_color='#161C25')
    contact_label.place(x=10, y=200)
    contact_entry = customtkinter.CTkEntry(housekeeping_window, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
    contact_entry.place(x=160, y=200)

    # Shift Button
    Shift_label = customtkinter.CTkLabel(housekeeping_window, font=font1, text='Shift: ', text_color='#fff', bg_color='#161C25')
    Shift_label.place(x=10, y=260)
    Shift_var = StringVar(value='Morning')
    Shift_menu = OptionMenu(housekeeping_window,  Shift_var, "Morning", "Evening", "Night")
    Shift_menu.place(x=160, y=260)

    # add_staff Button
    add_button = customtkinter.CTkButton(housekeeping_window, command=add_staff, font=font1, text_color='#fff', text='Add Staff', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', cursor='hand2', corner_radius=15, width=260)
    add_button.place(x=450, y=40)

    # Clear_staff Button
    clear_button = customtkinter.CTkButton(housekeeping_window, command=clear_fields, font=font1, text_color='#fff', text='New Entry', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25', border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=260)
    clear_button.place(x=450, y=100)

    # update_staff Button
    update_button = customtkinter.CTkButton(housekeeping_window, command=update_staff, font=font1, text_color='#fff', text='Update Staff', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25', border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=260)
    update_button.place(x=450, y=160)

    # Delete_staff Button
    delete_button = customtkinter.CTkButton(housekeeping_window, command=delete_staff, font=font1, text_color='#fff', text='Delete Staff', fg_color='#E40404', hover_color='#AE0000', bg_color='#161C25', border_color='#F40404', border_width=2, cursor='hand2', corner_radius=15, width=260)
    delete_button.place(x=450, y=220)

    style = ttk.Style(housekeeping_window)
    style.theme_use('clam')
    style.configure('Treeview', font=font2, foreground='#fff', background='#000', fieldbackground='#313837')
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    tree = ttk.Treeview(housekeeping_window, height=13)

    tree['columns'] = ('ID', 'Name', 'Duty', 'Contact', 'Shift')

    tree.column('#0', width=0, stretch=tk.NO)  # Hide the default first column
    tree.column('ID', anchor=tk.CENTER, width=80)
    tree.column('Name', anchor=tk.CENTER, width=200)
    tree.column('Duty', anchor=tk.CENTER, width=200)
    tree.column('Contact', anchor=tk.CENTER, width=180)
    tree.column('Shift', anchor=tk.CENTER, width=150)

    tree.heading('ID', text='ID')
    tree.heading('Name', text='Name')
    tree.heading('Duty', text='Duty')
    tree.heading('Contact', text='Contact')
    tree.heading('Shift', text='Shift')

    tree.place(x=10, y=350)

    tree.bind('<ButtonRelease>', display_data)

    refresh_treeview()


# Create a window to open_management_dashboard
def open_management_dashboard(login_window):
    management_dashboard = Toplevel()
    management_dashboard.title("Management Dashboard - Hospital Management System")
    management_dashboard.geometry("1000x600")
    management_dashboard.maxsize(1000, 600)
    management_dashboard.minsize(1000, 600)

    # hide the login window
    login_window.withdraw()

    # Add the background image in reception Dashboard
    bg_image = Image.open(r"E:\Python(HMS)\Management.png")
    bg_image = bg_image.resize((1000, 600))
    bg_photo = ImageTk.PhotoImage(bg_image)
    management_dashboard.bg = bg_photo 
    bg_label = Label(management_dashboard, image=management_dashboard.bg)
    bg_label.place(x=0, y=0, relheight=1, relwidth=1)

    # Button design settings
    button_width = 280
    button_height = 60
    button_font = ("Arial", 16, "bold")

    def create_glass_button(text, y, command=None):
        button = customtkinter.CTkButton(management_dashboard, text= text, text_color= "#FFFFFF",  font= button_font, fg_color= "#2C3E50", hover_color= "#34495E", corner_radius= 15, width= button_width, height= button_height, border_width= 2, border_color= "#FFFFFF", command= command)
        button.place(x=360, y=y)
        return button
    
    # Doctor Management
    create_glass_button("🩺 Doctor Management",  y= 130, command= open_doctor_management)

    # Patient Management
    create_glass_button("🙍 Patient Management",  y= 250, command= open_patient_management)

    # HouseKepping Management
    create_glass_button("🧝 Housekeeping Management", y= 370, command= open_housekeeping_management)

    # Exit
    def exit_and_return():
        management_dashboard.destroy()
        login_window.deiconify()

    create_glass_button("🚪 Exit", y=490, command=exit_and_return)




