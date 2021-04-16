import socket
import ssl
from threading import Thread

class readSSLStream(Thread):
    def __init__(self,server,url,oncallback=None , header=None):
        Thread.__init__(self)
        self.server = server
        self.url = url
        self.oncallback = oncallback
        self.header = header
        self.context = ssl.create_default_context()

    def run(self):
        context = ssl.create_default_context()
        with socket.create_connection((self.server, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=self.server) as ssock:
                mhead = 'GET {0} HTTP/1.1\r\n'.format(self.url)
                mhead = mhead + 'Host: {0}\r\n'.format(self.server)
                #mhead = mhead + 'Host: {0}\r\n'.format(self.server)
                if self.header is not None:
                    mhead = mhead + self.header + '\r\n'
                mhead = mhead + '\r\n\r\n'
                ssock.sendall(mhead.encode('utf-8'))
                buff = ssock.recv(2096000)
                if self.oncallback is not None:
                    self.oncallback(buff)
                print('===END===')


