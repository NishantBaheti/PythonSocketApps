import socket

# SOCK_STREAM for TCP
# SOCK_DGRAM for UDP

# AF_INET IPV4
# AF_INET6 IPV6

# Server methods
# socket(),bind(),listen(),accept()

HOST = '0.0.0.0'
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketObj:
    socketObj.bind((HOST, PORT))
    socketObj.listen()
    print(socketObj)

    conn, addr = socketObj.accept()
    with conn:
        print("Connected by :", addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)
