import socket
import datetime
import protocol
import commands

NAME = "SuperServer"

#check if the command is valid return true if it is, also return  string of the command
#and the params if there is any 
def check_request(cmd):
    if protocol.check_cmd(cmd):
        params = cmd.split()
        command = params.pop(0).upper()
        return True, command, params
    return False, "", []

#handle the request, use commands module. the function return the message that the server need to send
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

#send the respond 
#if the command is exit close the connection
#if it is send_photo use the handle request to get the message from the command and the status 
#for all other commands use the handler to get the message create the  
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
        #create the server
        server_socket.bind(('0.0.0.0', 8820))
        server_socket.listen()
        print("Server is up and running")

        (client_socket, client_address) = server_socket.accept()
        print("Client connected his address {}".format(client_address))
        
        while True:
            #get the message
            is_okay, data = protocol.get_msg(client_socket)
            #if the message follow the protocol check the request and send a respond
            #if the message input didn't mach any command send "wrong input" 
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