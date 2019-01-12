from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser
from sqlalchemy.orm import sessionmaker
import os

database_dir = os.path.dirname(os.path.abspath(__file__))
config_file = database_dir+"\\config.ini"


parser = ConfigParser()
parser.read(config_file)

constring = parser['database']['constring']

engine = create_engine(constring.format(database_dir),echo=True)

Base = declarative_base()

DBSession = sessionmaker(bind=engine)()

Base.metadata.create_all(engine)