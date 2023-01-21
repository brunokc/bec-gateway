from .requesthandler import ConnexRequestHandler

class ConnexState:
    def __init__(self):
        self._status = { }
        self._idu_status = { }
        self._odu_status = { }
        self._handler = ConnexRequestHandler()

