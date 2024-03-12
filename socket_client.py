import socket
import protocol

IMAGE = r"C:\Users\yonat\Documents\Yuval\devops\networking\network-socket-2\screen_client.jpg"

def handle_respond(my_socket, data, cmd):
    if cmd.upper() == "SEND_PHOTO":
        image_bytes = bytes(my_socket.recv(int(data)))
        with open(IMAGE, 'wb') as image_file:
            image_file.write(bytes(image_bytes))
            
    if data != "":
        print(data)


def main():
    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_PHOTO\nDIR\nDELETE\nCOPY\nEXECUTE\nDATE\nEXIT')

    try:
        my_socket = socket.socket()
        my_socket.connect(("127.0.0.1", 8820))
         
        while True:
            cmd = input("Wrote your command: ")
            cmd_msg = protocol.create_msg(cmd)
            my_socket.send(cmd_msg)          
            is_okay, data = protocol.get_msg(my_socket)
            if is_okay:
                handle_respond(my_socket, data, cmd)
            elif data == "":
                break

    except Exception as e:
        print("Error: {}".format(e))     
    finally:
        my_socket.close()

if __name__ == "__main__":
    main()