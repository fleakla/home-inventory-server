#!/usr/bin/env python

from bottle import Bottle, template, request, redirect
from google.appengine.api import users


testBottle = Bottle()


@testBottle.route('/tests/')
def default_handler():
    return template('webtemplates/tests/testWelcome', this_user=users.get_current_user())

