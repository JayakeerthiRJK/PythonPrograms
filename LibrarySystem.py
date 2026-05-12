class LibrarySystem:
    def __init__(self):
        self.books = []
    
    def store_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' has been stored in the library.")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' has been issued from the library.")
        else:
            print(f"Book '{book}' is not available in the library.")
    
    def return_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' has been returned to the library.")

# Object creation and method calls
library = LibrarySystem()
print(library.books)  # Should print an empty list since no books are stored yet
library.store_book("The Great RJK")
print(library.books)  # Should print the list with "The Great RJK"
library.store_book("To Kill a Monster")
print(library.books)  # Should print the list with both books

library.issue_book("The Great RJK")
print(library.books)  # Should print the list with only "To Kill a Monster"
library.return_book("The Great RJK")
print(library.books)  # Should print the list with both books again

library.issue_book("To Kill a Monster")
print(library.books)  # Should print the list with only "The Great RJK"
library.return_book("To Kill a Monster")
print(library.books)  # Should print the list with both books again
