# 📚 Library Management System | Python, Tkinter & Oracle Database

## 📌 Project Overview

This project is a desktop-based **Library Management System** developed using **Python**, **Tkinter**, and **Oracle Database**.

The application provides a user-friendly graphical interface that allows customers to register, log in, search books, borrow books, return books, view borrowing history, and change passwords.

The project demonstrates the integration of a Python GUI application with an Oracle relational database while implementing **CRUD operations, SQL queries, database transactions, and library management functionalities**.

---

# 🎯 Objectives

- Develop a desktop-based library management application.
- Implement customer registration and login functionality.
- Enable customers to search and borrow available books.
- Manage book returns and automatically update book inventory.
- Display customer borrowing history.
- Perform database operations using Oracle SQL.
- Design a modern and user-friendly graphical interface.

---

# 📂 Project Structure

```
Python-Oracle-Library-Management-System/
│
├── login.py
├── signin.py
├── dashboard.py
├── search_book.py
├── borrowed_book.py
├── return_book.py
├── change_pass.py
├── history.py
├── database.py
│
├── library.sql
├── README.md
│
└── screenshots/
    ├── login.png
    ├── registration.png
    ├── dashboard.png
    ├── search_book.png
    ├── borrow_history.png
    ├── return_book.png
    └── change_password.png
```

---

# 🗄️ Database Information

The project uses **Oracle Database** with the following tables:

## Customer Table

| Column | Description |
|--------|-------------|
| Customer_ID | Unique customer identifier |
| Name | Customer name |
| Email | Customer email |
| Contact_Number | Customer contact number |
| Address | Customer address |
| Password | Customer password |

---

## Book Table

| Column | Description |
|--------|-------------|
| Book_ID | Unique book identifier |
| Book_Name | Name of the book |
| Author | Book author |
| Quantity | Available book quantity |

---

## Borrow Table

| Column | Description |
|--------|-------------|
| Borrow_ID | Unique borrow identifier |
| Customer_ID | Customer reference ID |
| Book_ID | Book reference ID |
| Borrow_Date | Date of borrowing |

---

# ⚙️ System Workflow

```
Customer Registration
          |
          ▼
Customer Login
          |
          ▼
      Dashboard
          |
 ┌────────┼─────────┐
 │        │         │
 ▼        ▼         ▼
Search   History   Change
Book               Password
 │
 ▼
Borrow Book
 │
 ▼
Quantity Updated
 │
 ▼
Return Book
 │
 ▼
Quantity Restored
```

---

# 💻 Application Features

- ✅ Customer Registration
- ✅ Secure Login System
- ✅ Dashboard Navigation
- ✅ Search Books
- ✅ Borrow Books
- ✅ Return Books
- ✅ Borrowing History
- ✅ Change Password
- ✅ Automatic Inventory Update
- ✅ Oracle Database Connectivity
- ✅ Modern Tkinter User Interface

---

# 📊 SQL Concepts Used

The project implements the following SQL concepts:

- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`
- `INNER JOIN`
- `WHERE Clause`
- `ORDER BY`
- Aggregate Function (`MAX`)
- `NVL` Function
- Parameterized Queries

---

# 🎨 GUI Features

- Modern Tkinter interface
- Card-based layout design
- Navigation dashboard
- User-friendly forms
- Styled buttons
- Message boxes
- Treeview tables
- Responsive application windows

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Application Development |
| Tkinter | GUI Development |
| Oracle Database | Data Storage |
| Oracle SQL | Database Operations |
| oracledb | Python-Oracle Connectivity |

---

# 📷 Application Screenshots

## Login Page

<img width="1790" height="1148" alt="login" src="https://github.com/user-attachments/assets/e8cae9c6-ce4c-4b57-883d-6948a7cfbfc2" />

---

## Registration Page

<img width="1952" height="1496" alt="Registration" src="https://github.com/user-attachments/assets/156c958d-398f-4aab-b925-2018f2c7a733" />

---

## Dashboard

<img width="1788" height="1348" alt="Dashboard" src="https://github.com/user-attachments/assets/c4899c93-6752-4953-b70f-5e7f3a3d274e" />

---

## Search Book

<img width="1188" height="850" alt="Search" src="https://github.com/user-attachments/assets/5a22340c-3bdd-4a44-a77b-7e3ff6f83251" />

---

## History

<img width="1388" height="840" alt="History" src="https://github.com/user-attachments/assets/8b779e8c-9cac-4142-82f6-cdb689d4eb31" />

---

## Return Book

<img width="986" height="826" alt="Return" src="https://github.com/user-attachments/assets/1afe5056-72aa-423c-88e5-844fae5fbd01" />

---

## Change Password

<img width="986" height="754" alt="Change_pass" src="https://github.com/user-attachments/assets/6ae891ff-157a-4f88-b6c6-c171b4b0d149" />

---

# 🚀 Learning Outcomes

This project demonstrates practical knowledge of:

- Python GUI Development
- Event-Driven Programming
- Oracle Database Connectivity
- SQL Query Writing
- CRUD Operations
- Database Transactions
- Modular Programming
- Tkinter Widget Design
- User Authentication
- Inventory Management

---

# 🔮 Future Improvements

- Admin Dashboard
- Add / Delete / Update Books
- Fine Calculation System
- Password Encryption
- Report Generation
- User Role Management

---

# 💼 Use Case

This project demonstrates a complete desktop application integrating **Python, Tkinter, and Oracle Database** to automate essential library operations.

It showcases:

- GUI application development
- Database connectivity
- SQL programming
- CRUD operations
- Modular software design

This project is suitable for:

- Academic submissions
- Internship portfolios
- Python Developer portfolios
- Database Management practice

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates me to build and share more projects.
