LENGTH_FIELD_SIZE = 2

def check_cmd(data):
    if data == "DATE" or data == "WHORU" or data == "EXIT" or data == "RAND":
        return True
    return False

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