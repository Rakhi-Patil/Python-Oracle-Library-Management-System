from tkinter import *
from tkinter import messagebox
from database import get_connection


def change_password(customer_id):

    def update_password():

        old_password = entry_old.get()
        new_password = entry_new.get()
        confirm_password = entry_confirm.get()

        if old_password == "" or new_password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "New passwords do not match.")
            return

        conn = get_connection()

        if conn is None:
            messagebox.showerror("Error", "Database Connection Failed")
            return

        cursor = conn.cursor()

        # Check old password
        cursor.execute("""
            SELECT password
            FROM customer
            WHERE customer_id = :1
        """, (customer_id,))

        row = cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "Customer not found.")
            cursor.close()
            conn.close()
            return

        if row[0] != old_password:
            messagebox.showerror("Error", "Old password is incorrect.")
            cursor.close()
            conn.close()
            return

        # Update password
        cursor.execute("""
            UPDATE customer
            SET password = :1
            WHERE customer_id = :2
        """, (new_password, customer_id))

        conn.commit()

        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Password changed successfully.")

        root.destroy()

    root = Toplevel()
    root.title("Change Password")
    root.geometry("500x600")
    root.configure(bg="white")
    root.resizable(False, False)

    Label(root, text="Change Password",
          font=("Arial", 16, "bold"),
          bg="white",
          fg="navy").pack(pady=15)

    Label(root, text="Old Password", bg="white").pack()
    entry_old = Entry(root, show="*", width=30)
    entry_old.pack(pady=5)

    Label(root, text="New Password", bg="white").pack()
    entry_new = Entry(root, show="*", width=30)
    entry_new.pack(pady=5)

    Label(root, text="Confirm Password", bg="white").pack()
    entry_confirm = Entry(root, show="*", width=30)
    entry_confirm.pack(pady=5)

    Button(
        root,
        text="Update Password",
        bg="#0353a4",
        fg="white",
        width=18,
        command=update_password
    ).pack(pady=15)

    Button(
        root,
        text="Back",
        bg="#03045e",
        fg="white",
        width=18,
        command=root.destroy
    ).pack()



