from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationships
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurant"

class MenuItem(Base):
    __tablename__ = "menu_item"

engine = create_engine("sqlite:///restaurantmenu.db")
