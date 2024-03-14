import socket
import datetime
import protocol
import commands

NAME = "SuperServer"

def check_request(cmd):
    if protocol.check_cmd(cmd):
        params = cmd.split()
        command = params.pop(0).upper()
        return True, command, params
    return False, "", []

def handle_request(command , params):
    if command == 'DIR':
        return commands.dir(params)
    if command == 'DELETE':
        return commands.delete(params)
    if command == 'COPY':
        return commands.copy(params)
    if command == 'EXECUTE':
        return commands.execute(params)
    if command == "TAKE_SCREENSHOT":
        return commands.take_screenshot(params)
    if command == "DATE":
        return str(datetime.datetime.now())
    if command == "SEND_PHOTO":
        return commands.send_photo(params)

def send_respond(client_socket, cmd ,params):
    if cmd == "EXIT":
        client_socket.close()
        return True
    if cmd == "SEND_PHOTO":
        succeed, response = handle_request(cmd, params)
        if succeed:
            client_socket.send(response)
            return False
        else:
            response = protocol.create_msg(response)
            client_socket.send(response)
            return False         
    else:
        response = handle_request(cmd, params)
        response = protocol.create_msg(response)
        client_socket.send(response)
        return False


def main():
    with socket.socket() as server_socket:
        server_socket.bind(('0.0.0.0', 8820))
        server_socket.listen()
        print("Server is up and running")

        (client_socket, client_address) = server_socket.accept()
        print("Client connected his address {}".format(client_address))
        
        while True:
            is_okay, data = protocol.get_msg(client_socket)
            if is_okay:
                validation, cmd, params= check_request(data)
                if validation:
                    is_exit = send_respond(client_socket, cmd, params)
                    if is_exit:
                        break
                else:
                    message = protocol.create_msg("Wrong input, try again")
                    client_socket.send(message)
            else:
                message = protocol.create_msg("Wrong Protocol")
                client_socket.send(message)
if __name__ == "__main__":
    main()