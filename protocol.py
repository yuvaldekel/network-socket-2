import re
LENGTH_FIELD_SIZE = 4
PORT = 8820

#check if the command is in the right format
def check_cmd(data):
    return re.search("[Dd][Ii][Rr] .+$", data) or \
    re.search("^[Cc][Oo][Pp][Yy] .+ .+$", data) or \
    re.search("^[Dd][Ee][Ll][Ee][Tt][Ee] .+$", data) or \
    re.search("^[Ee][Xx][Ee][Cc][Uu][Tt][Ee] .+$", data) or \
    re.search("^[Ee][xX][Ii][Tt]$", data) or \
    re.search("^[tT][aA][kK][eE]_[sS][cC][rR][Ee][eE][Nn][sS][hH][oO][tT]$", data) or \
    re.search("^[sS][eE][nN][dD]_[pP][hH][oO][tT][oO]$", data) or \
    re.search("^[Dd][aA][Tt][Ee]$", data) 
    
#create the message with length area
def create_msg(data):
    length = str(len(data))
    zfill_length = length.zfill(LENGTH_FIELD_SIZE)
    message = zfill_length + data
    return message.encode()

#read the message from socket and return it, if the message follow the protocol return true, if the connection was closed return empty string 
def get_msg(my_socket):
    try:
        message_length = my_socket.recv(LENGTH_FIELD_SIZE).decode()
        if message_length == '':
            return False, ''
        message_length = int(message_length)
        data = my_socket.recv(message_length).decode()
        return True, data
    except ValueError:
        junk =  my_socket.recv(1024).decode()
        return False, "Error receiving massage"