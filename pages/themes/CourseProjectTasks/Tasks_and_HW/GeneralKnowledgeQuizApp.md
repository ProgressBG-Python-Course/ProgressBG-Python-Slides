# Python Fundamentals Course Project: General Knowledge Quiz

## Project Overview

Develop an interactive General Knowledge Quiz application that tests users on various topics, tracks their performance, and provides a customizable quiz experience.

## Core Application Features

### Quiz Management

- **Create Quizzes**: Generate quizzes with questions from:
  - Predefined categories (history, science, geography, etc.)
  - Custom categories created by the user
  - Mixed categories for general knowledge tests
  - Difficulty levels (easy, medium, hard)

- **Question Types**: Support multiple question formats:
  - Multiple choice (single correct answer)
  - True/False questions
  - Fill-in-the-blank
  - Short answer questions

- **Quiz Configuration**: Allow users to:
  - Set number of questions per quiz
  - Set time limits (optional)
  - Select specific categories or random mix
  - Choose difficulty level

### Quiz Interaction

- **Take Quiz**: Present questions with clear formatting
- **Answer Validation**: Check answers and provide immediate feedback
- **Score Tracking**: Calculate and display scores during and after quiz
- **Review Answers**: Show correct answers for missed questions

### Knowledge Base

- **Question Database**: Maintain a database of questions and answers
- **Add Questions**: Allow users to add new questions to the database
- **Edit/Delete Questions**: Modify or remove existing questions
- **Import/Export**: Support importing/exporting questions in common formats (CSV, JSON)

### Optional Enhancements

- GUI using PyQt
- Data visualization of performance metrics using Pandas/Matplotlib
- Timer functionality for timed quizzes
- User Management
- Leaderboard for multiple users

### Data Persistence

- **Save/Load**: Automatically save user profiles and quiz data between sessions
- **Backup/Restore**: Support backing up and restoring the question database

## Technical Requirements

1. Data Storage and Handling
    - Use appropriate data structures (dictionaries, lists, sets) to store quiz information
    - Implement file I/O for saving/loading the quiz data (JSON or CSV format)
    - Include exception handling for file operations and user input

1. Object-Oriented Design
    - Hint: create Question, QuestionDatabase, Quiz and QuizManager classes with appropriate attributes and methods

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
