import sqlite3

connection = sqlite3.connect("python_course.db")

cursor = connection.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS employees (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     position TEXT NOT NULL,
#     office TEXT,
#     age INTEGER,
#     start_date TEXT
# )
# ''')
# connection.commit()

# cursor.execute('''
# INSERT INTO employees (name, position, office, age, start_date)
# VALUES ('Ivan Ivanov', 'Software Engineer', 'Sofia', 30, '2022-01-01')
# ''')
# connection.commit()

# cursor.execute('SELECT * FROM employees')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# Update data
cursor.execute('''
UPDATE employees SET age = 31 WHERE name = 'Ivan Ivanov'
''')
# connection.commit()

# Delete data
cursor.execute('''
DELETE FROM employees WHERE name = 'Ivan Ivanov'
''')
connection.commit()