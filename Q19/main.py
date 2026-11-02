import tkinter as tk

from Model import LibraryModel
from view import LibraryView
from controller import LibraryController


def main():

    root = tk.Tk()

    # MVC Objects
    model = LibraryModel()
    view = LibraryView(root)

    # Connect Model and View through Controller
    controller = LibraryController(
        model,
        view
    )

    root.mainloop()


if __name__ == "__main__":
    main()
