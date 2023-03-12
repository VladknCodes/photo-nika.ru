# Настройка SQLAlchemy - Таблица "GBmessageTMP"


import sys

# Настройка базы данных
from sqlalchemy import Column, ForeignKey, Integer, String, Text

# Определения таблицы и модели
from sqlalchemy.ext.declarative import declarative_base

# создание экземпляра declarative_base
GBase = declarative_base()


# Создание класса GBook наследуя его из класса GBase.
class GBook(GBase):
    __tablename__ = 'GBmessageTMP'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    DateMes = Column(String(12))
    Message = Column(Text)