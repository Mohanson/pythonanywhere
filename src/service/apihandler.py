import tornado.web

import src.utils


class APIHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(APIHandler, self).__init__(application, request, **kwargs)
        if 'Origin' in self.request.headers:
            self.add_header('Access-Control-Allow-Origin', self.request.headers['Origin'])
        self.add_header('Access-Control-Allow-Credentials', 'true')
        self.add_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS,PUT,DELETE')
        self.add_header('Access-Control-Allow-Headers',
                        'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type')
        self.add_header('Connection', 'keep-alive')

        self.args = src.utils.ObjectDict()
        self.args.params = src.utils.ObjectDict()
        self.args.body = src.utils.ObjectDict()

    def options(self, *args, **kwargs):
        pass

    def get_current_user(self):
        user = self.get_secure_cookie('user')
        return user

    def set_current_user(self, user, expires_days=30):
        self.set_secure_cookie('user', user, expires_days=expires_days)

    def ewrite(self, err, chunk={}):
        assert isinstance(chunk, dict), 'ewrite function accept dict data only'
        self.write(dict({'err': err.err, 'errname': err.errname}, **chunk))

    def swrite(self, chunk={}):
        assert isinstance(chunk, dict), 'swrite function accept dict data only'
        self.write(dict({'err': 0}, **chunk))
