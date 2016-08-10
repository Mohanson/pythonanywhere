import sys

import toml


class ObjectDict(dict):

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value


with open('./res/settings.toml') as f:
    settings = toml.load(f, _dict=ObjectDict)

sys.modules['src.settings'] = settings
