from email.headerregistry import Address
from http import server
from multiprocessing import connection
import socket


# AF_INIT == IPV4/Dominio SOCKET_STREAM = Protocolo TPC/IP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Onde o servidor vai ser alocado. No caso no localhost na porta 7777
server.bind(('localhost', 7777))

# Quantidade de conecções que o servidor vai receber
server.listen(5)

# conecção com o cliente e o seu endereço
connection, address = server.accept()

# Recebendo o nome do arquivo em bytes e convertendo pra string
namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print("Arquivo enviado")
