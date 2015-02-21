#!/usr/bin/env python

from bottle import Bottle, template, request, redirect
from google.appengine.api import users
from google.appengine.ext import ndb
from myPackages.GuestBookEntity import GuestbookEntry


guestBottle = Bottle()

DEFAULT_GUESTBOOK_NAME = 'DEFUALT_GUESTBOOK'


def get_guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    return ndb.Key('LewisGuestbook', guestbook_name)


@guestBottle.route('/guestbook/')
def guestbook():
    cur_user = users.get_current_user()
    return template('webtemplates/guestbook/sign', this_user=cur_user,
                    redirect_path=request.path)


@guestBottle.route('/guestbook/sign/', method='POST')
def sign_guestbook():
    cur_user = users.get_current_user()
    entry = GuestbookEntry(parent=get_guestbook_key())
    entry.comment_author = cur_user.nickname()
    entry.comment = request.POST.get('comment').strip()
    entry.put()
    return redirect('/guestbook/fetchAll/')


@guestBottle.route('/guestbook/fetchAll/', method=['GET', 'POST'])
def fetch_all_comments():
    query = GuestbookEntry.query(ancestor=get_guestbook_key())

    filter_text = request.POST.get('filterText')

    if filter_text:
        query = query.filter(GuestbookEntry.comment_author >= filter_text)
        query = query.filter(GuestbookEntry.comment_author < filter_text + u"\ufffd")
        query = query.order(GuestbookEntry.comment_author)

    query = query.order(-GuestbookEntry.time_added)
    query_results = query.fetch()

    return template('webtemplates/guestbook/fetchallcomments', this_user=users.get_current_user(),
                    redirect_path=request.path, fetch_results=query_results)