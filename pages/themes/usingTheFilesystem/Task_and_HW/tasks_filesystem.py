# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write a function `filter_items(input_file, filter_word)` that reads a
text file (e.g., "shopping_list.txt") and writes all lines
that contain the `filter_word` to a new file. The new file should be named
with the format `<filter_word>_items.txt`. For example, if the filter word
is "milk", the output file should be named "milk_items.txt".
"""

### Given
## shopping_list.txt content:
# 1 liter of milk
# 2 apples
# Milk chocolate
# 3 bananas


### YOUR CODE HERE

### TEST:
# filter_items("shopping_list.txt", "milk")

### EXPECTED OUTPUT:
## "milk_items.txt" with content:
# 1 liter of milk
# Milk chocolate

# ---------------------------------- Task 2 ---------------------------------- #
"""DESCRIPTION:
Write a function `remove_debug_lines(input_file, output_file)` that reads a
text file "log.txt" and removes all lines containing the word "DEBUG".
"""

### Given
## log.txt content:
# INFO - Starting process
# DEBUG - Debugging the code
# ERROR - Something went wrong
# DEBUG - Another debug message


### YOUR CODE HERE

### TEST:
# remove_debug_lines("log.txt", "clean_log.txt")

### EXPECTED OUTPUT:
## The file "clean_log.txt" should be:
# INFO - Starting process
# ERROR - Something went wrong


# ---------------------------------- Task 3 ---------------------------------- #
"""DESCRIPTION:
Write a function `reverse_lines(input_file, output_file)` that reverses the
content of each line in a given text file.
The reversed lines should be saved in a new file.
"""

### Given
## A text file "input.txt" with content
# Hello
# World


### YOUR CODE HERE

### TEST:
# reverse_lines("input.txt", "output.txt")

### EXPECTED OUTPUT:
## The "output.txt" with content:
# olleH
# dlroW


# ---------------------------------- Task 4 ---------------------------------- #
"""DESCRIPTION:
Write a function `remove_blank_lines(filename)` that removes all blank lines in it.
"""

### Given
## sentences.txt content:
# This is a sentence.
#
#
# Another sentence.
#
#


### YOUR CODE HERE

### TEST:
# remove_blank_lines("sentences.txt")


### EXPECTED OUTPUT:
## The file "sentences.txt" will not contain any blank lines.
# This is a sentence.
# Another sentence.


# ---------------------------------- Task 5 ---------------------------------- #
"""DESCRIPTION:
Write a function `merge_files(file1, file2, output_file)` that merges two text
files "file1.txt" and "file2.txt" and saves the result in "merged.txt".
"""

### Given
## file1.txt content:
# Line 1 from file 1
# Line 2 from file 1

## file2.txt content:
# Line 1 from file 2
# Line 2 from file 2


### YOUR CODE HERE

### TEST:
# merge_files("file1.txt", "file2.txt", "merged.txt")


### EXPECTED OUTPUT:
# The file "merged.txt" with content:
# Line 1 from file 1
# Line 2 from file 1
# Line 1 from file 2
# Line 2 from file 2


# ---------------------------------- Task 6 ---------------------------------- #
"""DESCRIPTION:
Write a function `backup_files(src, dest)` that copies all files (but not directories)
from the source folder "src" to the destination folder "dest".

For each file, attach a timestamp suffix with current date and time to the filename
in the format 'YYYY-MM-DD_HH-MM-SS'.
For example: /src/track1.mp3 => /dest/track1.mp3_2020-01-01_18-30-45

If the destination folder doesn't exist, create it.
Do not remove the files from the source folder.

"""

### Given
# Source folder "src" contains the following files:
# /src/track1.mp3
# /src/track2.mp3
# /src/photo.jpg

# Destination folder "dest" may or may not exist.

### YOUR CODE HERE

### TEST:
# backup_files("src", "dest")

### EXPECTED OUTPUT:
## If the program is executed at 26.03.2025, 15:45:00 the "dest" folder sould contain:
# /dest/track1.mp3_2025-03-26_15-45-00
# /dest/track2.mp3_2025-03-26_15-45-00
# /dest/photo.jpg_2025-03-26_15-45-00

# The original files in the "src" folder remain untouched. If "dest" folder
# doesn't exist, it will be created automatically.
