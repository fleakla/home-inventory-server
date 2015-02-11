#!/usr/bin/env python
import webapp2
from bottle import Bottle, template

myBottle = Bottle()

@myBottle.route('/')
def howdy():
    myMessage = "Message in a Bottle"
    tattoo = "http://blog-cdn.tattoodo.com/wp-content/uploads/2014/04/House-of-Targaryen.jpg"
    output = template('webtemplates/helloWorld', data=myMessage, prettyImg=tattoo)
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