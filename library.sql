CREATE SEQUENCE customer_seq
START WITH 1
INCREMENT BY 1;

CREATE TABLE customer (
    customer_id VARCHAR2(20)
        DEFAULT ('CUST' || LPAD(customer_seq.NEXTVAL, 4, '0'))
        PRIMARY KEY,
    name VARCHAR2(100),
    email VARCHAR2(100) UNIQUE,
    contact VARCHAR2(10),
    address VARCHAR2(200),
    password VARCHAR2(100),
    membership_date DATE DEFAULT SYSDATE
);


SELECT customer_seq.NEXTVAL
FROM dual;



CREATE TABLE BOOK (
    BOOK_ID NUMBER PRIMARY KEY,
    BOOK_NAME VARCHAR2(100),
    AUTHOR VARCHAR2(100),
    CATEGORY VARCHAR2(50),
    QUANTITY NUMBER
);


CREATE TABLE borrow (
    borrow_id NUMBER PRIMARY KEY,
    customer_id VARCHAR2(20) REFERENCES customer(customer_id),
    book_id NUMBER REFERENCES book(book_id),
    borrow_date DATE DEFAULT SYSDATE
);

select * from borrow;

INSERT INTO BOOK VALUES (101, 'Python Basics', 'John Smith', 'Programming', 5);

INSERT INTO BOOK VALUES (102, 'Advanced Python', 'David Miller', 'Programming', 3);

INSERT INTO BOOK VALUES (103, 'SQL Fundamentals', 'Michael Brown', 'Database', 7);

INSERT INTO BOOK VALUES (104, 'Oracle Database Guide', 'James Wilson', 'Database', 4);

INSERT INTO BOOK VALUES (105, 'Data Structures', 'Mark Taylor', 'Computer Science', 6);

INSERT INTO BOOK VALUES (106, 'Operating Systems', 'Andrew Tanenbaum', 'Computer Science', 2);

INSERT INTO BOOK VALUES (107, 'Computer Networks', 'Behrouz Forouzan', 'Networking', 5);

INSERT INTO BOOK VALUES (108, 'Machine Learning Basics', 'Tom Mitchell', 'Artificial Intelligence', 4);

INSERT INTO BOOK VALUES (109, 'Artificial Intelligence', 'Stuart Russell', 'Artificial Intelligence', 3);

INSERT INTO BOOK VALUES (110, 'Power BI for Beginners', 'Alex Johnson', 'Data Analytics', 8);

INSERT INTO BOOK VALUES (111, 'Excel Essentials', 'Sarah Lee', 'Data Analytics', 10);

INSERT INTO BOOK VALUES (112, 'Java Programming', 'Herbert Schildt', 'Programming', 5);

INSERT INTO BOOK VALUES (113, 'C Programming', 'Dennis Ritchie', 'Programming', 4);

INSERT INTO BOOK VALUES (114, 'Web Development', 'Jon Duckett', 'Web Development', 6);

INSERT INTO BOOK VALUES (115, 'Data Analytics with Python', 'Wes McKinney', 'Data Analytics', 3);

COMMIT;




select * from book;

INSERT INTO books(title,author,category,quantity,available)
VALUES('Python Programming','John Zelle','Programming',5,5);

INSERT INTO books(title,author,category,quantity,available)
VALUES('Java Complete Reference','Herbert Schildt','Programming',3,3);

INSERT INTO books(title,author,category,quantity,available)
VALUES('Database Systems','Elmasri','Database',4,4);

INSERT INTO books(title,author,category,quantity,available)
VALUES('Operating System','Galvin','Computer',2,2);

COMMIT;



