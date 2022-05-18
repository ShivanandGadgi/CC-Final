
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'MyWebsite.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)