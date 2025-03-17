# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write an EvensIterator class, such that its objects can be used in for loops, iterating over the even numbers in specified [start, end] range (both inclusive).
"""


### YOUR CODE HERE


### TEST:
# for x in EvensRange(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a generator function (evens_generator), such that will yield an even number
in specified [start, end] range (both inclusive).
"""


### YOUR CODE HERE


### TEST:
# for x in evens_generator(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Define a generator function which will yield all Cyrillic Upper Letters, starting from 'А', to 'Я'
Tip: you can get a letter form its code, using the chr() built-in function, as shown in next examples:
print( chr(1040) )
# 'А''

print( chr(1041) )
# 'Б'

print( chr(1071) )
# 'Я'
"""


### YOUR CODE HERE


# TEST:
# for l in cyrilic_letter_generator():
#     print(l, end=",")

### EXPECTED OUTPUT:
# А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я,

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create both a generator function (words_from_sentence) and an iterator class (WordsFromSentence) that produces words from a sentence. Both should split the input sentence by spaces and return each word
one at a time when iterated over.
Your implementation should handle empty sentences properly.

"""


### YOUR CODE HERE


# # TEST case 1: Using the iterator class
# print("Test with iterator class:")
# for w in WordsFromSentence("this is a test"):
#     print(w)

# # TEST case 2: Using the generator function
# print("\nTest with generator function:")
# for w in words_from_sentence("this is a test"):
#     print(w)

### EXPECTED OUTPUT:
# Test with iterator class:
# this
# is
# a
# test
#
# Test with generator function:
# this
# is
# a
# test
