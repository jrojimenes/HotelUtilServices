import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from ..Domain import config

engine = sa.create_engine(config.get_sql_uri(), pool_pre_ping=True, pool_recycle=3600, connect_args={'connect_timeout': 1200})

Base = declarative_base(bind=engine)

# create a configured "Session" class
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
