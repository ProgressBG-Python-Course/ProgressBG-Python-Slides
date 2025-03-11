# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Create a class called 'Car' to represent a car. The class should have the following attributes and methods:

Attributes:
- 'make': a string representing the make of the car (e.g., Toyota, Honda).
- 'model': a string representing the model of the car (e.g., Camry, Civic).
- 'year': an integer representing the manufacturing year of the car.

Methods:
- 'start_engine()': a method that prints a message indicating that the car's engine has started.
- 'stop_engine()': a method that prints a message indicating that the car's engine has stopped.

Create an instance of the 'Car' class with information about a car and demonstrate the usage of the 'start_engine' and 'stop_engine' methods.

"""


### Define the Car class


### TEST
# car1 = Car("Toyota", "Camry", 2022)
# car1.start_engine()
# car1.stop_engine()

### EXPECTED OUTPUT:
# Engine started for Toyota Camry 2022
# Engine stopped for Toyota Camry 2022


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Student' to represent a student. The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the student's name.
- 'student_id': an integer representing the student's ID.
- 'courses': a list representing the courses the student is enrolled in.

Methods:
- 'add_course(course_name)': a method that adds a course to the student's list of courses.
- 'remove_course(course_name)': a method that removes a course from the student's list of courses.
- 'list_courses()': a method that prints the list of courses the student is enrolled in.

Create an instance of the 'Student' class with your own information and demonstrate the usage of the methods.


"""


### Define the Student class


### TEST
# student1 = Student("Alice", 12345)
# student1.add_course("Math")
# student1.add_course("History")
# student1.list_courses()

### EXPECTED OUTPUT:
# Courses: Math,History


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Book' to represent a book in a library system. The class should have the following attributes and methods:

Attributes:
- 'title': a string representing the title of the book.
- 'author': a string representing the author of the book.
- 'isbn': a string representing the ISBN of the book.
- 'year': an integer representing the publication year of the book.

Methods:
- '__str__()': a method that returns a formatted string with the book's title, author, ISBN, and publication year.

Create a class called 'Library' that manages a collection of books. The class should have the following methods:

Methods:
- 'add_book(book)': adds a book to the library's collection.
- 'remove_book(isbn)': removes a book from the library by its ISBN.
- 'find_book(isbn)': finds and returns a book by its ISBN. If not found, returns None.
- 'list_books()': prints a list of all books in the library.

Create instances of the 'Book' class and demonstrate the usage of the 'Library' class by adding, removing, and listing books.
"""


### Define the Book class


### Define the Library class


### TEST
# book1 = Book("1984", "George Orwell", "123456789", 1949)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321", 1960)

# library = Library()
# library.add_book(book1)
# library.add_book(book2)

# print("List of books in the library:")
# library.list_books()

# # Remove a book
# library.remove_book("123456789")
# print("\nList of books after removal:")
# library.list_books()

# # Find a book
# book = library.find_book("987654321")
# if book:
#     print(f"\nFound book: {book}")
# else:
#     print("\nBook not found.")


### EXPECTED OUTPUT:
# List of books in the library:
# Title: 1984
# Author: George Orwell
# ISBN: 123456789
# Year: 1949
# --------------------
# Title: To Kill a Mockingbird
# Author: Harper Lee
# ISBN: 987654321
# Year: 1960
# --------------------

# List of books after removal:
# Title: To Kill a Mockingbird
# Author: Harper Lee
# ISBN: 987654321
# Year: 1960
# --------------------

# Found book: Title: To Kill a Mockingbird
# Author: Harper Lee
# ISBN: 987654321
# Year: 1960


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'BankAccount' to represent a bank account. The class should have the following attributes and methods:

Attributes:
- 'account_number': a string representing the account number.
- '__balance': a float representing the current balance of the account. It must be private

Methods:
- 'deposit(amount)': a method that adds the provided amount to the account balance.
- 'withdraw(amount)': a method that subtracts the provided amount from the account balance.
- 'get_balance()': a method that returns the current balance of the account.

Create an instance of the 'BankAccount' class with your own account information and demonstrate the usage of the methods.

"""


### Define the BankAccount class


### TEST:
# account1 = BankAccount("12345", 1000.0)
# account1.deposit(500.0)
# account1.withdraw(200.0)
# print(account1.get_balance())

# # Attempt to directly modify the balance (no effect, as __balance is private):
# account1.__balance = 0
# print(account1.get_balance())

### EXPECTED OUTPUT:
# 1300.0
# 1300.0


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Create a base class called 'Shape' to represent a geometric shape. The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the name of the shape.

Methods:
- 'area()': a method that will return the string 'Not implemented for common shape'

Create two subclasses, 'Rectangle' and 'Circle', that inherit from the 'Shape' class and implement their specific area calculation methods.

Demonstrate the usage of the 'Rectangle' and 'Circle' classes by creating instances of each and calculating their respective areas.

"""


### Define the Shape base class


### Define the Rectangle class inheriting from Shape


### Define the Circle class inheriting from Shape


### TEST:
# rectangle1 = Rectangle("Rectangle", 5.0, 3.0)
# circle1 = Circle("Circle", 2.0)
# print(rectangle1.area())
# print(f"{circle1.area():.2f}")

### EXPECTED OUTPUT:
# 15.0
# 12.57
