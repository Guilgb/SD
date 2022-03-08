import socket
# import threading

PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
client, end = server.accept()

theand = False

while not theand:
    msg = client.recv(2048).decode(FORMAT)
    if msg == 'sair':
        theand = True
    else:
        print(msg)
    client.send(input('Mensagem: ').encode(FORMAT))

client.close()
server.close()
