#!/usr/bin/env python
import json

from bottle import Bottle, template, request
from google.appengine.api import urlfetch


google_books_url = "https://www.googleapis.com/books/v1/volumes?q=%s"
isbn_search_param_str = "{ISBN:%s}"

isbnBottle = Bottle()

wanted_gbooks_fields = ['selfLink', 'volumeInfo']
wanted_volume_info = ['title', 'subtitle', 'authors', 'publisher', 'publishedDate', 'description',
                      'industryIdentifiers',
                      'pageCount', 'categories', 'imageLinks', 'previewLink', 'canonicalVolumeLink']


def extract_fields(gbooks_results=None):
    ret_hash = {}
    if gbooks_results and gbooks_results['totalItems'] > 0:
        primary_result = gbooks_results['items'][0]
        for field in wanted_gbooks_fields:
            # print(field)
            if field == 'volumeInfo':
                for info_item in wanted_volume_info:
                    if info_item in primary_result[field]:
                        # print("     " + info_item)
                        ret_hash[info_item] = primary_result[field][info_item]
                    else:
                        # print("      no " + info_item)
                        ret_hash[info_item] = None
            else:
                if field in primary_result:
                    # print("  found " + field)
                    ret_hash[field] = primary_result[field]
                else:
                    # print("  not found " + field)
                    ret_hash[field] = None

    return ret_hash


@isbnBottle.route('/searchISBN/', method=['GET'])
def searchISBN():
    isbn_str = request.GET.get('ISBN')
    extracted = None
    if isbn_str:
        parm = isbn_search_param_str % isbn_str
        url_str = google_books_url % parm
        results = urlfetch.fetch(url=url_str)
        results = json.loads(results.content)
        extracted = extract_fields(results)

    return template('webtemplates/inventory/searchISBN', srch_results=extracted)
