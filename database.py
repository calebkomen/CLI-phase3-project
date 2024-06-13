#!/usr/bin/env python3
import sqlite3

def create_tables():
    print("Creating tables...")  # Print a message to indicate the start of table creation
    # Connect to the database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
    print("Authors table created.")  # Print a message after creating the authors table

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors (id)
    )
    ''')
    print("Books table created.")  # Print a message after creating the books table

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrowers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
    print("Borrowers table created.")  # Print a message after creating the borrowers table

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrow_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        borrower_id INTEGER,
        book_id INTEGER,
        FOREIGN KEY (borrower_id) REFERENCES borrowers (id),
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
    ''')
    print("Borrow records table created.")  # Print a message after creating the borrow_records table

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Tables creation complete.")  # Print a message after completing table creation
