import json

class HTTPEntity:
    '''
    A base class representing an http entity
    '''

    def __init__(self, mime: str) -> None:
        '''
        Create an entity with a mime type
        '''
        self.mime = mime

    def encode_string(self, s: str) -> bytes:
        '''
        Encode a string to a bytes object
        '''
        return s.encode('utf-8')

    def encode(self) -> bytes:
        '''
        Encode internal data into a bytes object
        '''
        return b''

class HTTPJsonEntity(HTTPEntity):
    '''
    A class representing an http entity with the application/json mime type
    '''

    def __init__(self, obj: dict):
        '''
        Create a json entity with a dict
        '''
        super().__init__('application/json')
        self.obj = obj

    def encode(self) -> bytes:
        return self.encode_string(json.dumps(self.obj))
