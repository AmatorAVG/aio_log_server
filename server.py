import socket


def http_response(msg):
    return "HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}".format(
        len(msg), msg
    )


# HOST = '127.0.0.1'
# HOST = 'localhost'
# HOST = '192.168.43.95'
HOST = "172.16.10.10"
PORT = 9092

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Соединение установлено с", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode()
            print("Полученные данные:", msg)
            response = http_response(msg)
            conn.sendall(response.encode())
