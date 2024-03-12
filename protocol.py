import re
LENGTH_FIELD_SIZE = 4
PORT = 8820

def check_cmd(data):
    return re.search("[Dd][Ii][Rr] .+$", data) or \
    re.search("^[Cc][Oo][Pp][Yy] .+ .+$", data) or \
    re.search("^[Dd][Ee][Ll][Ee][Tt][Ee] .+$", data) or \
    re.search("^[Ee][Xx][Ee][Cc][Uu][Tt][Ee] .+$", data) or \
    re.search("^[Ee][xX][Ii][Tt]$", data) or \
    re.search("^[tT][aA][kK][eE]_[sS][cC][rR][Ee][eE][Nn][sS][hH][oO][tT]$", data) or \
    re.search("^[sS][eE][nN][dD]_[pP][hH][oO][tT][oO]$", data) or \
    re.search("^[Dd][aA][Tt][Ee]$", data) 
    

def create_msg(data):
    length = str(len(data))
    zfill_length = length.zfill(LENGTH_FIELD_SIZE)
    message = zfill_length + data
    return message.encode()

def get_msg(my_socket):
    try:
        length_message = my_socket.recv(LENGTH_FIELD_SIZE).decode()
        if length_message == '':
            return False, ''
        length_message = int(length_message)
        data = my_socket.recv(length_message).decode()
        return True, data
    except ValueError:
        junk =  my_socket.recv(1024).decode()
        return False, "Error"