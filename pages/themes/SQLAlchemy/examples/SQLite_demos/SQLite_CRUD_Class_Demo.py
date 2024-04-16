import sqlite3

class DB:
    def __init__(self, db_name='python_course.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create users table if it doesn't exist."""
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        ''')
        self.conn.commit()

    def add_user(self, name, age):
        """Add a new user to the database."""
        self.c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()

    def get_users(self):
        """Retrieve all users from the database."""
        self.c.execute('SELECT * FROM users')
        return self.c.fetchall()

    def update_user(self, user_id, name, age):
        """Update a user's information in the database."""
        self.c.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        """Delete a user from the database."""
        self.c.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()

    def __del__(self):
        """Close the database connection when the object is deleted."""
        self.conn.close()


if __name__ == "__main__":
    db = DB()
    db.add_user('Ivan', 30)
    db.add_user('Maria', 25)
    print(db.get_users())
    db.update_user(1, 'Ivan Petrov', 31)
    # db.delete_user(2)
    print(db.get_users())
