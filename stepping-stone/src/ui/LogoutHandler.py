from google.appengine.ext import webapp
from google.appengine.api import users

class LogoutHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        redirectpage = self.request.get("redirect", "/noauthtest")

        if user:
            self.redirect(users.create_logout_url(redirectpage))
        else:
            self.redirect(redirectpage)
