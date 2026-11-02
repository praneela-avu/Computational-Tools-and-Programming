import sqlite3
from datetime import date


class LibraryModel:

    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT,
                quantity INTEGER NOT NULL,
                available INTEGER NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS issues (
                issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                student_name TEXT NOT NULL,
                issue_date TEXT NOT NULL,
                return_date TEXT,
                status TEXT NOT NULL,
                FOREIGN KEY(book_id) REFERENCES books(id)
            )
        """)

        self.conn.commit()

    # Add Book
    def add_book(self, title, author, category, quantity):
        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO books
            (title, author, category, quantity, available)
            VALUES (?, ?, ?, ?, ?)
        """, (title, author, category, quantity, quantity))

        self.conn.commit()

    # Display Books
    def get_books(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT id, title, author, category,
                   quantity, available
            FROM books
            ORDER BY id
        """)

        return cursor.fetchall()

    # Search Books
    def search_books(self, keyword):
        cursor = self.conn.cursor()

        search = "%" + keyword + "%"

        cursor.execute("""
            SELECT id, title, author, category,
                   quantity, available
            FROM books
            WHERE title LIKE ?
               OR author LIKE ?
               OR category LIKE ?
            ORDER BY id
        """, (search, search, search))

        return cursor.fetchall()

    # Issue Book
    def issue_book(self, book_id, student_name):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT available FROM books WHERE id = ?",
            (book_id,)
        )

        book = cursor.fetchone()

        if book is None:
            return False, "Book not found."

        if book[0] <= 0:
            return False, "Book is not available."

        cursor.execute("""
            INSERT INTO issues
            (book_id, student_name, issue_date, status)
            VALUES (?, ?, ?, ?)
        """, (
            book_id,
            student_name,
            str(date.today()),
            "Issued"
        ))

        cursor.execute("""
            UPDATE books
            SET available = available - 1
            WHERE id = ?
        """, (book_id,))

        self.conn.commit()

        return True, "Book issued successfully."

    # Return Book
    def return_book(self, issue_id):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT book_id, status
            FROM issues
            WHERE issue_id = ?
        """, (issue_id,))

        issue = cursor.fetchone()

        if issue is None:
            return False, "Issue record not found."

        book_id, status = issue

        if status == "Returned":
            return False, "Book has already been returned."

        cursor.execute("""
            UPDATE issues
            SET return_date = ?,
                status = 'Returned'
            WHERE issue_id = ?
        """, (str(date.today()), issue_id))

        cursor.execute("""
            UPDATE books
            SET available = available + 1
            WHERE id = ?
        """, (book_id,))

        self.conn.commit()

        return True, "Book returned successfully."

    # Display Issue Records
    def get_issues(self):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT
                issues.issue_id,
                books.title,
                issues.student_name,
                issues.issue_date,
                issues.return_date,
                issues.status
            FROM issues
            JOIN books
            ON issues.book_id = books.id
            ORDER BY issues.issue_id
        """)

        return cursor.fetchall()
