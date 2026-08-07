from tkinter import *
from tkinter import messagebox
from database import get_connection


def return_book(customer_id):

    def return_selected_book():

        book_id = entry_book_id.get().strip()

        if book_id == "":
            messagebox.showerror("Error", "Please enter Book ID.")
            return

        conn = get_connection()

        if conn is None:
            messagebox.showerror("Error", "Database Connection Failed")
            return

        cursor = conn.cursor()

        # Check if customer borrowed this book
        cursor.execute("""
            SELECT borrow_id
            FROM borrow
            WHERE customer_id = :1
            AND book_id = :2
        """, (customer_id, int(book_id)))

        row = cursor.fetchone()

        if row is None:
            messagebox.showerror(
                "Error",
                "You have not borrowed this book."
            )

            cursor.close()
            conn.close()
            return

        borrow_id = row[0]

        # Delete borrow record
        cursor.execute("""
            DELETE FROM borrow
            WHERE borrow_id = :1
        """, (borrow_id,))

        # Increase quantity
        cursor.execute("""
            UPDATE book
            SET quantity = quantity + 1
            WHERE book_id = :1
        """, (int(book_id),))

        conn.commit()

        cursor.close()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Book returned successfully."
        )

        root.destroy()

    # ---------------- Window ---------------- #

    root = Toplevel()

    root.title("Return Book")
    root.geometry("500x500")
    root.configure(bg="#F4F6F9")
    root.resizable(False, False)

    # ---------------- Header ---------------- #

    header = Frame(root, bg="#1E3A5F", height=70)
    header.pack(fill=X)

    Label(
        header,
        text="📚 Return Book",
        bg="#1E3A5F",
        fg="white",
        font=("Segoe UI", 18, "bold")
    ).pack(pady=18)

    # ---------------- Card ---------------- #

    card = Frame(
        root,
        bg="white",
        bd=1,
        relief="solid"
    )

    card.place(x=40, y=90, width=370, height=200)

    Label(
        card,
        text="Enter Book ID",
        bg="white",
        fg="#1E3A5F",
        font=("Segoe UI", 12, "bold")
    ).pack(pady=(20, 8))

    entry_book_id = Entry(
        card,
        font=("Segoe UI", 11),
        width=28,
        bd=2,
        relief="groove",
        justify="center"
    )
    entry_book_id.pack(ipady=5)

    # ---------------- Buttons ---------------- #

    Button(
        card,
        text="✔ Return Book",
        bg="#023e8a",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief=FLAT,
        activebackground="#023e8a",
        activeforeground="white",
        cursor="hand2",
        width=20,
        command=return_selected_book
    ).pack(pady=(25, 10))

    Button(
        card,
        text="← Back",
        bg="#03045e",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief=FLAT,
        activebackground="#03045e",
        activeforeground="white",
        cursor="hand2",
        width=20,
        command=root.destroy
    ).pack()

    root.mainloop()