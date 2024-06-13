from models import Author, Book, Borrower

def menu():
    print("Library Management System")
    print("1. Manage Authors")
    print("2. Manage Books")
    print("3. Manage Borrowers")
    print("4. Exit")

def author_menu():
    print("Manage Authors")
    print("1. Create Author")
    print("2. Delete Author")
    print("3. Display All Authors")
    print("4. Find Author by ID")
    print("5. Back to Main Menu")

def book_menu():
    print("Manage Books")
    print("1. Create Book")
    print("2. Delete Book")
    print("3. Display All Books")
    print("4. Find Book by ID")
    print("5. Back to Main Menu")

def borrower_menu():
    print("Manage Borrowers")
    print("1. Create Borrower")
    print("2. Delete Borrower")
    print("3. Display All Borrowers")
    print("4. Find Borrower by ID")
    print("5. Back to Main Menu")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == '1':
            while True:
                author_menu()
                author_choice = input("Choose an option: ")
                if author_choice == '1':
                    name = input("Enter author name: ")
                    Author.create(name)
                    print("Author created.")
                elif author_choice == '2':
                    author_id = int(input("Enter author ID to delete: "))
                    Author.delete(author_id)
                    print("Author deleted.")
                elif author_choice == '3':
                    authors = Author.get_all()
                    for author in authors:
                        print(author)
                elif author_choice == '4':
                    author_id = int(input("Enter author ID: "))
                    author = Author.find_by_id(author_id)
                    print(author)
                elif author_choice == '5':
                    break
                else:
                    print("Invalid option. Try again.")
        elif choice == '2':
            while True:
                book_menu()
                book_choice = input("Choose an option: ")
                if book_choice == '1':
                    title = input("Enter book title: ")
                    author_id = int(input("Enter author ID: "))
                    Book.create(title, author_id)
                    print("Book created.")
                elif book_choice == '2':
                    book_id = int(input("Enter book ID to delete: "))
                    Book.delete(book_id)
                    print("Book deleted.")
                elif book_choice == '3':
                    books = Book.get_all()
                    for book in books:
                        print(book)
                elif book_choice == '4':
                    book_id = int(input("Enter book ID: "))
                    book = Book.find_by_id(book_id)
                    print(book)
                elif book_choice == '5':
                    break
                else:
                    print("Invalid option. Try again.")
        elif choice == '3':
            while True:
                borrower_menu()
                borrower_choice = input("Choose an option: ")
                if borrower_choice == '1':
                    name = input("Enter borrower name: ")
                    Borrower.create(name)
                    print("Borrower created.")
                elif borrower_choice == '2':
                    borrower_id = int(input("Enter borrower ID to delete: "))
                    Borrower.delete(borrower_id)
                    print("Borrower deleted.")
                elif borrower_choice == '3':
                    borrowers = Borrower.get_all()
                    for borrower in borrowers:
                        print(borrower)
                elif borrower_choice == '4':
                    borrower_id = int(input("Enter borrower ID: "))
                    borrower = Borrower.find_by_id(borrower_id)
                    print(borrower)
                elif borrower_choice == '5':
                    break
                else:
                    print("Invalid option. Try again.")
        elif choice == '4':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    from database import create_tables
    create_tables()
    main()
