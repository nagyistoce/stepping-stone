'''
Created on 28/11/2010

@author: emlyn
'''

from google.appengine.ext import webapp
from google.appengine.api import users

class NoPathHandler(webapp.RequestHandler):
    '''
    Do this if there is no handler for the request
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def get(self):
        self.response.out.write('<h1>Stepping Stones</h1>')
    
    def post(self):
        pass 
    
        