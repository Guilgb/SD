import socket
import threading

HOST = 'localhost'
PORT = 5643
ADDR = (HOST, PORT)


def connect_clients(conn, addr):

    print(f"[NEW CONNECT]{addr} connected")

    connected = True

    while connected:
        msg = conn.recv(1024).decode('utf-8')
        if msg == 'sair':
            connected = False
        else:
            print(f"[{addr}] {msg}")
            msg = f"Msg received: {msg}"
            conn.send(msg.encode('utf-8'))
    conn.close()


def main():

    print('SART...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print('[LISTEN...] Server: ', ADDR)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=connect_clients, args=(
            conn, addr))
        thread.start()
        print(f'[CONNECTION ACCEPT]: {threading.activeCount() -1}')


if __name__ == '__main__':
    main()
