# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:

Define a function named `get_numeric_input()` that:

1. Prompts the user to enter a valid number.
2. Continuously prompts until a valid number (integer or floating-point) is entered.
3. Returns the valid number as a `float`.

The function must handle potential errors, such as:

- KeyboardInterrupt - gracefully exit, if user press 'Ctrl+C' (you can use the exit(0) function)
- Invalid input - non-numeric characters.
- Any other unexpected errors that might occur during input.
"""


### YOUR CODE HERE


# TEST:
# number = get_numeric_input()
# print(f"You entered: {number}")

### EXPECTED OUTPUT:
# Please enter a number: sds
# Invalid input. Please enter a numeric value.
# Please enter a number: 3
# You entered: 3.0

# Please enter a number: ^C (pressing CTRL+C)
# Input cancelled by user. Exiting...


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:

Defin function get_valid_username(), that prompts the user to enter their name.
Ensure the entered name meets the following criteria:

1. Contains only letters.
    - tip: you can use the string.isalpha() method
2. Starts with an uppercase letter.
    - tip: you can use the string.isupper() method
3. Is at least 2 characters long.

The function should handle invalid inputs using custom exceptions and display appropriate error messages:
- If the username contains non-alphabetic characters => "Name must contain only letters."
- If the username doesn't start with an uppercase letter=> "Name must start with an uppercase letter."
- If the username is shorter than 2 characters => "Name must be at least 2 characters long."

The function should continuously prompt the user until a valid username is entered.
Upon a valid username, the function should return the username.

"""


### YOUR CODE HERE


# TEST:
# username = get_valid_username()
# print(f"Hello, {username}!")

# EXPECTED OUTPUT:
# Please enter your name: ivan123
#         Error: Name must contain only letters.
# Please enter your name: ivan
#         Error: Name must start with an uppercase letter.
# Please enter your name: I
#         Error: Name must be at least 2 characters long.
# Please enter your name: Ivan
# Hello, Ivan!
