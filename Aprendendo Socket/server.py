import socket

HOST = "localhost"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Aguardando Conecxão")
client_socket, client_address = server.accept()


file = open('email.png', "wb")
image_chunk = client_socket.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)

file.close()
client_socket.close()
