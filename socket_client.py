import socket

def main():
    try:
        my_socket = socket.socket()
        my_socket.connect(("127.0.0.1", 8820)) 
        while True:
            what_to_send = 0
            message = None
            what_to_send = int(input("what would you like to send to the server:\npress one for DATE,\npress two for WHORU,\npress two for RAND,\npress four for EXIT. "))
            if what_to_send == 1:
                message = "DATE"
            elif what_to_send == 2:
                message = "WHORU"
            elif what_to_send == 3:
                message = "RAND"
            elif what_to_send == 4:
                message = "EXIT"
            if message != None:
                length = str(len(message))
                zfill_length = length.zfill(2)
                message = zfill_length + message
                my_socket.send(message.encode())
                length_message = my_socket.recv(2).decode()
                data = my_socket.recv(length_message).decode()
                if data == '':
                    #raise Exception("You exited")
                    print("You exited the connection")
                    break
                print("server sent {}".format(data))
    except Exception as e:
        print("Error: {}".format(e))     
    finally:
        my_socket.close()

if __name__ == "__main__":
    main()