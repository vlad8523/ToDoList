from .task import Task
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

def insert_task(sm: sessionmaker[Session], task: Task) -> None:
    with sm() as session:
        with session.begin():
            session.add(task)
