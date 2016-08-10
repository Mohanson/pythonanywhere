import src.service.apihandler
import src.service.routeset


@src.service.routeset.bind('/api/v1/routes')
class Service(src.service.apihandler.APIHandler):

    def get(self):
        import src.service.routeset
        routes = []
        for route, _ in src.service.routeset.routeset:
            routes.append(route)
        routes.sort()
        self.swrite({
            'routes': routes
        })
