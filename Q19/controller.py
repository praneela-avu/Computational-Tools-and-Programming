from tkinter import messagebox


class LibraryController:

    def __init__(self, model, view):

        self.model = model
        self.view = view

        # Button Events
        self.view.add_button.config(
            command=self.add_book
        )

        self.view.search_button.config(
            command=self.search_books
        )

        self.view.show_all_button.config(
            command=self.show_all_books
        )

        self.view.issue_button.config(
            command=self.issue_book
        )

        self.view.return_button.config(
            command=self.return_book
        )

        self.show_all_books()
        self.show_issues()

    # Add Book
    def add_book(self):

        title = self.view.title_entry.get().strip()
        author = self.view.author_entry.get().strip()
        category = self.view.category_entry.get().strip()
        quantity = self.view.quantity_entry.get().strip()

        if title == "" or author == "" or quantity == "":
            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )
            return

        try:
            quantity = int(quantity)

            if quantity <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Error",
                "Quantity must be a positive number."
            )
            return

        self.model.add_book(
            title,
            author,
            category,
            quantity
        )

        messagebox.showinfo(
            "Success",
            "Book added successfully."
        )

        self.clear_book_form()
        self.show_all_books()

    # Search
    def search_books(self):

        keyword = self.view.search_entry.get().strip()

        books = self.model.search_books(keyword)

        self.display_books(books)

    # Show All
    def show_all_books(self):

        books = self.model.get_books()

        self.display_books(books)

    # Display Books
    def display_books(self, books):

        for item in self.view.book_table.get_children():
            self.view.book_table.delete(item)

        for book in books:
            self.view.book_table.insert(
                "",
                "end",
                values=book
            )

    # Issue Book
    def issue_book(self):

        book_id = self.view.issue_book_id.get().strip()
        student = self.view.student_entry.get().strip()

        if book_id == "" or student == "":
            messagebox.showerror(
                "Error",
                "Book ID and Student Name are required."
            )
            return

        try:
            book_id = int(book_id)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Book ID must be a number."
            )
            return

        success, message = self.model.issue_book(
            book_id,
            student
        )

        if success:

            messagebox.showinfo(
                "Success",
                message
            )

            self.view.issue_book_id.delete(
                0,
                "end"
            )

            self.view.student_entry.delete(
                0,
                "end"
            )

            self.show_all_books()
            self.show_issues()

        else:

            messagebox.showerror(
                "Error",
                message
            )

    # Return Book
    def return_book(self):

        issue_id = self.view.issue_id_entry.get().strip()

        if issue_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Issue ID."
            )
            return

        try:
            issue_id = int(issue_id)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Issue ID must be a number."
            )
            return

        success, message = self.model.return_book(
            issue_id
        )

        if success:

            messagebox.showinfo(
                "Success",
                message
            )

            self.view.issue_id_entry.delete(
                0,
                "end"
            )

            self.show_all_books()
            self.show_issues()

        else:

            messagebox.showerror(
                "Error",
                message
            )

    # Display Issues
    def show_issues(self):

        issues = self.model.get_issues()

        for item in self.view.issue_table.get_children():
            self.view.issue_table.delete(item)

        for issue in issues:
            self.view.issue_table.insert(
                "",
                "end",
                values=issue
            )

    # Clear Book Form
    def clear_book_form(self):

        self.view.title_entry.delete(0, "end")
        self.view.author_entry.delete(0, "end")
        self.view.category_entry.delete(0, "end")
        self.view.quantity_entry.delete(0, "end")
