__author__ = 'fleak'

from google.appengine.ext import ndb


class Creator(ndb.Model):
    name = ndb.StringProperty()


class Work(ndb.Model):
    title = ndb.StringProperty(indexed=True)
    creator = ndb.StringProperty(indexed=True)
    publication_date = ndb.DateProperty(indexed=False)
    isbn_number = ndb.StringProperty(indexed=True)


class InventoryEntry(ndb.Model):
    work = ndb.StructuredProperty(Work)
    time_added = ndb.DateTimeProperty(indexed=False, auto_now_add=True)
