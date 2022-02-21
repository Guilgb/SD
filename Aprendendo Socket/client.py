import socket

HOST = "localhost"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))  # 127.0.0.1

file = open("email.png", "rb")
image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)
    file.close()
    client.close()

print("Mensagem ecoada: ", image_data.decode())
