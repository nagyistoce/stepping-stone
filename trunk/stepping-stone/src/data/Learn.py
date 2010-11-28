'''
Created on 28/11/2010

@author: emlyn
'''

from google.appengine.ext import db

class Learn(db.Model):
    '''
    A Learn Entity
    '''

    name = db.StringProperty()
    content = db.StringProperty(multiline=True)
    lastModifiedBy = db.UserProperty(auto_current_user = True)
    lastModifiedAt = db.DateTimeProperty(auto_now_add = True, required=True)
    
    def datum(self):
        return {
            "name": self.name, 
            "content": self.content,
            "lastModifiedBy": self.lastModifiedBy,
            "lastModifiedAt": self.lastModifiedAt
            }

    def GetByName(cls, aName):
        retval = None
        lqry = Learn.all().filter('name =', aName)
        litems = lqry.fetch(1)      
        if litems:
            retval = litems[0]
        return retval
    GetByName = classmethod(GetByName)
    
        
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