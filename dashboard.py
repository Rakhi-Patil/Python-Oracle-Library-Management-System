from tkinter import *
from tkinter import messagebox


def dashboard(user):

    root = Tk()
    root.title("Library Management System")
    root.geometry("900x650")
    root.configure(bg="#F4F6F9")
    root.resizable(False, False)

    # ---------------- User Data ---------------- #

    customer_id = user[0]
    name = user[1]
    email = user[2]
    contact = user[3]
    address = user[4]

    # ---------------- Functions ---------------- #

    def open_search_book():
        from search_book import search_book
        search_book(customer_id)

    def open_history():
        from history import history
        history(customer_id)

    def open_change_password():
        from change_pass import change_password
        change_password(customer_id)

    def open_return_book():
        from return_book import return_book
        return_book(customer_id)

    def logout():
        if messagebox.askyesno("Logout", "Do you want to logout?"):
            root.destroy()

    # ---------------- Header ---------------- #

    header = Frame(root, bg="#1E3A5F", height=80)
    header.pack(fill=X)

    Label(
        header,
        text="📚 Library Management System",
        bg="#1E3A5F",
        fg="white",
        font=("Segoe UI", 22, "bold")
    ).pack(pady=18)

    # ---------------- Welcome ---------------- #

    Label(
        root,
        text=f"Welcome, {name}",
        bg="#F4F6F9",
        fg="#1E3A5F",
        font=("Segoe UI", 18, "bold")
    ).pack(pady=15)

    # ---------------- Main Container ---------------- #

    container = Frame(root, bg="#F4F6F9")
    container.pack(fill=BOTH, expand=True)

    # ---------------- Left Card ---------------- #

    info_card = Frame(
        container,
        bg="white",
        bd=1,
        relief="solid"
    )

    info_card.place(x=40, y=10, width=380, height=450)

    Label(
        info_card,
        text="User Information",
        bg="white",
        fg="#1E3A5F",
        font=("Segoe UI", 16, "bold")
    ).pack(pady=15)

    details = [
        ("Customer ID", customer_id),
        ("Name", name),
        ("Email", email),
        ("Contact", contact),
        ("Address", address)
    ]

    for title, value in details:

        row = Frame(info_card, bg="white")
        row.pack(fill=X, padx=20, pady=8)

        Label(
            row,
            text=title,
            width=12,
            anchor="w",
            bg="white",
            fg="#555555",
            font=("Segoe UI", 10, "bold")
        ).pack(side=LEFT)

        Label(
            row,
            text=":",
            bg="white",
            font=("Segoe UI", 10)
        ).pack(side=LEFT)

        Label(
            row,
            text=value,
            bg="white",
            fg="#222222",
            font=("Segoe UI", 10)
        ).pack(side=LEFT, padx=10)

    # ---------------- Right Card ---------------- #

    menu_card = Frame(
        container,
        bg="white",
        bd=1,
        relief="solid"
    )

    menu_card.place(x=470, y=10, width=370, height=450)

    Label(
        menu_card,
        text="Quick Actions",
        bg="white",
        fg="#1E3A5F",
        font=("Segoe UI", 16, "bold")
    ).pack(pady=20)

    btn_font = ("Segoe UI", 11, "bold")

    Button(
        menu_card,
        text="🔍 Search Book",
        bg="#00b4d8",
        fg="white",
        activebackground="#00b4d8",
        activeforeground="white",
        relief=FLAT,
        cursor="hand2",
        font=btn_font,
        width=22,
        height=2,
        command=open_search_book
    ).pack(pady=8)

    Button(
        menu_card,
        text="📖 Borrow History",
        bg="#0096c7",
        fg="white",
        activebackground="#0096c7",
        activeforeground="white",
        relief=FLAT,
        cursor="hand2",
        font=btn_font,
        width=22,
        height=2,
        command=open_history
    ).pack(pady=8)

    Button(
        menu_card,
        text="🔑 Change Password",
        bg="#0077b6",
        fg="white",
        activebackground="#0077b6",
        activeforeground="white",
        relief=FLAT,
        cursor="hand2",
        font=btn_font,
        width=22,
        height=2,
        command=open_change_password
    ).pack(pady=8)

    Button(
        menu_card,
        text="📚 Return Book",
        bg="#023e8a",
        fg="white",
        activebackground="#023e8a",
        activeforeground="white",
        relief=FLAT,
        cursor="hand2",
        font=btn_font,
        width=22,
        height=2,
        command=open_return_book
    ).pack(pady=8)

    Button(
        menu_card,
        text=" Logout",
        bg="#03045e",
        fg="white",
        activebackground="#03045e",
        activeforeground="white",
        relief=FLAT,
        cursor="hand2",
        font=btn_font,
        width=22,
        height=2,
        command=logout
    ).pack(pady=20)

    # ---------------- Footer ---------------- #

    Label(
        root,
        text="Library Management System",
        bg="#F4F6F9",
        fg="gray",
        font=("Segoe UI", 9)
    ).pack(side=BOTTOM, pady=8)

    root.mainloop()