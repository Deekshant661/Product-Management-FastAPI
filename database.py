from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#We use sessionlocal to access the database.
#how do we create an object of sessionlocal?
#we just have to call the constructor of sessionmaker class and that will create the object for us.
db_url= "postgresql://postgres:9999@localhost:5432/fastdb"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)