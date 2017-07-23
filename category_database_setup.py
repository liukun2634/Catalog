# -*- coding: utf-8 -*-
import os
import sys
from sqlalchemy import Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
"""This database is the template for all kinds of category and related items"""


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    """Class Category stores id,name"""
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


class Item(Base):
    """Class Item stores id, name, category_id, description"""

    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(1000))
    category_name = Column(String(20), ForeignKey('category.name'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_name': self.category_name,
        }


engine = create_engine('sqlite:///category.db')

Base.metadata.create_all(engine)
