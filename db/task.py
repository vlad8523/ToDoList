from sqlalchemy import Column, Integer, Text
from .base import BaseModel

class Task(BaseModel):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    text = Column(Text, unique=False)