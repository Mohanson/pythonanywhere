import logging

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

import src.log
import src.service.routeset
import src.settings
import src.utils

apis = [
    'src.service.view.view',
    'src.service.api.v1.version',
    'src.service.api.v1.echo',
    'src.service.api.v1.routes'
]


for api in apis:
    __import__(api)


settings = {
    'wsgi': src.settings.tornado.wsgi,
    'xsrf_cookies': False,
    'debug': src.settings.tornado.debug,
    'cookie_secret': src.settings.tornado.cookie_secret,
    'gzip': True,
    'static_path': src.settings.tornado.static_path,
}

if settings['wsgi']:
    application = tornado.wsgi.WSGIApplication(src.service.routeset.routeset, **settings)
else:
    application = tornado.web.Application(src.service.routeset.routeset, **settings)

logging.root.setLevel(logging.DEBUG)
for name in ['tornado.access', 'tornado.application', 'tornado.general']:
    logger = logging.getLogger(name)
    for handler in src.log.root.handlers:
        logger.addHandler(handler)


def run():
    src.log.info('Http server started on port %s' % src.settings.tornado.port)
    for route in src.service.routeset.routeset:
        src.log.info('Route bind ' + route.__str__())
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(src.settings.tornado.port)
    tornado.ioloop.IOLoop.instance().start()
