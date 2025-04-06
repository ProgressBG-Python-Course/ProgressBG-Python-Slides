from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __str__(self):
        return f"User: {self.name}, {self.age}"


class DB:
    def __init__(self, db_name):
        self.engine = create_engine(f"sqlite:///{db_name}", echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_user(self, name, age):
        with self.Session() as session:
            session.add(User(name=name, age=age))
            session.commit()

    def create_users(self, users):
        with self.Session() as session:
            session.add_all([User(name=name, age=age) for name, age in users])
            session.commit()

    def get_user_by_name(self, name):
        with self.Session() as session:
            return session.query(User).filter_by(name=name).first()

    def get_all_users(self):
        with self.Session() as session:
            return session.query(User).all()

    def update_user(self, user_id, name, age):
        with self.Session() as session:
            user = session.get(User, user_id)
            if user:
                user.name = name
                user.age = age
                session.commit()

    def delete_user(self, user_id):
        with self.Session() as session:
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                session.commit()


if __name__ == "__main__":
    # Create db object to work with 'users.db'
    db = DB("users.db")

    # Create single user
    db.create_user("Ivan", 30)

    # Create multiple users
    users = [("Georgi", 25), ("Maria", 28), ("Petar", 35)]
    db.create_users(users)

    # Read all users
    users = db.get_all_users()
    for user in users:
        print(user)

    # Update user
    user = db.get_user_by_name("Ivan")
    if user:
        db.update_user(user.id, "Ivan Petrov", 31)

    # Delete user
    db.delete_user(2)
