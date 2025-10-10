class Book:
    def __init__(self, title, author):
        """Base class for all books"""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for Book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """EBook class - inherits from Book"""
        super().__init__(title, author)  # Call parent class constructor
        self.file_size = file_size
    
    def __str__(self):
        """String representation for EBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """PrintBook class - inherits from Book"""
        super().__init__(title, author)  # Call parent class constructor
        self.page_count = page_count
    
    def __str__(self):
        """String representation for PrintBook"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library class using composition to manage books"""
        self.books = []  # List to store book instances
    
    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library"""
        for book in self.books:
            print(book)

     

     

           
           
           
           
            

    
    

