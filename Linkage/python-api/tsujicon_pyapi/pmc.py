import socket

class pmc:

    def __init__(self):
        socket.setdefaulttimeout(30) #TODO: make timeout to variable
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip, port):
        self._socket.connect((ip,  port))
        return 0

    def ver(self):
        return self.send_recv(b'VER?')

    def send(self, data):
        if isinstance(data,(bytes,)):
            self._socket.send(data + b'\r\n')
        else:
            self._socket.send(bytes(data, "utf-8") + b'\r\n')

    def send_recv(self, data):
        if isinstance(data,(bytes,)):
            self._socket.send(data + b'\r\n')
        else:
            self._socket.send(bytes(data, "utf-8") + b'\r\n')

        r = self._socket.recv(1024)
        return r.decode('utf8')

    def estop(self, ch):
        self.send('ESTP' + ch)

    def get_pos16(self):
        p = self.send_recv(b'PS_16?')
        return [int(x) for x in p.split('/')]

    def get_pos(self,ch):
        p = self.send_recv("PS?"+ch)
        return int(p)

    def set_pos(self,ch,pos):
        #PS<ch><pos>
        self.send("PS" + ch + str(pos))

    def get_status(self):
        p = self.send_recv(b'STS_16?')
        return p

    def __exit__(self, exc_type, exc_value, traceback):
        self._socket.close()
        self.exc_type = exc_type
        self.exc_value = exc_value
        self.traceback = traceback
