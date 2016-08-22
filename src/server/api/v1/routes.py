import src.server.apihandler
import src.server.routeset


@src.server.routeset.bind('/api/v1/routes')
class Service(src.server.apihandler.APIHandler):

    def get(self):
        import src.server.routeset
        routes = []
        for route, _ in src.server.routeset.routeset:
            routes.append(route)
        routes.sort()
        self.swrite({
            'routes': routes
        })
