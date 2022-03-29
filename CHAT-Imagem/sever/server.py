import socket
from _thread import *
from collections import defaultdict as df
import time


class Server:
    def __init__(self):
        self.rooms = df(list)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def accept_connections(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.server.bind((self.ip_address, int(self.port)))
        self.server.listen(100)
        print("SERVER CONNECTED)")

        while True:
            connection, address = self.server.accept()
            print(str(address[0]) + ":" + str(address[1]) + " conectado")

            start_new_thread(self.clientThread, (connection,))

        self.server.close()

    def clientThread(self, connection):
        user = connection.recv(1024).decode().replace("Usuario ", "")
        room = connection.recv(1024).decode().replace("Se juntou ", "")

        if room not in self.rooms:
            connection.send("chat criado".encode())
        else:
            connection.send("Bem vindo".encode())

        self.rooms[room].append(connection)

        while True:
            try:
                message = connection.recv(1024)
                print(str(message.decode()))
                if message:
                    if str(message.decode()) == "FILE":
                        self.broadcastFile(connection, room, user)

                    else:
                        messageToSend = "o " + \
                            str(user) + " disse: " + message.decode()
                        self.broadcast(messageToSend, connection, room)

                else:
                    self.remove(connection, room)
            except Exception as e:
                print(repr(e))
                print("Disconected")
                break

    def broadcastFile(self, connection, room_id, user_id):
        fileName = connection.recv(1024).decode()
        lenOfFile = connection.recv(1024).decode()
        for client in self.rooms[room_id]:
            if client != connection:
                try:
                    client.send("FILE".encode())
                    time.sleep(0.1)
                    client.send(fileName.encode())
                    time.sleep(0.1)
                    client.send(lenOfFile.encode())
                    time.sleep(0.1)
                    client.send(user_id.encode())

                except:
                    client.close()
                    self.remove(client, room_id)

        total = 0
        print(fileName, lenOfFile)
        while str(total) != lenOfFile:
            data = connection.recv(1024)
            total = total + len(data)
            for client in self.rooms[room_id]:
                if client != connection:
                    try:
                        client.send(data)
                        # time.sleep(0.1)
                    except:
                        client.close()
                        self.remove(client, room_id)
        print("Enviado")

    def broadcast(self, messageToSend, connection, room):
        for client in self.rooms[room]:
            if client != connection:
                try:
                    client.send(messageToSend.encode())
                except:
                    client.close()
                    self.remove(client, room)

    def remove(self, connection, room_id):
        if connection in self.rooms[room_id]:
            self.rooms[room_id].remove(connection)


if __name__ == "__main__":
    ipAddress = "localhost"
    port = 12345

    s = Server()
    s.accept_connections(ipAddress, port)
