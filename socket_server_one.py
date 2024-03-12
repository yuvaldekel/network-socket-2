import socket
import protocol

MY_PORT = 8821
HIS_PORT = 8820

def main():   
    while True:
        #as server
        #create server and accept connection
        a_socket = socket.socket()
        a_socket.bind(('0.0.0.0', MY_PORT))
        a_socket.listen()
        print(f"Side A listening  port {MY_PORT}")
        (b_socket, b_address) = a_socket.accept()
        print("Side B is connected")

        #get massage process it 
        is_okay, massage = protocol.get_msg(b_socket)
        if is_okay:
            if massage.lower() == "exit":
                b_socket.close()
                a_socket.close()
                print("Side B disconnected")
                break
            print(f"Side B sent {massage}")

        #send back respond
        b_socket.send(protocol.create_msg(massage))
        print(f"Side A send back {massage}")
        b_socket.close()
        a_socket.close()
        print("Side B disconnected")
        
        #as client
        a_socket = socket.socket()
        what_to_send = input("what would you like to send to the server: ")

        #connect
        a_socket.connect(("127.0.0.1", HIS_PORT))
        print(f"side A connected to port {HIS_PORT}")
        
        #send massage
        a_socket.send(protocol.create_msg(what_to_send))
        print(f"Side A sent {what_to_send}")

        #get respond and process it
        is_okay, respond = protocol.get_msg(a_socket)
        if is_okay:
            print(f"Side B sent {respond}")
        elif respond == "":
            break
        print(f"Side A disconnected")
        a_socket.close()
        
if __name__ == "__main__":
    main()