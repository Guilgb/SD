import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 8080))
print("Conectado...")

name_file = str(input('Digite o nome do Arquivo: '))

client.send(name_file.encode())

with open(name_file, 'wb') as file:
    while True:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{name_file} recebido!\n')
