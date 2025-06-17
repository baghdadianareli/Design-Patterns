class LibraryManagingSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.employees = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from library.")
        else:
            print("Book not found in library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered.")

    def unsubscribe_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"User '{user.name}' unsubscribed.")
        else:
            print("User not found.")

class Book:
    def __init__(self, title, author, genre, publish_date, availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publish_date = publish_date
        self.availability = availability

    def order_book(self):
        if self.availability:
            self.availability = False
            print(f"The book '{self.title}' has been ordered.")
        else:
            print(f"Sorry, '{self.title}' is not available.")

    def return_book(self):
        self.availability = True
        print(f"The book '{self.title}' has been returned.")

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book):
        library.remove_book(book)

# Example usage
if __name__ == "__main__":
    library = LibraryManagingSystem()

    book1 = Book("1984", "George Orwell", "Dystopian", "1949")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "1960")

    user1 = User("Alice", 25)
    emp1 = Employee("Bob", 40)

    library.register_user(user1)

    emp1.add_book(library, book1)
    emp1.add_book(library, book2)

    book1.order_book()

    book1.return_book()

    emp1.remove_book(library, book2)