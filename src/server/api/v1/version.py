import src.server.apihandler
import src.server.routeset


@src.server.routeset.bind('/api/v1/version')
class Service(src.server.apihandler.APIHandler):

    def get(self):
        self.swrite({
            'name': src.settings.project.name,
            'version': src.settings.project.version,
            'author': src.settings.project.author,
            'url': src.settings.project.url,
        })
