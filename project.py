#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kun Liu
# @Date: 2017-07-07 19:21:22

"""
  This is the project for a catalog page
  run it by using python project.py or ./project.py
  The page would show on localhost:8000
"""

from functools import wraps
from flask import Flask, render_template
from flask import jsonify, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from category_database_setup import Base, Category, Item, User

from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Conect to the category sqlite database
engine = create_engine("sqlite:///category.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show index or Home page


@app.route('/')
@app.route('/catalog')
def showCatalog():
    all_category = session.query(Category).all()
    latest_items = session.query(Item).order_by(Item.id.desc()).limit(5)
    return render_template('index.html', all_category=all_category,
                           latest_items=latest_items, session=login_session)

# Index JSON page


@app.route('/catalog/JSON')
def showCatalogJSON():
    category = session.query(Category).all()
    return jsonify(Category=[i.serialize for i in category])

# Show every category items


@app.route('/catalog/<category_name>')
def showItems(category_name):
    category = session.query(Category).filter_by(name=str(category_name)).one()
    if category:
        items = session.query(Item).filter_by(
            category_name=category.name).all()
        all_category = session.query(Category).all()
        return render_template('category.html', category=category,
                               items=items, all_category=all_category)
    else:
        return "404 not found %s" % category_name

# Category JSON page


@app.route('/catalog/<category_name>/JSON')
def showItemsJSON(category_name):
    category = session.query(Category).filter_by(name=str(category_name)).one()
    if category:
        items = session.query(Item).filter_by(category_name=category.name)
        return jsonify(Items=[i.serialize for i in items])
    else:
        return "404 not found %s" % category_name

# Show one item in details


@app.route('/catalog/<category_name>/<item_name>')
def showItem(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    if category:
        item = session.query(Item).filter_by(
            category_name=category.name, name=item_name).one()
        return render_template('item.html', category=category,
                               item=item, session=login_session)
    else:
        return "404 not found %s" % item_name

# Item JSON page


@app.route('/catalog/<category_name>/<item_name>/JSON')
def showItemJSON(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    if category:
        item = session.query(Item).filter_by(
            category_name=category.name, name=item_name).one()
        return jsonify(Item=item.serialize)
    else:
        return "404 not found %s" % item_name

# Decorator for login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('showLogin'))
        return f(*args, **kwargs)
    return decorated_function

# New item (need Login)


@app.route('/catalog/new', methods=['GET', 'POST'])
@login_required
def newItem():
  
    if request.method == 'POST':
        new_item = Item(name=request.form['name'],
                        description=request.form['description'],
                        category_name=request.form['category_name'],
                        user_id=login_session['user_id'])
        session.add(new_item)
        flash('New Item %s Successfully Created' % new_item.name)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        all_category = session.query(Category).all()
        return render_template('newitem.html', all_category=all_category)

# Edit item(need Login)


@app.route('/catalog/<category_name>/<item_name>/edit',
           methods=['GET', 'POST'])
@login_required
def editItem(category_name, item_name):
    # Only login can query
    edit_item = session.query(Item).filter_by(
        name=item_name, category_name=category_name).one()
    # Check if user can edit item
    if edit_item.user_id != login_session['user_id']:
        return render_template('forbidedit.html')

    if request.method == 'POST':
        if request.form['name']:
            edit_item.name = request.form['name']
        if request.form['description']:
            edit_item.description = request.form['description']
        if request.form['new_category_name'] != category_name:
            edit_item.category_name = new_category_name
        session.add(edit_item)
        session.commit()
        # redirect to the former category page
        return redirect(url_for('showItems', category_name=category_name))
    else:
        # category is to show all the category
        all_category = session.query(Category).all()
        return render_template('edititem.html',
                               item=edit_item, all_category=all_category)

# Delete item(need Login)


@app.route('/catalog/<category_name>/<item_name>/delete',
           methods=['GET', 'POST'])
@login_required
def deleteItem(category_name, item_name):
    # Only login can query    
    delete_item = session.query(Item).filter_by(
        name=item_name, category_name=category_name).one() 
     # Check if user can delete item
    if delete_item.user_id != login_session['user_id']:
        return render_template('forbiddelete.html')

    if request.method == 'POST':
        session.delete(delete_item)
        session.commit()
        return redirect(url_for('showItems', category_name=category_name))
    else:
        return render_template('deleteitem.html', item=delete_item)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog Web Application"

# Login page


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

# Connect page


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    # TODO: There are login in bug here when you login in twice without logout
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response =\
            make_response(json.dumps(
                'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius:"\
    " 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# disconnect- Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']  # NOQA
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for("showCatalog"))
    else:

        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# About me html


@app.route('/about')
def about():
    return render_template('about.html')


# main function to run the flask app
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
