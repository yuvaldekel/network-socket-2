import socket
import protocol

MY_PORT = 8820
HIS_PORT = 8821

def main():
    while True:
        #as client
        b_socket = socket.socket()
        what_to_send = input("what would you like to send to the server: ")

        #connect
        b_socket.connect(("127.0.0.1", HIS_PORT))
        print(f"side B connected to port {HIS_PORT}")

        #send massage
        b_socket.send(protocol.create_msg(what_to_send))
        print(f"Side B sent {what_to_send}")

        #get respond and process it
        is_okay, respond = protocol.get_msg(b_socket)
        if is_okay:
            print(f"Side A sent {respond}")
        elif respond == "":
            break
        print(f"Side B disconnected")
        b_socket.close()

        #as server
        #create server and accept connection
        b_socket = socket.socket()
        b_socket.bind(('0.0.0.0', MY_PORT))
        b_socket.listen()
        print(f"Side B listening  port {MY_PORT}")
        (a_socket, a_address) = b_socket.accept()
        print("Side A is connected")

        #get massage process it 
        is_okay, massage = protocol.get_msg(a_socket)
        if is_okay:
            if massage.lower() == "exit":
                a_socket.close()
                b_socket.close()
                print("Side A disconnected")
                break
            print(f"Side A sent {massage}")

        #send back respond
        a_socket.send(protocol.create_msg(massage))
        print(f"Side B send back {massage}")
        a_socket.close()
        b_socket.close()
        print("Side A disconnected")
        


if __name__ == "__main__":
    main()