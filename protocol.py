LENGTH_FIELD_SIZE = 2
PORT = 8820

def check_cmd(data):
    if data == "DATE" or data == "WHORU" or data == "EXIT" or data == "RAND":
        return True
    return False

def create_msg(data):
    length = str(len(data))
    zfill_length = length.zfill(LENGTH_FIELD_SIZE)
    message = zfill_length + data
    return message

def get_msg(my_socket):
    try:
        length_message = my_socket.recv(2).decode()
        if length_message == '':
            return True, ''
        length_message = int(length_message)
        data = my_socket.recv(length_message).decode()
        return True, data
    except ValueError:
        return False, "Error"