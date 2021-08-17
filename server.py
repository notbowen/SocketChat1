#Server Script for chat thingy
#socket ip = 0.0.0.0
#socket port = 6942

import socket
import os
import threading

ip = "0.0.0.0"
port = 6942

connections = []

try:
    s = socket.socket()
    print("Socket created")
except socket.error as e:
    print("Error while creating socket.\nDebug log:", e)
    os._exit()

s.bind((ip, port))
print("Binded to {0}:{1}".format(socket.gethostbyname(socket.gethostname()), port))

s.listen(100)
print("Server is ready.")

def cThread(c, addr):
    while True:
        try:
            msg = c.recv(1024)
            for i in connections:
                if i != c:
                    connections.remove(i)
                    return
                i.send(msg)
        except ConnectionResetError:
            connections.remove(c)
            print(addr + " disconnected")
            return

while True:
    c, addr = s.accept()
    connections.append(c)
    print("Connection from", addr)
    thread = threading.Thread(target=cThread, args=(c, addr))
    thread.daemon = True
    thread.start()
