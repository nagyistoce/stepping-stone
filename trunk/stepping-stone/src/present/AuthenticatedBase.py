from google.appengine.ext import webapp
from google.appengine.api import users

class AuthenticatedBase(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user:
            self.AuthenticatedGet(user)
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        user = users.get_current_user()
        
        if user:
            self.AuthenticatedPost(user)
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def AuthenticatedGet(self, user):
        self.response.out.write('AUTHENTICATEDGET NOT IMPLEMENTED')

    def AuthenticatedPost(self, user):
        self.response.out.write('AUTHENTICATEDPOST NOT IMPLEMENTED')
