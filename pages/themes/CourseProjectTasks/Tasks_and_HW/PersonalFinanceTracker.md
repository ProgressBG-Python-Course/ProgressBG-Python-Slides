# Python Fundamentals Course Project: Personal Finance Tracker

## Project Overview

Develop a comprehensive Personal Finance Tracker application that helps user monitor their income and expenses.

## Core Application Features

### Transaction Management

- **Record Transactions**: Add new financial transactions with details including:
  - Amount (income or expense)
  - Date and time
  - Category (e.g., groceries, utilities, salary, entertainment)
  - Payment method (cash, credit card, bank transfer)
  - Description/note
  - Tags for custom organization

- **Edit Transactions**: Modify any transaction information after creation

- **Delete Transactions**: Remove transactions from the system with confirmation

- **View Transactions**: Display transaction details in a formatted way

### Financial Organization and Search

- **Basic Search**: Find transactions by description, amount, or category
- **Advanced Filtering**: Filter transactions by:
  - Date range
  - Multiple categories
  - Income vs. expenses
  - Payment methods
  - Custom tags

### Financial Analysis

- **Statistics**: Generate insights about your finances:
  - Income vs. expenses summary
  - Spending by category breakdown
  - Monthly/weekly spending trends

### Optional Enhancements

- GUI using PyQt
- Financial data visualization using Pandas/Matplotlib
- Currency conversion support

### Data Persistence

- **Save/Load**: Automatically save financial data between sessions
- **Import/Export**: Support importing/exporting data in common formats (CSV, JSON)

## Technical Requirements

1. Data Storage and Handling
    - Use appropriate data structures (dictionaries, lists, sets) to store financial information
    - Implement file I/O for saving/loading the financial data (JSON or CSV format)
    - Include exception handling for file operations and user input

1. Object-Oriented Design
    - Hint: create Transaction and TransactionManager classes with appropriate attributes and methods

1. User Interface
    - Build a command-line interface with a menu system
    - Implement proper input validation and error messages
    - Use string formatting to display information in a readable format

1. Code Organization
    - Use virtual environment for your project
    - Organize code into modules with appropriate functions and classes
    - Create a package structure with proper imports
    - Include docstrings and comments for code documentation
    - Follow PEP 8 styling guidelines (use linters and formatters)

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
