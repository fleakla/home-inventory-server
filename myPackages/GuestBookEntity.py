__author__ = 'fleak'

from google.appengine.ext import ndb


class GuestbookEntry(ndb.Model):
    time_added = ndb.DateTimeProperty(auto_now_add=True)
    comment_author = ndb.StringProperty()
    comment = ndb.StringProperty(indexed=False)