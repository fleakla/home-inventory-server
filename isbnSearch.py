#!/usr/bin/env python

from bottle import Bottle, template, request
from google.appengine.api import urlfetch


google_books_url = "https://www.googleapis.com/books/v1/volumes?q=%s"
isbn_search_param_str = "{ISBN:%s}"

isbnBottle = Bottle()


@isbnBottle.route('/searchISBN/', method=['GET'])
def searchISBN():
    isbn_str = request.GET.get('ISBN')
    results = None
    if isbn_str:
        parm = isbn_search_param_str % isbn_str
        url_str = google_books_url % parm
        results = urlfetch.fetch(url=url_str)
        print(results.content)

    return template('webtemplates/inventory/searchISBN')
