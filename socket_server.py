import socket
import datetime
import random

NAME = "SuperServer"

def main():
    with socket.socket() as server_socket:
        server_socket.bind(('0.0.0.0', 8820))
        server_socket.listen()
        print("Server is up and running")

        (client_socket, client_address) = server_socket.accept()
        print("Client connected his address {}".format(client_address))
        while True:
            length_message = client_socket.recv(2).decode()
            data = client_socket.recv(length_message).decode()
            print("Client sent: {}".format(data))
            if data == 'DATE':
                date = str(datetime.datetime.now())
                length = str(len(date))
                zfill_length = length.zfill(2)
                message = zfill_length + date
                client_socket.send(message.encode())
            elif data == 'WHORU':
                length = str(len(NAME))
                zfill_length = length.zfill(2)
                message = zfill_length + NAME
                client_socket.send(message.encode())
            elif data == 'RAND':
                number = str(random.randint(1,10))
                length = str(len(number))
                zfill_length = length.zfill(2)
                message = zfill_length + number
                client_socket.send(message.encode())
            elif data == 'EXIT':
                client_socket.close()
                break
            else:
                client_socket.send("Problem with the request".encode())

if __name__ == "__main__":
    main()