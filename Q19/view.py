import tkinter as tk
from tkinter import ttk


class LibraryView:

    def __init__(self, root):

        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("950x650")

        self.create_gui()

    def create_gui(self):

        title = tk.Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=15
        )

        title.pack(fill="x")

        notebook = ttk.Notebook(self.root)
        notebook.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.book_tab = ttk.Frame(notebook)
        self.issue_tab = ttk.Frame(notebook)
        self.return_tab = ttk.Frame(notebook)

        notebook.add(
            self.book_tab,
            text="Book Management"
        )

        notebook.add(
            self.issue_tab,
            text="Issue Book"
        )

        notebook.add(
            self.return_tab,
            text="Return Book"
        )

        self.create_book_tab()
        self.create_issue_tab()
        self.create_return_tab()

    # ---------------- BOOK TAB ----------------

    def create_book_tab(self):

        frame = ttk.LabelFrame(
            self.book_tab,
            text="Book Details"
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=15
        )

        ttk.Label(
            frame,
            text="Book Title:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.title_entry = ttk.Entry(
            frame,
            width=30
        )

        self.title_entry.grid(row=0, column=1)

        ttk.Label(
            frame,
            text="Author:"
        ).grid(row=0, column=2, padx=10)

        self.author_entry = ttk.Entry(
            frame,
            width=30
        )

        self.author_entry.grid(row=0, column=3)

        ttk.Label(
            frame,
            text="Category:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.category_entry = ttk.Entry(
            frame,
            width=30
        )

        self.category_entry.grid(row=1, column=1)

        ttk.Label(
            frame,
            text="Quantity:"
        ).grid(row=1, column=2, padx=10)

        self.quantity_entry = ttk.Entry(
            frame,
            width=30
        )

        self.quantity_entry.grid(row=1, column=3)

        self.add_button = ttk.Button(
            frame,
            text="Add Book"
        )

        self.add_button.grid(
            row=2,
            column=1,
            pady=10
        )

        # Search

        search_frame = ttk.Frame(
            self.book_tab
        )

        search_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        ttk.Label(
            search_frame,
            text="Search:"
        ).pack(side="left")

        self.search_entry = ttk.Entry(
            search_frame,
            width=40
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        self.search_button = ttk.Button(
            search_frame,
            text="Search"
        )

        self.search_button.pack(side="left")

        self.show_all_button = ttk.Button(
            search_frame,
            text="Show All"
        )

        self.show_all_button.pack(
            side="left",
            padx=5
        )

        # Book Table

        columns = (
            "ID",
            "Title",
            "Author",
            "Category",
            "Quantity",
            "Available"
        )

        self.book_table = ttk.Treeview(
            self.book_tab,
            columns=columns,
            show="headings",
            height=15
        )

        for column in columns:
            self.book_table.heading(
                column,
                text=column
            )

            self.book_table.column(
                column,
                width=130
            )

        self.book_table.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

    # ---------------- ISSUE TAB ----------------

    def create_issue_tab(self):

        frame = ttk.LabelFrame(
            self.issue_tab,
            text="Issue Book"
        )

        frame.pack(
            padx=30,
            pady=30
        )

        ttk.Label(
            frame,
            text="Book ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        self.issue_book_id = ttk.Entry(
            frame,
            width=30
        )

        self.issue_book_id.grid(
            row=0,
            column=1
        )

        ttk.Label(
            frame,
            text="Student Name:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=15
        )

        self.student_entry = ttk.Entry(
            frame,
            width=30
        )

        self.student_entry.grid(
            row=1,
            column=1
        )

        self.issue_button = ttk.Button(
            frame,
            text="Issue Book"
        )

        self.issue_button.grid(
            row=2,
            column=1,
            pady=15
        )

    # ---------------- RETURN TAB ----------------

    def create_return_tab(self):

        frame = ttk.LabelFrame(
            self.return_tab,
            text="Return Book"
        )

        frame.pack(
            padx=30,
            pady=20
        )

        ttk.Label(
            frame,
            text="Issue ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        self.issue_id_entry = ttk.Entry(
            frame,
            width=30
        )

        self.issue_id_entry.grid(
            row=0,
            column=1
        )

        self.return_button = ttk.Button(
            frame,
            text="Return Book"
        )

        self.return_button.grid(
            row=1,
            column=1,
            pady=15
        )

        # Issue Table

        columns = (
            "Issue ID",
            "Book",
            "Student",
            "Issue Date",
            "Return Date",
            "Status"
        )

        self.issue_table = ttk.Treeview(
            self.return_tab,
            columns=columns,
            show="headings",
            height=15
        )

        for column in columns:
            self.issue_table.heading(
                column,
                text=column
            )

            self.issue_table.column(
                column,
                width=140
            )

        self.issue_table.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )
