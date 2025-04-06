from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class DB:
    def __init__(self, db_name):
        try:
            self.engine = create_engine(f"sqlite:///{db_name}", echo=False)
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print('*** Connection Established ***')
        except Exception as e:
            print(e)
            exit()

    def authenticate(self, user_name, password):
        with self.Session() as session:
            stmt = select(User).where(User.username == user_name, User.password == password)
            return session.execute(stmt).scalar()


if __name__ == "__main__":
    db = DB("pyqtDemos.db")

    user_name = "Maria"
    password = "maria123"

    authenticated = db.authenticate(user_name=user_name, password=password)

    if authenticated:
        print("Login Successful")
    else:
        print("Login Failed")
