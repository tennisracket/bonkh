import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import Column, Integer, String
from database.config import Base,DBSession,engine



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(length=255))
    surname = Column(String(length=255))
    email = Column(String(length=255))

    def __init__(self,name,surname,email):
        self.name = name
        self.surname = surname
        self.email = email

    def __repr__(self):
        return "<{klass} @{id:x} {attrs}>".format(
            klass=self.__class__.__name__,
            id=id(self) & 0xFFFFFF,
            attrs=" ".join("{}={!r}".format(k, v) for k, v in self.__dict__.items()),
            )
    def save(self):
        DBSession.add(self)
        DBSession.commit()

Base.metadata.create_all(engine)
