#!/usr/bin/env python
from bottle import Bottle, template, request, redirect
from google.appengine.api import users
from google.appengine.ext import ndb
from myPackages.inventoryEntry import InventoryEntry, Work, Creator

myBottle = Bottle()


@myBottle.route('/')
def howdy():
    current_user = users.get_current_user()

    if current_user:
        my_message = "Hello, " + current_user.nickname()
        dragon = \
            "http://img4.wikia.nocookie.net/__cb20121214173011/gameofthrones/images/a/ac/HouseTargaryenMetallic.jpg"
        output = template('webtemplates/helloWorld', data=my_message, prettyImg=dragon)
        return output
    else:
        redirect(users.create_login_url(request.url))


@myBottle.error(404)
def error404handler_404(error):
    return "Like, there was a 404 that got in my Bottle.  Uncool man!\n\n" + error


@myBottle.route('/Test1')
def test1pathhandler():
    return "This is my bottle at path Test1"


@myBottle.route('/FormTest')
def testformhandler():
    return template("webtemplates/formHandler")


@myBottle.route('/saveFormTest', method='POST')
def test_form_save_handler():
    title = request.POST.get('title').strip()
    genre = request.POST.get('genre').strip()
    author = request.POST.get('author')

    data_dictionary = {'Title': title, 'Genre': genre, 'Author': author}

    return template('webtemplates/saveTest', dataDictionary=data_dictionary)


@myBottle.route('/saveAndSearchTest')
def save_and_search_test():
    current_user = check_user_status(request.url)

    return template('webtemplates/saveToDataStoreTest', user=current_user)


def build_inventory_key(default_name='DEFAULT_INVENTORY'):
    cur_user = users.get_current_user()
    if cur_user:
        default_name = cur_user.nickname()

    return ndb.Key(default_name)


@myBottle.route('/saveOrSearchBookData', method='POST')
def display_save_search_form():
    # if request.POST.get('Save'):
    entry = InventoryEntry(parent=build_inventory_key())
    entry.work = Work()
    entry.work.title = request.POST.get('title').strip()
    entry.work.creator = request.POST.get('author').strip()
    entry.work.publication_date = request.POST.get('PubDate').strip()
    entry.work.isbn_number = request.POST.get('ISBN').strip()
    # entry.put()

    return template('webtemplates/saveToDataStoreTest', user=users.get_current_user())


@myBottle.route('/credentialhandler', method='POST')
def credentialhandler():
    if request.POST.get('login'):
        redirect(users.create_login_url(request.POST.get('redirectTarget')))
    else:
        if request.POST.get('logout'):
            redirect(users.create_logout_url(request.POST.get('redirectTarget')))


def check_user_status(loginredirect='/saveAndSearchTest'):
    cur_user = users.get_current_user()
    if cur_user:
        return cur_user
    else:
        redirect(users.create_login_url(loginredirect))
