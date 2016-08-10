import src.service.apihandler
import src.service.routeset


@src.service.routeset.bind('/api/v1/version')
class Service(src.service.apihandler.APIHandler):

    def get(self):
        self.swrite({
            'name': src.settings.project.name,
            'version': src.settings.project.version,
            'author': src.settings.project.author,
            'url': src.settings.project.url,
        })
