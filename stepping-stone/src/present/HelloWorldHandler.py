'''
Created on 28/11/2010

@author: emlyn
'''

from google.appengine.ext import webapp
from google.appengine.api import users

class HelloWorldHandler(webapp.RequestHandler):
    '''
    Just a HelloWorld to test the webapp initialisation mechanism
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def get(self):
        self.response.out.write('Hello, world!')
    
    def post(self):
        pass 
    
        