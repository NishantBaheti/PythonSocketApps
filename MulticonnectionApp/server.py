import socket
import types
import selectors

HOST = '0.0.0.0'
PORT = 12345

sel = selectors.DefaultSelector()


localSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localSocket.bind((HOST, PORT))
localSocket.listen()


print(f"Listening on Host {HOST} and Port {PORT}")

# socket on non-blocking mode
# Calls made to server socket will no longer block
localSocket.setblocking(False)


sel.register(localSocket, selectors.EVENT_READ, data=None)


def acceptWrapper(sock):
    conn, addr = sock.accept()

    print("Accepted connection from :", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def serviceConnection(key, mask):
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recvData = sock.recv(1024)
        if recvData:
            data.outb += recvData
        else:
            print("closing connection to ", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing : ", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            # client socket is not accepted
            acceptWrapper(key.fileobj)
        else:
            # client socket is already accepted
            serviceConnection(key, mask)
