import socket


HOST = 'localhost'
PORT = 5643
ADDR = (HOST, PORT)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print('[CONNECTED...] Client connected to server: ', ADDR)

    connected = True
    while connected:

        msg = input("Digite sua mensagem: ")

        client.send(msg.encode('utf-8'))

        if msg == 'sair':
            connected = False
        else:
            msg = client.recv(1024).decode('utf-8')
            print(f"[SERVER] {msg}")


if __name__ == '__main__':
    main()
