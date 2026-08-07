from tkinter import *
from tkinter import ttk, messagebox
from database import get_connection


def history(customer_id):

    root = Toplevel()
    root.title("Borrow & Return History")
    root.geometry("700x400")
    root.configure(bg="white")

    Label(
        root,
        text="Borrow & Return History",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="navy"
    ).pack(pady=10)

    columns = ("Borrow ID", "Book ID", "Book Name", "Borrow Date")

    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    conn = get_connection()

    if conn is None:
        messagebox.showerror("Error", "Database Connection Failed")
        return

    cursor = conn.cursor()

    cursor.execute("""
        SELECT b.borrow_id,
               bk.book_id,
               bk.book_name,
               b.borrow_date
        FROM borrow b
        JOIN book bk
        ON b.book_id = bk.book_id
        WHERE b.customer_id = :1
        ORDER BY b.borrow_date DESC
    """, (customer_id,))

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    cursor.close()
    conn.close()

    Button(
        root,
        text="Close",
        bg="#03045e",
        fg="white",
        command=root.destroy
    ).pack(pady=10)