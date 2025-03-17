# Python Fundamentals Course Project: Personal Library Manager

## Project Overview

Develop a Personal Library Management application that allows users to organize and track their book collection.

## Core Application Features

### Book Management

- **Add Books**: Create new book entries with details including:
  - Title, author(s), ISBN
  - Publication year and publisher
  - Genre/category
  - Page count
  - Format (hardcover, paperback, e-book, audiobook)
  - Price
  - Purchase date
  - Personal rating (1-5 stars)
  - Read status (unread, in-progress, completed)
  - Custom tags/notes

- **Edit Books**: Modify any book information after creation

- **Remove Books**: Delete books from the collection with confirmation

- **View Books**: Display book details in a formatted way

### Search and Organization

- **Basic Search**: Find books by title, author, or ISBN
- **Advanced Filtering**: Filter the collection by:
  - Multiple genres
  - Read/unread status
  - Publication year range
  - Rating range
  - Custom tags

### Collection Analysis

- **Statistics**: Generate basic statistics about your collection:
  - Total books count
  - Total collection value
  - Books by genre distribution (optional)
  - Read vs. unread books ratio (optional)

### Optional Enhancements

- GUI using PyQt
- Statistics and visualization using Pandas/Matplotlib.

### Data Persistence

- **Save/Load**: Automatically save library data between sessions
- **Import/Export**: Support importing/exporting data in common formats (CSV, JSON)

## Technical Requirements

1. Data Storage and Handling
    - Use appropriate data structures (dictionaries, lists, sets) to store book information
    - Implement file I/O for saving/loading the library data (JSON or CSV format)
    - Include exception handling for file operations and user input

1. Object-Oriented Design
    - Hint: create a Book and LibraryManager classes with appropriate attributes and methods

1. User Interface
    - Build a command-line interface with a menu system
    - Implement proper input validation and error messages
    - Use string formatting to display information in a readable format.

1. Code Organization
    - Use virtual environment for your project
    - Organize code into modules with appropriate functions and classes
    - Create a package structure with proper imports
    - Include docstrings and comments for code documentation
    - Follow PEP 8 styling guidelines (use linters and formaters)

## Submission Requirements

- Your project must be in Github, in a separate repo
- Create Requirements.txt file for listing all dependencies
- Create README.md with installation and usage instructions

### Timeline

- Submission deadline: *3 weeks after course completion*

## Evaluation Criteria and Grading

- Functionality (60%): Does the application work as described? Are all required features implemented?
- Code Quality (30%): Is the code well-structured, readable, and maintainable?
- Documentation (10%): Is the code well-documented? Is the README clear and comprehensive?

### Grading Formula (2-6 Scale)

The final grade will be calculated using this formula:

**Grade = 2 + 4 × (Weighted Score ÷ 100)**

Where:

- Weighted Score = (Functionality × 0.6) + (Code Quality × 0.3) + (Documentation × 0.1)
- Each component is evaluated on a scale of 0-100%
- Final grade is rounded to the nearest 0.5

Example calculation:

- Functionality: 80% × 0.6 = 48%
- Code Quality: 70% × 0.3 = 21%
- Documentation: 90% × 0.1 = 9%
- Weighted Score: 48% + 21% + 9% = 78%
- Grade = 2 + 4 × (78 ÷ 100) = 2 + 3.12 = 5.12 = 5.0 (Very Good)
