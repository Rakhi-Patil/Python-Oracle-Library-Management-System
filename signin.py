from tkinter import *
from tkinter import messagebox
from database import get_connection

# ---------------- Register Function ---------------- #

def register_user():
    name = name_var.get().strip()
    email = email_var.get().strip()
    contact = contact_var.get().strip()
    address = address_var.get().strip()
    password = password_var.get().strip()
    confirm = confirm_var.get().strip()

    # Validation
    if name == "" or email == "" or contact == "" or address == "" or password == "" or confirm == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    conn = get_connection()

    if conn is None:
        messagebox.showerror("Error", "Database Connection Failed")
        return

    cursor = conn.cursor()

    # Check duplicate email
    cursor.execute(
        "SELECT COUNT(*) FROM customer WHERE email = :1",
        [email]
    )

    count = cursor.fetchone()[0]

    if count > 0:
        messagebox.showerror("Error", "Email already exists")
        cursor.close()
        conn.close()
        return

    # Insert customer
    cursor.execute("""
        INSERT INTO customer
        (name,email,contact,address,password)
        VALUES
        (:1,:2,:3,:4,:5)
    """, [name, email, contact, address, password])

    conn.commit()

    messagebox.showinfo("Success", "Registration Successful!")

    # Clear fields
    name_var.set("")
    email_var.set("")
    contact_var.set("")
    address_var.set("")
    password_var.set("")
    confirm_var.set("")

    cursor.close()
    conn.close()

    root.destroy()

    from login import login_user
    login_user()


# ---------------- Window ---------------- #

root = Tk()
root.title("Customer Registration")
root.geometry("980x720")
root.configure(bg="#EAF4FF")
root.resizable(False, False)

# ================= LEFT PANEL ================= #

left_frame = Frame(root, bg="#0F4C81", width=360)
left_frame.pack(side=LEFT, fill=Y)

Label(
    left_frame,
    text="Library\nManagement\nSystem",
    bg="#0F4C81",
    fg="white",
    font=("Segoe UI", 28, "bold"),
    justify="left"
).place(x=40, y=80)

Label(
    left_frame,
    text="Create your account to\naccess the library system\nsecurely.",
    bg="#0F4C81",
    fg="#D6EAF8",
    font=("Segoe UI", 12),
    justify="left"
).place(x=40, y=230)

Label(
    left_frame,
    text="Safe • Secure • Reliable",
    bg="#0F4C81",
    fg="white",
    font=("Segoe UI", 11)
).place(x=40, y=520)

# ================= RIGHT PANEL ================= #

right_frame = Frame(root, bg="white")
right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

Label(
    right_frame,
    text="Create Account",
    bg="white",
    fg="#0F4C81",
    font=("Segoe UI", 24, "bold")
).pack(pady=(30, 5))

Label(
    right_frame,
    text="Fill in the details below",
    bg="white",
    fg="gray",
    font=("Segoe UI", 11)
).pack()

form = Frame(right_frame, bg="white")
form.pack(pady=20)

# Variables
name_var = StringVar()
email_var = StringVar()
contact_var = StringVar()
address_var = StringVar()
password_var = StringVar()
confirm_var = StringVar()

label_font = ("Segoe UI", 10, "bold")
entry_font = ("Segoe UI", 11)

# ---------------- Name ---------------- #

Label(form, text="Full Name", bg="white", fg="#0F4C81",
      font=label_font).grid(row=0, column=0, sticky="w", pady=(8, 3))

Entry(
    form,
    textvariable=name_var,
    font=entry_font,
    width=35,
    bd=2,
    relief=GROOVE
).grid(row=1, column=0, ipady=6)

# ---------------- Email ---------------- #

Label(form, text="Email Address", bg="white", fg="#0F4C81",
      font=label_font).grid(row=2, column=0, sticky="w", pady=(12, 3))

Entry(
    form,
    textvariable=email_var,
    font=entry_font,
    width=35,
    bd=2,
    relief=GROOVE
).grid(row=3, column=0, ipady=6)

# ---------------- Contact ---------------- #

Label(form, text="Contact Number", bg="white", fg="#0F4C81",
      font=label_font).grid(row=4, column=0, sticky="w", pady=(12, 3))

Entry(
    form,
    textvariable=contact_var,
    font=entry_font,
    width=35,
    bd=2,
    relief=GROOVE
).grid(row=5, column=0, ipady=6)

# ---------------- Address ---------------- #

Label(form, text="Address", bg="white", fg="#0F4C81",
      font=label_font).grid(row=6, column=0, sticky="w", pady=(12, 3))

Entry(
    form,
    textvariable=address_var,
    font=entry_font,
    width=35,
    bd=2,
    relief=GROOVE
).grid(row=7, column=0, ipady=6)

# ---------------- Password ---------------- #

Label(form, text="Password", bg="white", fg="#0F4C81",
      font=label_font).grid(row=8, column=0, sticky="w", pady=(12, 3))

Entry(
    form,
    textvariable=password_var,
    show="*",
    font=entry_font,
    width=35,
    bd=2,
    relief=GROOVE
).grid(row=9, column=0, ipady=6)

# ---------------- Confirm Password ---------------- #

Label(form, text="Confirm Password", bg="white", fg="#0F4C81",
      font=label_font).grid(row=10, column=0, sticky="w", pady=(12, 3))

Entry(
    form,
    textvariable=confirm_var,
    show="*",
    font=entry_font,
    width=35,
    bd=2,
    relief=GROOVE
).grid(row=11, column=0, ipady=6)

# ---------------- Register Button ---------------- #

Button(
    right_frame,
    text="CREATE ACCOUNT",
    command=register_user,
    bg="#1565C0",
    fg="white",
    activebackground="#0D47A1",
    activeforeground="white",
    font=("Segoe UI", 11, "bold"),
    relief=FLAT,
    bd=0,
    cursor="hand2",
    width=28,
    pady=10
).pack(pady=25)

root.mainloop()


