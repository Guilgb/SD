from pydoc import cli
import socket
# import threading

PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

theand = False

print('Digite sair para sair do chat')

while not theand:
    client.send(input('Mensagem: ').encode(FORMAT))
    msg = client.recv(2048).decode(FORMAT)

    if msg == 'sair':
        theand = True
    else:
        print(msg)

client.close()
