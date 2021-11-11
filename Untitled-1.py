import cherrypy

class App:
    def __init__(self):
        self  = Store()

class Store:
    def __init__(self):
        self = InternationalStore()

class InternationalStore:
    app = App()
    def buy (self, id=None):
        return "prod %s, 29 euros" % str(id)
    
cherrypy.quickstart(App(), "/")