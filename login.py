from tkinter import *
from tkinter import messagebox
from database import get_connection


# ---------------- Login Function ---------------- #

def login_user():
    email = email_var.get().strip()
    password = password_var.get().strip()

    if email == "" or password == "":
        messagebox.showerror("Error", "Please enter Email and Password")
        return

    conn = get_connection()

    if conn is None:
        messagebox.showerror("Error", "Database Connection Failed")
        return

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM customer
        WHERE email=:1 AND password=:2
    """, [email, password])

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        messagebox.showinfo("Success", "Login Successful")

        root.destroy()

        from dashboard import dashboard
        dashboard(user)

    else:
        messagebox.showerror("Error", "Invalid Email or Password")


# ---------------- Open Register ---------------- #

def open_register():
    root.destroy()

    from signin import register_user
    register_user()


# ---------------- UI ---------------- #

root = Tk()
root.title("Login")
root.geometry("900x550")
root.configure(bg="#EAF4FF")
root.resizable(False, False)

# ================= Left Side ================= #

left_frame = Frame(root, bg="#0F4C81", width=350)
left_frame.pack(side=LEFT, fill=Y)

Label(
    left_frame,
    text="Library\nManagement\nSystem",
    font=("Segoe UI", 25, "bold"),
    fg="white",
    bg="#0F4C81",
    justify="left"
).place(x=40, y=100)

Label(
    left_frame,
    text="\nManage your library\nsecurely and efficiently.",
    font=("Segoe UI", 12),
    fg="#D6EAF8",
    bg="#0F4C81",
    justify="left"
).place(x=40, y=240)

Label(
    left_frame,
    text="Rakhi Patil",
    font=("Segoe UI", 10),
    fg="white",
    bg="#0F4C81"
).place(x=70, y=500)

# ================= Right Side ================= #

right_frame = Frame(root, bg="white")
right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

Label(
    right_frame,
    text="Welcome Back",
    font=("Segoe UI", 24, "bold"),
    bg="white",
    fg="#0F4C81"
).pack(pady=(50, 5))

Label(
    right_frame,
    text="Sign in to continue",
    font=("Segoe UI", 11),
    bg="white",
    fg="gray"
).pack()

login_frame = Frame(right_frame, bg="white")
login_frame.pack(pady=35)

email_var = StringVar()
password_var = StringVar()

# Email
Label(
    login_frame,
    text="Email Address",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#0F4C81"
).grid(row=0, column=0, sticky="w", pady=(0, 5))

email_entry = Entry(
    login_frame,
    textvariable=email_var,
    font=("Segoe UI", 11),
    width=32,
    bd=2,
    relief=GROOVE
)
email_entry.grid(row=1, column=0, pady=(0, 18), ipady=6)

# Password
Label(
    login_frame,
    text="Password",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#0F4C81"
).grid(row=2, column=0, sticky="w", pady=(0, 5))

password_entry = Entry(
    login_frame,
    textvariable=password_var,
    show="*",
    font=("Segoe UI", 11),
    width=32,
    bd=2,
    relief=GROOVE
)
password_entry.grid(row=3, column=0, pady=(0, 25), ipady=6)

# Login Button
Button(
    login_frame,
    text="LOGIN",
    font=("Segoe UI", 11, "bold"),
    bg="#1565C0",
    fg="white",
    activebackground="#1565C0",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    width=28,
    pady=8,
    command=login_user
).grid(row=4, column=0)

# Register Section
Label(
    right_frame,
    text="Don't have an account?",
    font=("Segoe UI", 10),
    bg="white",
    fg="gray"
).pack(pady=(35, 5))

Button(
    right_frame,
    text="Create Account",
    font=("Segoe UI", 10, "bold"),
    bg="white",
    fg="#1565C0",
    relief=FLAT,
    cursor="hand2",
    command=open_register
).pack()

root.mainloop()