import datetime
import json

import src.record
import src.service.apihandler
import src.service.routeset


@src.service.routeset.bind('/api/v1/echo')
class Echo(src.service.apihandler.APIHandler):
    messages = src.record.get('messages', [])

    def get(self):
        self.swrite({
            'messages': self.messages
        })

    def post(self):
        if len(self.messages) > 30:
            self.messages.pop()

        body = self.request.body.decode()
        content_type = self.request.headers.get('Content-Type')
        try:
            body = json.loads(body)
            assert isinstance(body, dict)
            content_type = 'application/json'
        except Exception:
            body = body

        message = {
            'time': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'ip': self.request.remote_ip,
            'body': body,
            'content-type': content_type,
        }
        self.messages.insert(0, message)
        src.record.set('messages', self.messages)
        self.swrite()

    def delete(self):
        self.messages.clear()
        src.record.set('messages', [])
        self.swrite()
