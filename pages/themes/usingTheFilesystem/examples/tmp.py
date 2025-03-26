# 1. Basic File Reading Methods

# Reading an entire file
def read_entire_file():
    # Using open() with 'r' (read) mode
    with open("example.txt", "r") as file:
        content = file.read()  # Reads entire file as a single string
        print(content)


# Reading line by line
def read_line_by_line():
    with open("example.txt", "r") as file:
        # Method 1: Using readlines()
        lines = file.readlines()  # Returns list of all lines
        for line in lines:
            print(line.strip())  # strip() removes trailing newline

        # Method 2: Iterating directly over the file object
        file.seek(0)  # Reset file pointer to beginning
        for line in file:
            print(line.strip())


# Reading specific number of characters
def read_characters():
    with open("example.txt", "r") as file:
        chunk = file.read(50)  # Read first 50 characters
        print(chunk)


# 2. File Reading with Different Encodings
def read_with_encoding():
    # Reading files with specific encoding
    with open("international.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)


# 3. Error Handling
def safe_file_reading():
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You don't have permission to read this file.")


# 4. Reading Large Files Efficiently
def read_large_file():
    with open("large_file.txt", "r") as file:
        # Process file line by line to save memory
        for line in file:
            # Process each line without loading entire file
            process_line(line)


def process_line(line):
    # Example processing function
    print(line.strip())


# 5. Reading CSV Files
import csv


def read_csv_file():
    with open("data.csv", "r") as csvfile:
        # Using csv reader
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header row

        for row in csv_reader:
            print(row)  # Each row is a list of values


# 6. Reading JSON Files
import json


def read_json_file():
    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)
        print(data)  # Parsed JSON data


# Demonstration of different reading methods
if __name__ == "__main__":
    read_entire_file()
    read_line_by_line()
    read_characters()
    read_with_encoding()
    safe_file_reading()
    read_large_file()
    read_csv_file()
    read_json_file()
