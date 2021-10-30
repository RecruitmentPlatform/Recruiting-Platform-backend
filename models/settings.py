from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///models/platform.db', echo=True)  #use when run the app
# engine = create_engine('sqlite:///platform.db', echo=True) 
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()