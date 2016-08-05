import src.rest.apihandler
import src.rest.routeset


@src.rest.routeset.bind('/api/v1/routes')
class Service(src.rest.apihandler.APIHandler):

    def get(self):
        import src.rest.routeset
        routes = []
        for route, _ in src.rest.routeset.routeset:
            routes.append(route)
        routes.sort()
        self.swrite({
            'routes': routes
        })
