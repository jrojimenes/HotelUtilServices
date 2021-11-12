from contextlib import contextmanager
from sqlalchemy import exc
from fastapi import HTTPException
from .dbContext import Session


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
    except exc.SQLAlchemyError as e:
        session.rollback()
        Session.remove()
        print("error from session")
        print(e.__cause__)
        print(e)
        raise HTTPException(status_code=444, detail=e)
    finally:
        session.close()
        Session.remove()
