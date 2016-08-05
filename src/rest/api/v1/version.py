import src.rest.apihandler
import src.rest.routeset
import src.utils.settings as settings


@src.rest.routeset.bind('/api/v1/version')
class Service(src.rest.apihandler.APIHandler):

    def get(self):
        self.swrite({
            'name': settings.project.name,
            'version': settings.project.version,
            'author': settings.project.author,
            'url': settings.project.url,
        })
