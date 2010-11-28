'''
Created on 28/11/2010

@author: emlyn
'''

import HelloWorldHandler
from present import NoPathHandler

class InitApp(object):
    '''
    This initialises the webapp application handler array
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def InitHandlers(self, aWebAppHandlers):
        aHandlers = [
         ('/helloworld', HelloWorldHandler.HelloWorldHandler),
         ('/', NoPathHandler.NoPathHandler)
        ]
        aWebAppHandlers.extend(aHandlers)
        