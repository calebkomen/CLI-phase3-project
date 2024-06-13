from database import connect_db


# Rest of the code remains unchanged

class Author:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def create(name):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
            conn.commit()
    
    @staticmethod
    def delete(author_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM authors WHERE id = ?', (author_id,))
            conn.commit()
    
    @staticmethod
    def get_all():
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM authors')
            return cursor.fetchall()

    @staticmethod
    def find_by_id(author_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
            return cursor.fetchone()

class Book:
    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id

    @staticmethod
    def create(title, author_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO books (title, author_id) VALUES (?, ?)', (title, author_id))
            conn.commit()

    @staticmethod
    def delete(book_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books')
            return cursor.fetchall()

    @staticmethod
    def find_by_id(book_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
            return cursor.fetchone()

class Borrower:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def create(name):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO borrowers (name) VALUES (?)', (name,))
            conn.commit()

    @staticmethod
    def delete(borrower_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM borrowers WHERE id = ?', (borrower_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM borrowers')
            return cursor.fetchall()

    @staticmethod
    def find_by_id(borrower_id):
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM borrowers WHERE id = ?', (borrower_id,))
            return cursor.fetchone()
 
    