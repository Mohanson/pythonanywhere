import sys

import toml

import src.utils

with open('./res/settings.toml') as f:
    setting = toml.load(f, _dict=src.utils.ObjectDict)

sys.modules['src.utils.settings'] = setting
