from sqlalchemy import create_engine
from sqlalchemys
from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.ini")

constring = parser['database']['constring']

engine = create_engine(constring,echo=False)

