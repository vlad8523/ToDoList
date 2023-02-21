from sqlalchemy import Engine
from sqlalchemy.orm import Session
from db import insert_task
from db import Task
from db import BaseModel


def init_table(base, engine: Engine) -> None:
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)


def main() -> None:
    from loader import sm, engine

    init_table(BaseModel, engine)

    for i in range(3):
        insert_task(sm, Task(text = 'task1'))
        insert_task(sm, Task(text = 'task2'))

if __name__ == '__main__':
    main()
    print(1)