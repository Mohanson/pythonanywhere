import os.path

import src.service.apihandler
import src.service.routeset

routes = [
    r'/',
    r'/version',
    r'/echo',
]


class View(src.service.apihandler.APIHandler):

    with open('./res/static/html/base.html') as fp:
        context = fp.read()

    def get(self):
        self.write(self.context)

for route in routes:
    src.service.routeset.bind(route)(View)
