import src.server.apihandler
import src.server.routeset

routes = [
    r'/',
    r'/version',
    r'/echo',
]


class View(src.server.apihandler.APIHandler):

    with open('./res/static/html/base.html') as fp:
        context = fp.read()

    def get(self):
        self.write(self.context)

for route in routes:
    src.server.routeset.bind(route)(View)
