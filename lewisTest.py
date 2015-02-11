#!/usr/bin/env python
import webapp2
from bottle import Bottle, template

myBottle = Bottle()

@myBottle.route('/')
def howdy():
    mymessage = "Message in a Bottle"
    dragon = "http://img4.wikia.nocookie.net/__cb20121214173011/gameofthrones/images/a/ac/HouseTargaryenMetallic.jpg"
    output = template('webtemplates/helloWorld', data=mymessage, prettyImg=dragon)
    return output

@myBottle.error(404)
def errorHandler_404(error):
    return "Like, there was a 404 that got in my Bottle.  Uncool man!"

@myBottle.route('/Test1')
def test1PathHandler():
    return "This is my bottle at path Test1"


@myBottle.route('/FormTest')
def testFormHandler():
    return template('webtemplates/formHandler')

@myBottle.route('/saveFormTest', method='POST')
def testFormSaveHandler():
    return "I handled a post event!"



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)