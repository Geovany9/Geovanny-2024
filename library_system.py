class Book:
    def __init__(self, title, author, category, isbn):
        self.title = title
        self.author = author
        self.category = category
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}, ISBN: {self.isbn}"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}, Borrowed Books: {', '.join([str(book) for book in self.borrowed_books])}"


class Library:
    def __init__(self):
        self.books_available = {}
        self.users_registered = set()

    def add_book(self, book):
        self.books_available[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.books_available:
            del self.books_available[isbn]

    def register_user(self, user):
        self.users_registered.add(user.user_id)

    def unregister_user(self, user):
        if user.user_id in self.users_registered:
            self.users_registered.remove(user.user_id)

    def lend_book(self, user, isbn):
        if isbn in self.books_available:
            book = self.books_available[isbn]
            user.borrow_book(book)
            self.remove_book(isbn)

    def return_book(self, user, isbn):
        if isbn in self.books_available.values():
            book = self.books_available[isbn]
            user.return_book(book)
            self.add_book(book)

    def __str__(self):
        return f"Books Available: {', '.join([str(book) for book in self.books_available.values()])}, Users Registered: {', '.join([str(user_id) for user_id in self.users_registered])}"


# Ejemplo de uso
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "9780061120084")
    book3 = Book("1984", "George Orwell", "Dystopian", "9780451524935")

    user1 = User("Alice", 1)
    user2 = User("Bob", 2)

    library = Library()

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.register_user(user1)
    library.register_user(user2)

    print("Books Available in Library:")
    for book in library.books_available.values():
        print(book)

    print("\nUsers Registered in Library:")
    for user_id in library.users_registered:
        print(user_id)

    print("\nBob borrows a book:")
    library.lend_book(user2, "9780743273565")

    print("\nBooks Available in Library after Bob borrows a book:")
    for book in library.books_available.values():
        print(book)

    print("\nBob's Borrowed Books:")
    print(user2)

    print("\nBob returns the book:")
    library.return_book(user2, "9780743273565")

    print("\nBooks Available in Library after Bob returns the book:")
    for book in library.books_available.values():
        print(book)
