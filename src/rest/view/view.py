import os.path

import src.rest.apihandler
import src.rest.routeset
import src.utils.settings as settings

routes = [
    r'/',
    r'/version',
    r'/echo',
]


class View(src.rest.apihandler.APIHandler):

    with open('./res/static/html/base.html') as fp:
        context = fp.read()

    def get(self):
        self.write(self.context)

for route in routes:
    src.rest.routeset.bind(route)(View)
