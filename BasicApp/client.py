import socket
import time

HOST = '0.0.0.0'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketObj:
    socketObj.connect((HOST, PORT))
    while True:
        socketObj.sendall(b"Hello ")

        data = socketObj.recv(1024)
        print('Received', repr(data))
        time.sleep(5)
