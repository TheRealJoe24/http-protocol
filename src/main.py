# import socket

# PORT = 5000

# def main():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     sock.bind(('127.0.0.1', PORT))
#     sock.listen(5)
    
#     while True:
#         client, client_addr = sock.accept()
#         print(client.recv(4096))
#         client.send(b'HTTP/1.1 200 OK\r\n\r\nasdf')
#         client.close()

# if __name__ == '__main__':
#     main()

from toy_http import server

app = server.HTTPServer()
app.listen(5000)
