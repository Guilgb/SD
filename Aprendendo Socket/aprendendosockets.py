import socket

HOST = "localhost"
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print("Aguardando Conecxão")

connect, local = server.accept()
print(f"conectado em {local}")
while True:
    data = connect.recv(2048)
    if not data:
        print("Fechando a conecxão")
        connect.close()
        break
    connect.sendall(data)
