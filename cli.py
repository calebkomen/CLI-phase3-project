#!/usr/bin/env python3

from colorama import init, Fore, Style
from models import Author, Book, Borrower

# Initialize colorama
init()

def display_menu(menu_title, options):
    """
    Display a menu with a title and list of options.

    Args:
        menu_title (str): The title of the menu.
        options (list): A list of menu options.
    """
    print(Fore.CYAN + menu_title + Style.RESET_ALL)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    print(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL, end='')


def main_menu():
    """
    Display the main menu.
    """
    display_menu("Library Management System", ["Manage Authors", "Manage Books", "Manage Borrowers", "Exit"])


def author_menu():
    """
    Display the author management menu.
    """
    display_menu("Manage Authors", ["Create Author", "Delete Author", "Display All Authors", "Find Author by ID", "Back to Main Menu"])


def book_menu():
    """
    Display the book management menu.
    """
    display_menu("Manage Books", ["Create Book", "Delete Book", "Display All Books", "Find Book by ID", "Back to Main Menu"])


def borrower_menu():
    """
    Display the borrower management menu.
    """
    display_menu("Manage Borrowers", ["Create Borrower", "Delete Borrower", "Display All Borrowers", "Find Borrower by ID", "Back to Main Menu"])


def manage_authors():
    """
    Handle the author management workflow.
    """
    while True:
        author_menu()
        choice = input().strip()
        if choice == '1':
            name = input("Enter author name: ").strip()
            Author.create(name)
            print(Fore.GREEN + "Author created." + Style.RESET_ALL)
        elif choice == '2':
            author_id = int(input("Enter author ID to delete: ").strip())
            Author.delete(author_id)
            print(Fore.RED + "Author deleted." + Style.RESET_ALL)
        elif choice == '3':
            authors = Author.get_all()
            for author in authors:
                print(author)
        elif choice == '4':
            author_id = int(input("Enter author ID: ").strip())
            author = Author.find_by_id(author_id)
            print(author)
        elif choice == '5':
            break
        else:
            print(Fore.RED + "Invalid option. Try again." + Style.RESET_ALL)


def manage_books():
    """
    Handle the book management workflow.
    """
    while True:
        book_menu()
        choice = input().strip()
        if choice == '1':
            title = input("Enter book title: ").strip()
            author_id = int(input("Enter author ID: ").strip())
            Book.create(title, author_id)
            print(Fore.GREEN + "Book created." + Style.RESET_ALL)
        elif choice == '2':
            book_id = int(input("Enter book ID to delete: ").strip())
            Book.delete(book_id)
            print(Fore.RED + "Book deleted." + Style.RESET_ALL)
        elif choice == '3':
            books = Book.get_all()
            for book in books:
                print(book)
        elif choice == '4':
            book_id = int(input("Enter book ID: ").strip())
            book = Book.find_by_id(book_id)
            print(book)
        elif choice == '5':
            break
        else:
            print(Fore.RED + "Invalid option. Try again." + Style.RESET_ALL)


def manage_borrowers():
    """
    Handle the borrower management workflow.
    """
    while True:
        borrower_menu()
        choice = input().strip()
        if choice == '1':
            name = input("Enter borrower name: ").strip()
            Borrower.create(name)
            print(Fore.GREEN + "Borrower created." + Style.RESET_ALL)
        elif choice == '2':
            borrower_id = int(input("Enter borrower ID to delete: ").strip())
            Borrower.delete(borrower_id)
            print(Fore.RED + "Borrower deleted." + Style.RESET_ALL)
        elif choice == '3':
            borrowers = Borrower.get_all()
            for borrower in borrowers:
                print(borrower)
        elif choice == '4':
            borrower_id = int(input("Enter borrower ID: ").strip())
            borrower = Borrower.find_by_id(borrower_id)
            print(borrower)
        elif choice == '5':
            break
        else:
            print(Fore.RED + "Invalid option. Try again." + Style.RESET_ALL)


def main():
    """
    Main function to run the Library Management System CLI.
    """
    while True:
        main_menu()
        choice = input().strip()
        if choice == '1':
            manage_authors()
        elif choice == '2':
            manage_books()
        elif choice == '3':
            manage_borrowers()
        elif choice == '4':
            print(Fore.CYAN + "Exiting the Library Management System. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Try again." + Style.RESET_ALL)


if __name__ == "__main__":
    from database import create_tables
    create_tables()
    main()
