from sqlalchemy.engine import create_engine,Engine
from sqlalchemy import URL
from typing import Union
from sqlalchemy.orm import sessionmaker, Session


def get_engine(url: Union[URL, str]) -> Engine:
    engine = create_engine(url, echo=True)
    return engine

def get_session_maker(engine: Engine) -> sessionmaker:
    return sessionmaker(engine, class_=Session)