class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued successfully.")
        else:
            print(self.title, "is already issued.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned successfully.")
        else:
            print(self.title, "was not issued.")


class Book(LibraryItem):
    def display(self):
        print("Book:", self.title)


class Magazine(LibraryItem):
    def display(self):
        print("Magazine:", self.title)


class Journal(LibraryItem):
    def display(self):
        print("Journal:", self.title)


items = [
    Book("Python Programming"),
    Magazine("Tech Today"),
    Journal("Computer Science Journal")
]

for item in items:
    item.display()
    item.issue()
    item.return_item()
    print()