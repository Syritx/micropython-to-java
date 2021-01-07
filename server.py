import socket
import threading as t
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 5000))
print(socket.gethostname())
server.listen(5)

def thread(clt, addr):
    connected = True

    while connected:

        message_len = clt.recv(1024).decode('utf-8')
        if message_len != None:

            message = None
            try:
                message_len = int(message_len)
                message = clt.recv(message_len).decode('utf-8')

            except:
                message = message_len


            if (message == 'hello, button was pressed'):
                subprocess.call(['sh','./main.sh'])
            print(message)


while True:
    client_socket, addr = server.accept()
    print("connection")

    thr = t.Thread(target=thread, args=(client_socket, addr))
    thr.start()