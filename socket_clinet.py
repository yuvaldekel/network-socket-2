import socket

def main():
    with socket.socket() as my_socket:
        my_socket.connect(("127.0.0.1", 8820))
        my_socket.send("Omer".encode())
        data = my_socket.recv(1024).decode()
        print(data)


if __name__ == "__main__":
    main()