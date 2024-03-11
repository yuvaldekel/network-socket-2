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
            data = client_socket.recv(5).decode()
            print("Client sent: {}".format(data))
            if data == 'DATE':
                date = str(datetime.datetime.now())
                client_socket.send(date.encode())
            elif data == 'WHORU':
                client_socket.send(NAME.encode())
            elif data == 'RAND':
                number = str(random.randint(1,10))
                client_socket.send(number.encode())
            elif data == 'EXIT':
                client_socket.close()
                break
            else:
                client_socket.send("Problem with the request".encode())

if __name__ == "__main__":
    main()