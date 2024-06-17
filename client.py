import socket

sock = socket.socket()
sock.setblocking(1)
# sock.connect(("172.16.10.10", 9090))
sock.connect(("62.173.139.168", 9090))

msg = "Привет!"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
