'''
Created on 28/11/2010

@author: emlyn
'''

from google.appengine.ext import webapp
from google.appengine.api import users
#from django.utils import simplejson as json
import util.ssjson
from data.Learn import Learn
from util import ssjson
from present import AuthenticatedBase

class LearnHandler(AuthenticatedBase.AuthenticatedBase):
    '''
    REST interface for Learn entity
    '''
    
    def get(self):
        llearnName = self.request.get("name", None)
        llearn = None
        
        if llearnName:
            llearn = Learn.GetByName(llearnName)
        
        if llearn:
            ljson = ssjson.dumps(llearn.datum())
            self.response.headers["Content-Type"] = "application/json"
            self.response.out.write(ljson)
        else:
            self.error(400) # bad request
            self.response.out.write("Bad Request")
    
    def post(self):
        pass 
    
'''
MIT License

Copyright (c) 2010 Emlyn O'Regan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''