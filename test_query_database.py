# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from category_database_setup import Base, Category, Item


engine = create_engine("sqlite:///category.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

category = session.query(Category).first()
#category = session.query(Category).filter_by(id=3)
print category.name
category2 = session.query(Category).filter_by(name="C++").one()
print category2.name
session.close()