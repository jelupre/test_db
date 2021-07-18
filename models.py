from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Musician(Base):
    __tablename__ = 'musicians'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    instruments = relationship('Instrument', uselist=False, back_populates='musician')
    contact_info = relationship('ContactInfo', uselist=False, back_populates='musician')


class Instrument(Base):
    __tablename__ = 'instruments'

    musician = relationship('Musician', back_populates='instruments')

    id = Column(Integer, primary_key=True, nullable=False)
    musician_id = Column(Integer, ForeignKey('musicians.id'))
    name = Column(String)


class ContactInfo(Base):
    __tablename__ = 'contact_info'

    musician = relationship('Musician', back_populates='contact_info')

    musician_id = Column(Integer, ForeignKey('musicians.id'), primary_key=True)
    mail = Column(String)
    phone_number = Column(String)
