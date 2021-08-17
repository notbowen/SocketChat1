#Client script for chat
#socket ip -> input
#socket port = 6942

import socket
import sys
import threading
import atexit

ip = input("IP pls: ")
port = 6942

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except socket.error as e:
    print("Error while creating socket.\nDebug log:", e)
    sys.exit()

s.connect((ip, port))
print("Connected to %s:%s" %(ip, port))
username = input("\nUsername: ")
print("\nType a message and press enter to send :)\n")

def sendMsg():
    while True:
        msg = input("")
        while msg == "":
            msg = input("")
        s.send((username + ": " + msg).encode())

def exit_handler():
    s.close()


msgThread = threading.Thread(target=sendMsg)
msgThread.daemon = True
msgThread.start()
atexit.register(exit_handler)
while True:
    rmsg = s.recv(1024)
    if not rmsg: break
    print(rmsg.decode())
