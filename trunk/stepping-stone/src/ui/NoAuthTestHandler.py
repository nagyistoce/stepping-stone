from google.appengine.ext import webapp
from google.appengine.api import users

class NoAuthTestHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user:
            self.response.out.write("<p>Auth isn't required, but you are authed as %s.</p>" % user.email())
        else:
            self.response.out.write("<p>Auth isn't required, and you are not authed.</p>")
            
        self.response.out.write("<p>Go to the <a href='/authtest'>AuthTest</a> page.</p>")
