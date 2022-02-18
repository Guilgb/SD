import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen()

print("Aguardando conecxão...")

connect, address = server.accept()
print(f"Conectado em: {address}")

name_file = connect.recv(2048).decode()

with open(name_file, 'rb') as file:
    for data in file.readlines():
        connect.send(data)
        if not data:
            print("Fechando a conecxão")
            connect.close()
            break
    print("Arquivo Enviado!!")
