import socket

def main():
    try:
        my_socket = socket.socket()
        what_to_send = input("what would you like to send to the server: ")
        my_socket.connect(("127.0.0.1", 8820))
        my_socket.send(what_to_send.encode())
        data = my_socket.recv(1024).decode()
        print(data)
        
    except ConnectionRefusedError:
        print("Error receiving data back")
    finally:
        my_socket.close()

if __name__ == "__main__":
    main()