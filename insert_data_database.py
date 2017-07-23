# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from category_database_setup import Category, Item, Base,User

engine = create_engine('sqlite:///category.db')

Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)

session = DBsession()

# Create dummy user
User1 = User(name="Common", email="996529090@qq.com",
             picture='none')
session.add(User1)
session.commit()


# Item for C++
# reference to http://en.cppreference.com/w/cpp/links/libs
category1 = Category(name="C++")

session.add(category1)
session.commit()

item1 = Item(name="Boost",
             description="large collection of generic libraries (Boost License)",  # NOQA
             category=category1,
             user_id=1)
session.add(item1)
session.commit()

item2 = Item(name="GSL",
             description="Guidelines Support library implementation, recommended by Bjarne Stroustrup, Herb Sutter and Co in C++ Core Guidelines ",  # NOQA
             category=category1,
             user_id=1)
session.add(item2)
session.commit()

item3=Item(name = "BDE",
             description = " The Bloomberg Development Environment core libraries from Bloomberg L.P. (Apache License)",  # NOQA
             category = category1,
             user_id = 1)
session.add(item3)
session.commit()

item4=Item(name="Dlib",
             description="networking, threads, graphical interfaces, data structures, linear algebra, machine learning, XML and text parsing, numerical optimization, Bayesian nets, and numerous other tasks (Boost License) ",  # NOQA
             category=category1,
             user_id=1)
session.add(item4)
session.commit()

item5=Item(name="JUCE",
             description="An extensive, mature, cross-platform C++ toolkit (GPL Licens ",  # NOQA
             category=category1,
             user_id=1)
session.add(item5)
session.commit()

item5=Item(name="REASON",
             description="xml, xpath, regex, threads, sockets, http, sql, date-time, streams, encoding and decoding, filesystem, compression (GPL License)  ",  # NOQA
             category=category1,
             user_id=1)
session.add(item5)
session.commit()

item6=Item(name="Loki",
             description="Adesign patterns  ",  # NOQA
             category=category1,
             user_id=1)
session.add(item6)
session.commit()

# Item for Java
# reference to https://en.wikipedia.org/wiki/List_of_Java_APIs
category2=Category(name="Java")

session.add(category2)
session.commit()

item1=Item(name="JAI",
             description="A set of interfaces that support a high-level programming model allowing to manipulate images easily.",  # NOQA
             category=category2,
             user_id=1)
session.add(item1)
session.commit()

item2=Item(name="JDO",
             description="A specification of Java object persistence.",  # NOQA
             category=category2,
             user_id=1)
session.add(item2)
session.commit()

item3=Item(name="JMF",
             description="An API that enables audio, video and other time-based media to be added to Java applications and applets.",  # NOQA
             category=category2,
             user_id=1)
session.add(item3)
session.commit()

item4=Item(name="JNDI",
             description="An API for directory services.",  # NOQA
             category=category2,
             user_id=1)
session.add(item4)
session.commit()

item5=Item(name="JPA",
             description="A specification for object-relational mapping.",  # NOQA
             category=category2,
             user_id=1)
session.add(item5)
session.commit()

item6=Item(name="JSAPI",
             description="This API allows for speech synthesis and speech recognition.",  # NOQA
             category=category2,
             user_id=1)
session.add(item6)
session.commit()


# Item for Python
# reference to
# https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/
category3=Category(name="Python")

session.add(category3)
session.commit()

item1=Item(name="Requests",
             description="The most famous http library. Its a must have for every python developer.",  # NOQA
             category=category3,
             user_id=1)
session.add(item1)
session.commit()

item2=Item(name="Scrapy",
             description="If you are involved in webscraping then this is a must have library for you. After using this library you wont use any other.",  # NOQA
             category=category3,
             user_id=1)
session.add(item2)
session.commit()

item3=Item(name="wxPython",
             description="A gui toolkit for python. I have primarily used it in place of tkinter. You will really love it.",  # NOQA
             category=category3,
             user_id=1)
session.add(item3)
session.commit()

