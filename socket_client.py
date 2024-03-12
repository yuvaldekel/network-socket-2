import socket
import protocol

IMAGE = r"C:\Users\yonat\Documents\Yuval\devops\networking\network-socket-2\screen_client.jpg"

def handle_respond(my_socket, respond, cmd):
    #if the command is send_photo, first checks if the server succeed to read the image
    #if it did, read from the socket the image by its size (the main function read the size) and saves it 
    if cmd.upper() == "SEND_PHOTO":
        if "Error" in str(respond):
            print(respond)
        else:
            image_bytes = bytes(my_socket.recv(int(respond)))
            image_file = open(IMAGE, 'wb')
            image_file.write(bytes(image_bytes))
            image_file.close()
    #for all other commands if the server sent a respond print it      
    elif respond != "":
        print(respond)

def main():
    print('Welcome to remote command line interface. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_PHOTO\nDIR\nDELETE\nCOPY\nEXECUTE\nDATE\nEXIT')

    try:
        #create and connect the client to the server
        my_socket = socket.socket()
        my_socket.connect(("127.0.0.1", 8820))
         
        while True:
            #get the command, format it by the protocol standard and send it
            cmd = input("Write your command: ")
            cmd_msg = protocol.create_msg(cmd)
            my_socket.send(cmd_msg)  

            #get the respond, format it if it is okay pass it to the handler
            #if not checks if the connection was closed, if it was, close the client
            is_okay, respond = protocol.get_msg(my_socket)
            if is_okay:
                handle_respond(my_socket, respond, cmd)
            elif respond == "":
                break
            else: 
                print(respond)

    except Exception as e:
        print("Error: {}".format(e))     
    finally:
        my_socket.close()

if __name__ == "__main__":
    main()