import socket

def main():
    with socket.socket() as server_socket:
        server_socket.bind(('0.0.0.0', 8820))
        server_socket.listen()
        print("Server is up and running")

        (client_socket, client_address) = server_socket.accept()
        print("Client connected")

        data = client_socket.recv(1024).decode()
        print("Client sent: " + data)

        reply = 'Hello ' + data
        client_socket.send(reply.encode())

        client_socket.close()

if __name__ == "__main__":
    main()