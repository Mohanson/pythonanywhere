import json

import tornado.web

import src.settings as settings
import src.utils


class ParamsAdorner:

    def __init__(self, required=[], mayneeds=[]):
        self.required = required
        self.mayneeds = mayneeds

    def __call__(self, func):
        def wrapper(handler, *args, **kwargs):
            params = src.utils.ObjectDict()
            for key in self.required:
                try:
                    value = handler.get_argument(key)
                except tornado.web.MissingArgumentError:
                    handler.ewrite(rest.error.MissingRequiredArgument, {
                        'info': 'missing required argument: %s' % key
                    })
                    return
                else:
                    params[key] = value

            for key in self.mayneeds:
                params[key] = handler.get_argument(key, None)

            handler.args.params = params
            return func(handler, *args, **kwargs)

        return wrapper

params = ParamsAdorner


class BodyURLEncodeAdorner:

    def __init__(self, required=[], mayneeds=[]):
        self.required = required
        self.mayneeds = mayneeds

    def __call__(self, func):
        def wrapper(handler, *args, **kwargs):
            body = src.utils.ObjectDict()
            for key in self.required:
                try:
                    value = handler.get_body_argument(key)
                except tornado.web.MissingArgumentError:
                    handler.ewrite(rest.error.MissingRequiredArgument, {
                        'info': 'missing required argument: %s' % key
                    })
                    return
                else:
                    body[key] = value

            for key in self.mayneeds:
                body[key] = handler.get_argument(key, None)

            handler.args.body = body
            return func(handler, *args, **kwargs)

        return wrapper


class BodyJSONAdorner:

    def __init__(self, required=[], mayneeds=[]):
        self.required = required
        self.mayneeds = mayneeds

    def __call__(self, func):
        def wrapper(handler, *args, **kwargs):
            data = json.loads(self.request.body)
            body = src.utils.ObjectDict()
            for key in self.required:
                try:
                    value = data.get(key)
                except tornado.web.MissingArgumentError:
                    handler.ewrite(rest.error.MissingRequiredArgument, {
                        'info': 'missing required argument: %s' % key
                    })
                    return
                else:
                    body[key] = value

            for key in self.mayneeds:
                body[key] = data.get(key, None)

            handler.args.body = body
            return func(handler, *args, **kwargs)

        return wrapper

body = {
    'application/x-www-form-urlencoded': BodyURLEncodeAdorner,
    'application/json': BodyJSONAdorner
}.get(settings.tornado.content_type)
