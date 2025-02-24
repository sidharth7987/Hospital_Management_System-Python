from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox
from Reception.reception import open_reception_dashboard
from Management.management import open_management_dashboard
from Admin.admin import open_admin_dashboard
from Doctor.doctor import open_doctor_dashboard


# Create a main window of Hospital_Management_Syatem which is basically a login page.
win = Tk()
win.title("🏨 Hospital Management System 🏨")
win.geometry("1000x500")
win.maxsize(1000, 500)
win.minsize(1000, 500)

bg_image = Image.open(r"E:\Python(HMS)\Hospital.png")
bg_image = bg_image.resize((1000, 500))
bg = ImageTk.PhotoImage(bg_image)
bg_label = Label(win, image= bg)
bg_label.place(x= 0, y= 0, relheight= 1, relwidth= 1)


# Function to validate login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()

    # Credentials for each role
    credentials = {
        "Admin": {"username": "Sidharth", "password": "sidharth7987"},
        "Doctor": {"username": "Psycho", "password": "psycho123"}, 
        "Receptionist": {"username": "Nature", "password": "nature123"},
        "Management": {"username": "Management", "password": "management123"}
    }

    # validate the credentials
    if role in credentials:
        if username == credentials[role]["username"] and password == credentials[role]["password"]:
            messagebox.showinfo("login Success", f"Welcome, {role}!")

            # Redirect to role-specific dashboard here
            if role == "Admin":
                open_admin_dashboard()
            elif role == "Doctor":
                open_doctor_dashboard()
            elif role == "Receptionist":
                open_reception_dashboard()
            elif role == "Management":
                open_management_dashboard()
        
        else:
            messagebox.showerror("Login Failed !", "Invaild username or Password")
            
    else:
        messagebox.showerror("Login Failed !", "Please select s valid role")          



login_frame = Frame(win, bg="white", bd=5, relief=RIDGE)
login_frame.place(x=310, y=130, width=400, height=300)

# Username Label and Entry
username_label = Label(login_frame, text="Username:", font=("Arial", 12, 'bold'), bg="white")
username_label.place(x=30, y=20)
username_entry = ttk.Entry(login_frame, font=("Arial", 12))
username_entry.place(x=155, y=20)

# Password Label and Entry
password_label = Label(login_frame, text="Password:", font=("Arial", 12, 'bold'), bg="white")
password_label.place(x=30, y=80)
password_entry = ttk.Entry(login_frame, font=("Arial", 12), show="*")
password_entry.place(x=155, y=80)

# Role Label and Dropdown
role_label = Label(login_frame, text="Role:", font=("Arial", 12, 'bold'), bg="white")
role_label.place(x=30, y=140)
role_var = StringVar()
role_var.set("Select Role")
role_dropdown = OptionMenu(login_frame, role_var, "Admin", "Doctor", "Receptionist", "Management")
role_dropdown.config(font=("Arial", 10, 'bold'), width=15)
role_dropdown.place(x=155, y=140)

# Login Button
login_button = Button(login_frame, text="Login !", font=("Arial", 12, 'bold'), bg="Green", fg="white", width= 10, height= 1, command=validate_login)
login_button.place(x=100, y=220)


win.mainloop()