item4=Item(name="Pillow",
             description="A friendly fork of PIL (Python Imaging Library). It is more user friendly than PIL and is a must have for anyone who works with images.",  # NOQA
             category=category3,
             user_id=1)
session.add(item4)
session.commit()

item5=Item(name="SQLAlchemy",
             description="A database library. Many love it and many hate it. The choice is yours.",  # NOQA
             category=category3,
             user_id=1)
session.add(item5)
session.commit()

item6=Item(name="BeautifulSoup",
             description="I know its slow but this xml and html parsing library is very useful for beginners.",  # NOQA
             category=category3,
             user_id=1)
session.add(item6)
session.commit()


# Item for JavaScript
# reference to
# https://www.smashingmagazine.com/2009/03/40-stand-alone-javascript-libraries-for-specific-purposes/
category4=Category(name="JavaScript")

session.add(category4)
session.commit()

item1=Item(name="wForms",
             description="wForms is an opensource and unobtrusive library that simplifies the most common JavaScript form functions. It offers readytouse form validation functions for which can be applied by adding a class info to the form objects. Besides these, wForms has powerful form synchronization and conditional form capabilities (e.g. if x is checked, then show y).",  # NOQA
             category=category4,
             user_id=1)
session.add(item1)
session.commit()

item2=Item(name="JSTweener",
             description="A tweening library for JavaScript. Its API is similar to the famous ActionScript tweening engine Tweener. You can mention the time of the animation, define the transition effects and delays. At almost any point (like onStart, onComplete, onUpdate) you can fire new events.",  # NOQA
             category=category4,
             user_id=1)
session.add(item2)
session.commit()

item3=Item(name="FX",
             description="A lightweight library, with a YUI-like syntax, FX can create a tween for almost any CSS property. It supports color and scroll animations. Designing the to and from values of any object/property is enough.",  # NOQA
             category=category4,
             user_id=1)
session.add(item3)
session.commit()

item4=Item(name="Canvas 3D JS Library",
             description="C3DL makes writing 3D applications easy. It provides a set of math, scene and 3D object classes to make the canvas more accessible to developers who want to develop 3D content in a browser but not have to deal in depth with the 3D math needed to make it work.",  # NOQA
             category=category4,
             user_id=1)
session.add(item4)
session.commit()

item5=Item(name="Processing",
             description="This is a JavaScript port to the Processing language (a language for programming images, animation and interactions). The library is feature-rich for creating 2D outputs. It provides methods for shape/image drawing, color manipulation, fonts, objects, math functions and more.",  # NOQA
             category=category4,
             user_id=1)
session.add(item5)
session.commit()

item6=Item(name="ImageFX",
             description="This is a JavaScript library for adding effects to images, like blur, sharpen, emboss, lighten and more. ImageFX uses canvas element for creating the effects. It is compatible with all major browsers (there is a compatibility chart on the scripts page).",  # NOQA
             category=category4,
             user_id=1)
session.add(item6)
session.commit()


item1=Item(name="Folly",
             description="Facebook Open-source LibrarY. Library of C++11 components designed with practicality and efficiency in mind. ",  # NOQA
             category=category1,
             user_id=1)
session.add(item1)
session.commit()


item1=Item(name="JOGL",
             description="A wrapper library for OpenGL.",  # NOQA
             category=category2,
             user_id=1)
session.add(item1)
session.commit()


item1=Item(name="nltk",
             description="Natural Language Toolkit. I realize most people wont be using this one, but its generic enough. It is a very useful library if you want to manipulate strings. But its capacity is beyond that. Do check it out.",  # NOQA
             category=category3,
             user_id=1)
session.add(item1)
session.commit()


item1=Item(name="Mapstraction",
             description="There are several mapping providers that provide different APIs. If you need to switch providers (say from Google Maps to MapQuest), codes need to be updated. That\'s where Mapstraction comes in. It provides a common API that covers most of the popular mapping providers. By simply updating a line of code, it is possible to switch between them.",  # NOQA
             category=category4,
             user_id=1)
session.add(item1)
session.commit()


session.close()
print "added category"
