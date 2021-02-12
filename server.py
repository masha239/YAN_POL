import socket
import re

my_socket = socket.socket()
my_socket.bind(('', 8080))
my_socket.listen(100)

while True:
    conn, addr = my_socket.accept()
    data = ''

    while True:
        part_data = conn.recv(1024).decode()
        if not part_data:
            break
        data += part_data

    data = data.rstrip()

    result = re.fullmatch(r'GET /greet/[a-zA-Z]+', data)
    if result:
        name = data.split('/')[-1]
        named_answer = '200 OK\nHello ' + name
        conn.send(named_answer.encode())
    else:
        conn.send('400 Bad Request'.encode())
    
    conn.close()