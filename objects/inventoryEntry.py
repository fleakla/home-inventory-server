__author__ = 'fleak'

from google.appengine.ext import ndb


class Work(ndb.Model):
    title = ndb.StringProperty(indexed=False)
    creator = ndb.StructuredProperty(Creator)
    publication_date = ndb.DateProperty(indexed=False)
    isbn_number = ndb.StringProperty(indexed=False)


class Creator(ndb.Model):
    name = ndb.StringProperty(indexed=False)


class InventoryEntry(ndb.Model):
    work = ndb.StructuredProperty(Work)
    time_added = ndb.DateTimeProperty(indexed=False, auto_now_add=True)
