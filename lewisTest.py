#!/usr/bin/env python
import webapp2
from bottle import Bottle

myBottle = Bottle()

@myBottle.route('/')
def howdy():
    return "Hello World!  I'm in my Bottle!"

@myBottle.error(404)
def errorHandler_404(error):
    return "Like, there was a 404 that got in my Bottle.  Uncool man!"

@myBottle.route('/Test1')
def test1PathHandler():
    return "This is my bottle at path Test1"


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)