from google.appengine.ext import webapp
from google.appengine.api import users

class AuthTestHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user:
            self.response.out.write("Hello this is %s. <a href='/logout'>Logout</a>" % user.email())
        else:
            # this isn't right, I need to just reject requests here
            self.redirect(users.create_login_url(self.request.uri))
