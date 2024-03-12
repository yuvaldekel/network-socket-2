import socket
import protocol

IMAGE = r"C:\Users\yonat\Documents\Yuval\devops\networking\network-socket-2\screen_client.jpg"

def handle_respond(my_socket, respond, cmd):
    if cmd.upper() == "SEND_PHOTO":
        if "Error" in str(respond):
            print(respond)
        else:
            image_bytes = bytes(my_socket.recv(int(respond)))
            image_file = open(IMAGE, 'wb')
            image_file.write(bytes(image_bytes))
            image_file.close()
            
    elif respond != "":
        print(respond)

def main():
    print('Welcome to remote command line interface. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_PHOTO\nDIR\nDELETE\nCOPY\nEXECUTE\nDATE\nEXIT')

    try:
        my_socket = socket.socket()
        my_socket.connect(("127.0.0.1", 8820))
         
        while True:
            cmd = input("Write your command: ")
            cmd_msg = protocol.create_msg(cmd)
            my_socket.send(cmd_msg)          
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