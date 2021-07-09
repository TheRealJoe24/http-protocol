class HTTPRequest:
    '''
    A class containing http request data
    '''

    def __init__(self, server, method, headers, path, entity):
        self.server = server
        self.method = method
        self.headers = headers
        self.path = path
        self.entity = entity
