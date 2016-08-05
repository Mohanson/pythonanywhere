import fnmatch
import os
import pickle
import shutil

import src.utils.settings as settings

if not os.path.exists(settings.utils.record.path):
    os.makedirs(settings.utils.record.path)


def set(name, value):
    with open(os.path.join(settings.utils.record.path, name), 'wb') as f:
        pickle.dump(value, f)


def get(name, default=None):
    try:
        with open(os.path.join(settings.utils.record.path, name), 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default


def delete(name):
    os.remove(os.path.join(settings.utils.record.path, name))


def keys(pattern='*'):
    """Get qualified keys

    Patterns are Unix shell style:

    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq
    """
    keys = []
    for i in os.scandir(settings.utils.record.path):
        if pattern == '*' or fnmatch.fnmatch(i.name, pattern):
            keys.append(i.name)
    return keys


def clear():
    shutil.rmtree(settings.utils.record.path)
    if not os.path.exists(settings.utils.record.path):
        os.makedirs(settings.utils.record.path)
