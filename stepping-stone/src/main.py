'''
Created on 27/11/2010

@author: emlyn
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from present.InitApp import InitApp

lwebapphandlers = []
 
InitApp().InitHandlers(lwebapphandlers)

application = webapp.WSGIApplication(
    lwebapphandlers,
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()