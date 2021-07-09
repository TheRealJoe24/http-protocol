import socket
import sys, signal
import time

class HTTPServer:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self, port=5000):
        self.sock.bind(('127.0.0.1', port))
        self.sock.listen(5)

        signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))
        self._run()

    def _serve(self, client, addr):
        pass

    def _run(self):
        while True:
            time.sleep(1)

            client, addr = self.sock.accept()
            self._serve(client, addr)
