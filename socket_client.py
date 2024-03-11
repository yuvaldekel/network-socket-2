import socket
import protocol

def main():
    try:
        my_socket = socket.socket()
        my_socket.connect(("127.0.0.1", 8820))
         
        while True:
            what_to_send = 0
            message = ''
            what_to_send = int(input("what would you like to send to the server:\npress one for DATE,\npress two for WHORU,\npress two for RAND,\npress four for EXIT. "))
            
            if what_to_send == 1:
                message = "DATE"
            elif what_to_send == 2:
                message = "WHORU"
            elif what_to_send == 3:
                message = "RAND"
            elif what_to_send == 4:
                message = "EXIT"

            message = protocol.create_msg(message)
            my_socket.send(message.encode())
            
            is_okay, data = protocol.get_msg(my_socket)
            if is_okay:
                if data == '':
                    print("You stopped the connection")
                    break
                print("server sent {}".format(data))
            else:
                data = my_socket.recv(1024).decode()

    except Exception as e:
        print("Error: {}".format(e))     
    finally:
        my_socket.close()

if __name__ == "__main__":
    main()