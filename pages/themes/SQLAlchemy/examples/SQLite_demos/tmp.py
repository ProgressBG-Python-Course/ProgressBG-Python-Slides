from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///example.db", pool_size=2, max_overflow=0)
Session = sessionmaker(bind=engine)

s1 = Session()
s2 = Session()

dbapi1 = s1.connection().connection
dbapi2 = s2.connection().connection

print("Session1 DBAPI id:", id(dbapi1))
print("Session2 DBAPI id:", id(dbapi2))

# Keep both sessions open
# Borrowing a third connection would block because pool_size=2, max_overflow=0
s3 = Session()
dbapi3 = s3.connection().connection
print("Session3 DBAPI id:", id(dbapi3))  # would raise error or block if pool exhausted

s1.close()
s2.close()
s3.close()
