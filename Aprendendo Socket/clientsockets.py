import socket

HOST = "127.0.0.1"
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
server.sendall(str(input("Digite sua Mensagem:\n")).encode())
data = server.recv(2048)

print("Mensagem ecoada: ", data.decode())
