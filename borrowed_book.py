from tkinter import messagebox
from database import get_connection

def borrow_book(customer_id, book_id):

    conn = get_connection()

    if conn is None:
        messagebox.showerror("Error", "Database connection failed.")
        return

    cursor = conn.cursor()

    # Check available quantity
    cursor.execute("""
        SELECT quantity
        FROM book
        WHERE book_id = :1
    """, (book_id,))

    row = cursor.fetchone()

    if row is None:
        messagebox.showerror("Error", "Book not found.")
        cursor.close()
        conn.close()
        return

    if row[0] <= 0:
        messagebox.showinfo("Unavailable", "Book is not available.")
        cursor.close()
        conn.close()
        return

    # Generate next borrow_id
    cursor.execute("SELECT NVL(MAX(borrow_id),0)+1 FROM borrow")
    borrow_id = cursor.fetchone()[0]

    # Insert borrow record
    cursor.execute("""
        INSERT INTO borrow (borrow_id, customer_id, book_id)
        VALUES (:1, :2, :3)
    """, (borrow_id, customer_id, book_id))

    # Reduce quantity
    cursor.execute("""
        UPDATE book
        SET quantity = quantity - 1
        WHERE book_id = :1
    """, (book_id,))

    conn.commit()

    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Book borrowed successfully.")