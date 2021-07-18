from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Musician, Instrument, ContactInfo

# connect to server PostgreSQL on localhost with psycopg2
engine = create_engine(f'postgresql+psycopg2://postgres:1111@localhost/test', echo=True)
engine.connect()

carl = Musician(
    first_name='Carl',
    second_name='Jonatan',
    contact_info=ContactInfo(
        mail='carlj1987@gmail.com',
        phone_number='+7 (978) 870-95-22'
    ),
    instruments=[
        Instrument(
            name='Guitar'
        ),
        Instrument(
            name='Bass guitar'
        )
    ]
)

# open session
session = sessionmaker(bind=engine)
s = session()

s.add(carl)

s.commit()

# close connection
engine.dispose()
