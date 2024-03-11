import socket

def main():
    try:
        my_socket = socket.socket()
        my_socket.connect(("127.0.0.1", 8820)) 
        while True:
            what_to_send_number = 0
            what_to_send = None
            what_to_send_number = int(input("what would you like to send to the server:\npress one for DATE,\npress two for WHORU,\npress two for RAND,\npress four for EXIT. "))
            if what_to_send_number == 1:
                what_to_send = "DATE"
            elif what_to_send_number == 2:
                what_to_send = "WHORU"
            elif what_to_send_number == 3:
                what_to_send = "RAND"
            elif what_to_send_number == 4:
                what_to_send = "EXIT"
            if what_to_send != None:
                my_socket.send(what_to_send.encode())
                data = my_socket.recv(1024).decode()
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