import atexit
import datetime
import os
import os.path
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists('./vendor'):
    sys.path.insert(0, os.path.abspath('./vendor'))

import src
import src.utils.log
import src.utils.settings

try:
    import setproctitle
except ImportError:
    pass
else:
    project = src.utils.settings.project
    setproctitle.setproctitle('python' + ':' + project.name + ':' + project.version)


def echo_duration():
    origin = datetime.datetime.utcnow()

    def wrapper():
        duration = datetime.datetime.utcnow() - origin
        days = duration.days
        hours = int(duration.seconds / 3600)
        minutes = int((duration.seconds - 3600 * hours) / 60)
        seconds = int(duration.seconds - 3600 * hours - minutes * 60)
        msg = 'Shut Down.The program takes {days}D {hours}H {minutes}M {seconds}S'
        src.utils.log.info(msg.format(days=days, hours=hours, minutes=minutes, seconds=seconds))

    return wrapper

atexit.register(echo_duration())

if __name__ == '__main__':
    try:
        sys.exit(src.main())
    except KeyboardInterrupt:
        sys.exit()
