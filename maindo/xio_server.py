import socketserver
import threading

def data_deal(func): # 要接受参数就要改成三层装饰器
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):
    @data_deal
    def handle(self):
        data = str(self.request.recv(1024), 'utf-8')
        print(data)
        if data == '1':
            pass
        elif data == '2':
            pass
        elif data == '3':
            pass
        elif data == '4':
            pass
        elif data == '5':
            pass
        elif data == '0':
            pass


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Server():
    HOST = 'localhost'
    PORT = 8081
    def __init__(self):
        #self.server_class = ThreadedTCPRequestHandler
        self.server = ThreadedTCPServer((self.HOST, self.PORT), ThreadedTCPRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

if __name__ == "__main__":
    s = Server()
    s
