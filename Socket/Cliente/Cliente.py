from http import client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(('localhost', 7777))
print("Conectado!\n")

namefile = str(input('arquivo'))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000)
        if not data:
            break       
        file.write(data)

print("Arquivo recebido")