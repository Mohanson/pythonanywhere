import logging

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

import src.rest.routeset
import src.utils
import src.utils.log
import src.utils.settings

apis = [
    'src.rest.api.v1.version',
    'src.rest.view.view',

    'src.rest.api.v1.echo',
    'src.rest.api.v1.routes'
]


for api in apis:
    __import__(api)


settings = {
    'wsgi': src.utils.settings.tornado.wsgi,
    'xsrf_cookies': False,
    'debug': src.utils.settings.tornado.debug,
    'cookie_secret': src.utils.settings.tornado.cookie_secret,
    'gzip': True,
    'static_path': src.utils.settings.tornado.static_path,
}

if settings['wsgi']:
    application = tornado.wsgi.WSGIApplication(src.rest.routeset.routeset, **settings)
else:
    application = tornado.web.Application(src.rest.routeset.routeset, **settings)

logging.root.setLevel(logging.DEBUG)
for name in ['tornado.access', 'tornado.application', 'tornado.general']:
    logger = logging.getLogger(name)
    for handler in src.utils.log.root.handlers:
        logger.addHandler(handler)


def run():
    src.utils.log.info('Http server started on port %s' % src.utils.settings.tornado.port)
    for route in src.rest.routeset.routeset:
        src.utils.log.info('Route bind ' + route.__str__())
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(src.utils.settings.tornado.port)
    tornado.ioloop.IOLoop.instance().start()
