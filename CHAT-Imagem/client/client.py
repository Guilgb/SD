import socket
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
import time
import threading
import os


# -------------------CORES -----------------
backgroundcolor = "#171c28"
textcolor = "#7589aa"
backgroudbox = "#1f2e47"
backgroundaux = "#4362a8"
foreground = "#ffffff"
fontes = "rainyhearts 10"


class GUI:

    def __init__(self, ipAddress, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((ipAddress, port))

        self.janela = tk.Tk()
        self.janela.withdraw()

        self.login = tk.Toplevel()

        self.login.title("SDIS")
        self.login.resizable(False, False)
        self.login.configure(width=400, height=350)
        self.login.config(bg=backgroundcolor)

        self.pls = tk.Label(self.login,
                            text='TRABALHO DE SISTEMAS DISTRIBUIDOS', justify=tk.LEFT, bg=backgroundcolor, fg=textcolor, font="rainyhearts 12")

        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.userLabelName = tk.Label(
            self.login, text="nome: ", bg=backgroundcolor, fg=textcolor, font="rainyhearts 20")
        self.userLabelName.place(relheight=0.2, relx=0.1, rely=0.25)

        self.userEntryName = tk.Entry(
            self.login, fg=textcolor, font="rainyhearts 20")

        self.userEntryName.place(
            relwidth=0.4, relheight=0.1, relx=0.35, rely=0.30)

        self.userEntryName.focus()

        self.roomLabelName = tk.Label(self.login, text="sala: ",
                                      fg=textcolor,
                                      bg=backgroundcolor,
                                      font="rainyhearts 20")
        self.roomLabelName.place(relheight=0.2, relx=0.1, rely=0.40)

        self.roomEntryName = tk.Entry(self.login,
                                      fg=textcolor,
                                      font="rainyhearts 20",
                                      show="*")
        self.roomEntryName.place(
            relwidth=0.4, relheight=0.1, relx=0.35, rely=0.45)

        self.go = tk.Button(self.login, text="Entrar no Chat", bd=0, fg=backgroudbox, bg=textcolor,
                            font="rainyhearts 10", command=lambda: self.goAhead(self.userEntryName.get(), self.roomEntryName.get()))

        self.go.place(relx=0.35, rely=0.62, width=160, height=34)

        self.janela.mainloop()

    def goAhead(self, username, room=0):
        self.name = username
        self.server.send(str.encode(username))
        time.sleep(0.1)
        self.server.send(str.encode(room))

        self.login.destroy()
        self.layout()

        rcv = threading.Thread(target=self.receive)
        rcv.start()

    def layout(self):
        self.janela.deiconify()
        self.janela.title("CHAT")
        self.janela.resizable(width=False, height=False)
        self.janela.configure(width=470, height=550, bg=backgroundcolor)
        self.chatBoxHead = tk.Label(self.janela, bg=backgroudbox, fg=textcolor, text=self.name,
                                    font="rainyhearts 22", pady=5)

        self.chatBoxHead.place(relwidth=1)

        self.line = tk.Label(self.janela, width=450,
                             bg=backgroundcolor)

        self.line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.textCons = tk.Text(self.janela, width=20, height=2,
                                bg=backgroundcolor, fg=textcolor, font="rainyhearts 20", padx=5, pady=5)

        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)

        self.labelBottom = tk.Label(self.janela, bg=backgroudbox, height=80)

        self.labelBottom.place(relwidth=1,
                               rely=0.8)

        self.entryMsg = tk.Entry(self.labelBottom,
                                 bg=backgroundcolor, fg=textcolor, font="rainyhearts 13")
        self.entryMsg.place(relwidth=0.74, relheight=0.03,
                            rely=0.008, relx=0.011)
        self.entryMsg.focus()

        self.buttonMsg = tk.Button(self.labelBottom,
                                   text="SEND", font="rainyhearts 20", fg=textcolor, width=20, bg=backgroundcolor, bd=0,
                                   command=lambda: self.sendButton(self.entryMsg.get()))
        self.buttonMsg.place(relx=0.77, rely=0.008,
                             relheight=0.03, relwidth=0.22)

        self.labelFile = tk.Label(
            self.janela, bg=backgroudbox, height=70)

        self.labelFile.place(relwidth=1,
                             rely=0.9)

        self.fileLocation = tk.Label(self.labelFile, text="ver arquivo", bg=backgroundcolor, fg=textcolor, bd=0,
                                     font="rainyhearts 13")
        self.fileLocation.place(
            relwidth=0.65, relheight=0.03, rely=0.008, relx=0.011)

        self.browse = tk.Button(self.labelFile, text="Search", font="rainyhearts 13", width=13, bd=0,
                                bg=backgroundcolor, fg=textcolor,
                                command=self.browseFile)
        self.browse.place(relx=0.67, rely=0.008, relheight=0.03, relwidth=0.15)

        self.sengFileBtn = tk.Button(self.labelFile,
                                     text="enviar", font="rainyhearts 10", width=13, bg=backgroundcolor, bd=0, fg=textcolor,
                                     command=self.sendFile)
        self.sengFileBtn.place(relx=0.84, rely=0.008,
                               relheight=0.03, relwidth=0.15)

        self.textCons.config(cursor="arrow",)
        scrollbar = tk.Scrollbar(self.textCons)
        scrollbar.place(relheight=1,
                        relx=0.974)

        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=tk.DISABLED)

    def browseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="selecionar uma img",
                                                   filetypes=(("imagem receba obrigado meu deus",
                                                               "*.jpg*"),
                                                              ("msg",
                                                               "*.*")))
        self.fileLocation.configure(text="imagem aberta: " + self.filename)

    def sendFile(self):
        self.server.send("FILE".encode())
        time.sleep(0.1)
        self.server.send(
            str("client_" + os.path.basename(self.filename)).encode())
        time.sleep(0.1)
        self.server.send(str(os.path.getsize(self.filename)).encode())
        time.sleep(0.1)

        file = open(self.filename, "rb")
        data = file.read(1024)
        while data:
            self.server.send(data)
            data = file.read(1024)
        self.textCons.config(state=tk.DISABLED)
        self.textCons.config(state=tk.NORMAL)
        self.textCons.insert(tk.END, "arquivo: "
                                     + str(os.path.basename(self.filename))
                                     + "\n")
        self.textCons.config(state=tk.DISABLED)
        self.textCons.see(tk.END)

    def sendButton(self, msg):
        self.textCons.config(state=tk.DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, tk.END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

    def receive(self):
        while True:
            try:
                message = self.server.recv(1024).decode()

                if str(message) == "FILE":
                    file_name = self.server.recv(1024).decode()
                    lenOfFile = self.server.recv(1024).decode()
                    send_user = self.server.recv(1024).decode()

                    if os.path.exists(file_name):
                        os.remove(file_name)

                    total = 0
                    with open(file_name, 'wb') as file:
                        while str(total) != lenOfFile:
                            data = self.server.recv(1024)
                            total = total + len(data)
                            file.write(data)

                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state=tk.NORMAL)
                    self.textCons.insert(
                        tk.END, "😍 o " + str(send_user) + " 😍 enviou: " + file_name + " \nobrigado meuDEUs\n")
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.see(tk.END)

                else:
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state=tk.NORMAL)
                    self.textCons.insert(tk.END,
                                         message+"\n\n")

                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.see(tk.END)

            except:
                print("ERROR")
                self.server.close()
                break

    def sendMessage(self):
        self.textCons.config(state=tk.DISABLED)
        while True:
            self.server.send(self.msg.encode())
            self.textCons.config(state=tk.NORMAL)
            self.textCons.insert(tk.END,
                                 "you send: " + self.msg + "\n")

            self.textCons.config(state=tk.DISABLED)
            self.textCons.see(tk.END)
            break


if __name__ == "__main__":
    ip_address = "localhost"
    port = 12345
    g = GUI(ip_address, port)
