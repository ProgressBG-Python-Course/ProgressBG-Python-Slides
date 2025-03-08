# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    A library keeps a record of borrowed books in a dictionary,
    where the keys are book titles and the values are the number of copies borrowed.
    Implement functions to:
    a. Borrow a book.
    b. Return a book.
    c. Display all borrowed books.
"""

# borrowed_books = {
#     "Harry Potter": 2,
#     "The Hobbit": 1,
#     "1984": 3,
#     "Pride and Prejudice": 0,
# }

# def borrow_book(book):
#     borrowed_books[book] = borrowed_books.get(book, 0) + 1
#     print(f"'{book}' borrowed successfully.")

# def return_book(book):
#     if book in borrowed_books and borrowed_books[book] > 0:
#         borrowed_books[book] -= 1
#         print(f"'{book}' returned successfully.")
#     else:
#         print("Invalid return.")

# def show_books():
#     print("Currently borrowed books:", borrowed_books)

# def main():
#     action = input("Enter action (borrow/return/show): ").strip().lower()
#     if action == "borrow":
#         book = input("Enter book title: ").strip()
#         borrow_book(book)
#     elif action == "return":
#         book = input("Enter book title: ").strip()
#         return_book(book)
#     elif action == "show":
#         show_books()
#     else:
#         print("Invalid action.")

# main()


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    A restaurant maintains a menu with dishes and their prices in a dictionary.
    Implement functions to:
    a. Add a new dish.
    b. Update the price of an existing dish.
    c. Display all menu items.
"""

# menu = {
#     "Pizza": 12.99,
#     "Burger": 9.49,
#     "Pasta": 10.99
# }

# def add_dish(dish, price):
#     menu[dish] = price
#     print(f"Added {dish} for ${price:.2f}.")

# def update_price(dish, price):
#     if dish in menu:
#         menu[dish] = price
#         print(f"Updated {dish} to ${price:.2f}.")
#     else:
#         print("Dish not found.")

# def show_menu():
#     for dish, price in sorted(menu.items()):
#         print(f"{dish}: ${price:.2f}")

# while True:
#     action = input("Enter action (add/update/show/exit): ").strip().lower()
#     if action == "add":
#         dish = input("Enter dish name: ").strip()
#         price = float(input("Enter price: "))
#         add_dish(dish, price)
#     elif action == "update":
#         dish = input("Enter dish name: ").strip()
#         price = float(input("Enter new price: "))
#         update_price(dish, price)
#     elif action == "show":
#         show_menu()
#     elif action == "exit":
#         print("Good buy!")
#         break
#     else:
#         print("Invalid action.")


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    A school maintains student grades in a dictionary.
    Implement functions to:
    a. Add a student.
    b. Add a grade for a student.
    c. Calculate and display the average grade for a student.
"""

# grades = {
#     "Alice": [85, 90, 78],
#     "Bob": [88, 92],
#     "Charlie": [70, 75, 80]
# }

# def add_student(student):
#     if student in grades:
#         print("Student already exists.")
#     else:
#         grades[student] = []
#         print(f"{student} added.")

# def add_grade(student, grade):
#     if student in grades:
#         grades[student].append(grade)
#         print(f"Added grade {grade} for {student}.")
#     else:
#         print("Student not found.")

# def calculate_average(student):
#     if student in grades and grades[student]:
#         avg = sum(grades[student]) / len(grades[student])
#         print(f"Average grade for {student}: {avg:.2f}")
#     else:
#         print("Student not found or no grades available.")

# def solution4():
#     action = input("Enter action (add student/add grade/average): ").strip().lower()
#     if action == "add student":
#         student = input("Enter student name: ").strip()
#         add_student(student)
#     elif action == "add grade":
#         student = input("Enter student name: ").strip()
#         grade = int(input("Enter grade: "))
#         add_grade(student, grade)
#     elif action == "average":
#         student = input("Enter student name: ").strip()
#         calculate_average(student)
#     else:
#         print("Invalid action.")

# solution4()
