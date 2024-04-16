from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define a simple User class/table
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

# Set up the database engine and session
engine = create_engine('sqlite:///python_course.db', echo=False)  # Echo to print SQL queries
Base.metadata.create_all(engine)  # Create tables

Session = sessionmaker(bind=engine)
session = Session()


# session.add_all([
#     User(name='Ivan', age=23),
#     User(name='Maria', age=21),
#     User(name='Petar', age=28),
# ])

# session.commit()


rows = session.query(User).filter(User.age > 22).filter(User.name.like('%Ivan%')).all()
for user in rows:
    print(user)