import logging
import logging.handlers
import os
import os.path
import sys
import time

import src.settings as settings

if settings.utils.log.file.enable and not os.path.exists(settings.utils.log.file.path):
    os.makedirs(settings.utils.log.file.path)


class LogRecord(logging.LogRecord):

    def __init__(self, name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
        super(LogRecord, self).__init__(name, level, pathname, lineno, msg, args, exc_info, func, sinfo, **kwargs)
        self.created = time.time() + time.timezone

logging._logRecordFactory = LogRecord


class Formatter(logging.Formatter):

    def __init__(self, fmt):
        super(Formatter, self).__init__(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S')


class StreamHandler(logging.StreamHandler):

    def __init__(self, level=settings.utils.log.level, formats=settings.utils.log.stream.format):
        super(StreamHandler, self).__init__(sys.stdout)
        self.setFormatter(Formatter(formats))
        self.setLevel(level)


class TimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):

    def __init__(self, name, level=settings.utils.log.level, formats=settings.utils.log.file.format):
        super(TimedRotatingFileHandler, self).__init__(
            filename=os.path.join(settings.utils.log.file.path, name + '.log'), when='midnight', interval=1,
            backupCount=7, encoding='utf-8', delay=False, utc=True
        )
        self.setFormatter(Formatter(formats))
        self.setLevel(level)

root = logging.getLogger(settings.project.name)
root.setLevel(settings.utils.log.level)
root.addHandler(StreamHandler())
if settings.utils.log.file.enable:
    root.addHandler(TimedRotatingFileHandler(settings.project.name))
    root.addHandler(TimedRotatingFileHandler(settings.project.name + '.error', logging.ERROR))

critical = root.critical
error = root.error
exception = root.exception
warning = root.warning
info = root.info
debug = root.debug
log = root.log


def choose(name):
    return logging.getLogger(name=settings.project.name + '.' + name)
