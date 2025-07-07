# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write a program that asks the user to enter three numbers: start, stop, and step.
Create a range object using these values and convert it to a list named 'numbers'.

TIP: Use the range(start, stop, step) function and list() to convert it to a list.
"""

### YOUR CODE HERE
# start = int(input('Enter start: '))
# stop = int(input('Enter stop: '))
# step = int(input('Enter step: '))

# numbers = list( range(start,stop, step) )
# print(f'Generated list: {numbers}')


### EXPECTED OUTPUT:
# Enter start: 2
# Enter stop: 10
# Enter step: 2
# Generated list: [2, 4, 6, 8]

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a list of numbers separated by spaces.
    Then, ask for two indices 'start' and 'end' to slice the list.
    Create a new list 'sliced_list' containing elements from 'start' to 'end' (excluding 'end').

    TIP:
        Use: input_list = user_input.split() to convert the space-separated input string into a list.

"""

### YOUR CODE HERE
# user_input = input("Enter numbers separated by spaces: ")
# input_list = user_input.split()

# start_index = int(input("Enter start index: "))
# stop_index = int(input("Enter stop index: "))

# sliced_list = input_list[start_index:stop_index]
# print(f"Sliced list: {sliced_list}")

### EXPECTED OUTPUT:
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9
# Enter start index: 2
# Enter end index: 6
# Sliced list: ['3', '4', '5', '6']

# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 1 to 50 using range().
    Then, create a new list 'evens' that contains only the even numbers from
    this list using slicing.

    TIP: Use range(start, stop) to create the initial list.
        Use slicing with a step to extract every second element.
"""

### YOUR CODE HERE
# numbers = list(range(1, 51))
# evens = numbers[1::2]

# print(f"Original list: {numbers}")
# print(f"Even numbers: {evens}")

### EXPECTED OUTPUT:
# Original list: [1, 2, 3, ..., 50]
# Even numbers: [2, 4, 6, ..., 50]

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 100 to 50 (inclusive), counting down by 5.
    Then, create a new list 'first_half' that contains only the first half of this list using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
        Use slicing to extract the first half.
"""

### YOUR CODE HERE
# original_list = list(range(100, 49, -5))

# # Find the midpoint
# midpoint = len(original_list) // 2

# # Slice the first half (including midpoint)
# first_half = original_list[:midpoint+1]

# print(f'Original list: {original_list}')
# print(f'First half: {first_half}')

### EXPECTED OUTPUT:
# Original list: [100, 95, 90, ..., 50]
# First half: [100, 95, 90, ..., 75]

# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word.
    Create a new string 'reversed_word' that contains the word in reverse order using slicing.

    TIP: Use slicing with a negative step to reverse a string.
"""

### YOUR CODE HERE
# word = input('Enter a word: ')
# reversed_word = word[::-1]
# print(f'Reversed word: {reversed_word}')

### EXPECTED OUTPUT:
# Enter a word: Python
# Reversed word: nohtyP

# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 10 to 100 with a step of 10.
    Then, create a new list 'middle_part' containing all elements except the first and last two using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
         Use slicing to remove the first and last two elements.
"""

### YOUR CODE HERE
# original_list = list(range(10,101,10))
# middle_part = original_list[2:-2]

# print(f'Original list: {original_list}')
# print(f'Middle part: {middle_part}')

### EXPECTED OUTPUT:
# Original list: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Middle part: [30, 40, 50, 60, 70, 80]

# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a sentence.
    Create a new string 'every_second_char' that contains every second character from the sentence using slicing.

    TIP: Use slicing with a step to extract every second character.
"""

### YOUR CODE HERE
# sentence = input('Enter a sentence: ')
# every_second_char = sentence[::2]

# print(f'Every second character: {every_second_char}')


### EXPECTED OUTPUT:
# Enter a sentence: Python slicing is powerful!
# Every second character: Pto lcn spwru!

# ---------------------------------- Task 8 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_names' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### YOUR CODE HERE
# names = []

# names.append( input('Enter 1st name: ') )
# names.append( input('Enter 2d name: ') )
# names.append( input('Enter 3d name: ') )

# # copy names
# sorted_names = names[:]

# # sort
# sorted_names.sort()
# print(f'Originally entered names: {names}')
# print(f'Sorted names: {sorted_names}')

### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2d name: Ivan
# Enter 3d name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']

# ---------------------------------- Task 9 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word and then checks if the word is a palindrome.
    A palindrome is a word that reads the same forward and backward, ignoring case.

    Tip: you can use str.lower() to convert a string to lowercase
"""

### YOUR CODE HERE
# word = input('Enter a word: ')

# # Convert the word to lowercase for case-insensitive comparison
# lower_word = word.lower()


# if lower_word==lower_word[::-1]:
#     print(f'The word \'{word}\' is a palindrome')
# else:
#     print(f'The word \'{word}\' is not a palindrome')

### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome
