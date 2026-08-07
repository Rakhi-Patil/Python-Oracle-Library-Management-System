from tkinter import *
from tkinter import messagebox
from database import get_connection
from borrowed_book import borrow_book

def search_book(customer_id):
    current_book_id = None
    # ---------------- Search Function ---------------- #

    def search():
        nonlocal current_book_id

        book_name = entry_book.get().strip()

        if book_name == "":
            messagebox.showerror("Error", "Please enter a book name.")
            return

        conn = get_connection()

        if conn is None:
            messagebox.showerror("Error", "Database Connection Failed")
            return

        cursor = conn.cursor()

        cursor.execute("""
            SELECT book_id, book_name, author, quantity
            FROM book
            WHERE LOWER(book_name) LIKE LOWER(:1)
        """, ('%' + book_name + '%',))

        book = cursor.fetchone()

        cursor.close()
        conn.close()

        if book:

            current_book_id = book[0]

            lbl_id.config(text=book[0])
            lbl_name.config(text=book[1])
            lbl_author.config(text=book[2])
            lbl_quantity.config(text=book[3])

            btn_borrow.config(state="normal")

        else:

            current_book_id = None

            lbl_id.config(text="")
            lbl_name.config(text="")
            lbl_author.config(text="")
            lbl_quantity.config(text="")

            btn_borrow.config(state="disabled")

            messagebox.showinfo("Not Found", "Book not found.")

    # ---------------- Back Function ---------------- #

    def go_back():
        root.destroy()

    # ---------------- Window ---------------- #

    root = Toplevel()
    root.title("Search Book")
    root.geometry("600x600")
    root.configure(bg="white")
    root.resizable(False, False)

    # ---------------- Heading ---------------- #

    Label(
        root,
        text="Search Book",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="navy"
    ).pack(pady=15)

    # ---------------- Search Box ---------------- #

    Label(
        root,
        text="Book Name",
        bg="white",
        font=("Arial", 11)
    ).pack()

    entry_book = Entry(root, width=30, font=("Arial", 11))
    entry_book.pack(pady=8)

    # ---------------- Buttons ---------------- #

    button_frame = Frame(root, bg="white")
    button_frame.pack(pady=10)

    Button(
        button_frame,
        text="Search",
        bg="#0077b6",
        fg="white",
        width=12,
        font=("Arial", 10, "bold"),
        command=search
    ).grid(row=0, column=0, padx=10)

    btn_borrow = Button(
        button_frame,
        text="Borrow Book",
        bg="#023e8a",
        fg="white",
        width=15,
        font=("Arial", 10, "bold"),
        state="disabled",
        command=lambda: borrow_book(customer_id, current_book_id)
    )
    btn_borrow.grid(row=0, column=1, padx=10)

    Button(
        button_frame,
        text="Back",
        bg="#03045e",
        fg="white",
        width=12,
        font=("Arial", 10, "bold"),
        command=go_back
    ).grid(row=0, column=2, padx=10)


    # ---------------- Result Frame ---------------- #

    result_frame = LabelFrame(
        root,
        text="Book Details",
        bg="white",
        font=("Arial", 11, "bold")
    )

    result_frame.pack(padx=20, pady=15, fill="both")

    Label(result_frame, text="Book ID :", bg="white").grid(row=0, column=0, padx=10, pady=8, sticky="w")
    lbl_id = Label(result_frame, text="", bg="white")
    lbl_id.grid(row=0, column=1, sticky="w")

    Label(result_frame, text="Book Name :", bg="white").grid(row=1, column=0, padx=10, pady=8, sticky="w")
    lbl_name = Label(result_frame, text="", bg="white")
    lbl_name.grid(row=1, column=1, sticky="w")

    Label(result_frame, text="Author :", bg="white").grid(row=2, column=0, padx=10, pady=8, sticky="w")
    lbl_author = Label(result_frame, text="", bg="white")
    lbl_author.grid(row=2, column=1, sticky="w")

    Label(result_frame, text="Quantity :", bg="white").grid(row=3, column=0, padx=10, pady=8, sticky="w")
    lbl_quantity = Label(result_frame, text="", bg="white")
    lbl_quantity.grid(row=3, column=1, sticky="w")