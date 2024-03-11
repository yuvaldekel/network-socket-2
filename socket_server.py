import socket
import datetime
import random
import protocol

NAME = "SuperServer"

def main():
    with socket.socket() as server_socket:
        server_socket.bind(('0.0.0.0', 8820))
        server_socket.listen()
        print("Server is up and running")

        (client_socket, client_address) = server_socket.accept()
        print("Client connected his address {}".format(client_address))
        
        while True:
            is_okay, data = protocol.get_msg(client_socket)
            if not is_okay:
                message = protocol.create_msg("Wrong Protocol")
                client_socket.send(message.encode())
            
            elif not protocol.check_cmd(data):
                message = protocol.create_msg("Wrong Protocol")
                client_socket.send(message.encode())
            
            elif data == 'DATE':
                date = str(datetime.datetime.now())
                message = protocol.create_msg(date)
                client_socket.send(message.encode())            
            elif data == 'WHORU':
                message = protocol.create_msg(NAME)
                client_socket.send(message.encode())
            elif data == 'RAND':
                number = str(random.randint(1,10))
                message = protocol.create_msg(number)
                client_socket.send(message.encode())
            elif data == 'EXIT':
                client_socket.close()
                break

if __name__ == "__main__":
    main()