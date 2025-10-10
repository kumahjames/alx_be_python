from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\nAttempting to check out '1984':")
    library.check_out_book("1984")
    
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    print("\nAttempting to return '1984':")
    library.return_book("1984")
    
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
    
    # Test trying to check out an unavailable book (optional, for robustness)
    print("\nAttempting to check out 'Brave New World' twice:")
    library.check_out_book("Brave New World")
    library.check_out_book("Brave New World")


if __name__ == "__main__":
    main()