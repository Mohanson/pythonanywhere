class RouteSet(list):

    def __init__(self, *args, **kwargs):
        super(RouteSet, self).__init__(*args, **kwargs)

    def bind(self, route):
        assert route not in map(lambda _: _[0], self), 'Routing repeated binding "%s"' % route

        def wrapper(klass):
            self.append((route, klass))
            return klass

        return wrapper


routeset = RouteSet()


def bind(route):
    return routeset.bind(route)
