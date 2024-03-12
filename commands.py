import shutil
import glob
import os
import subprocess
import protocol
from pyautogui import screenshot

IMAGE_PATH = r'C:\Users\yonat\Documents\Yuval\devops\networking\network-socket-2\screen_server.jpg'


#dir command, return files in a given directory returns the error if occurred 
def dir(params):
    try:
        files = glob.glob(params[0])
        if len(files) == 0:
            return "There is not any file match the description." 
        return " ".join(files)
    except Exception as e:
        return "Error showing file is {} directory: {}.".format(params[0], e)
    
#delete a file if succeeded returns nothing return the error if occurred 
def delete(params):
    try:
        os.remove(params[0])
        return ""
    except IsADirectoryError:
        return "Can not delete {}, is a directory.".format(params[0])
    except FileNotFoundError:
        return "Can not delete {}, does not exist.".format(params[0])
    except PermissionError:
        return "Can not delete {}, you don't have permission.".format(params[0])   
    
#copy file to other location returns the error if occurred
def copy(params):
    try:
        shutil.copy(params[0], params[1])
        return ""
    except shutil.SameFileError:
        return f"Can not copy {params[0]} file, they are the same file."
    except PermissionError:
        return f"Can not copy {params[0]} file, permission denied."
    except IsADirectoryError:
        return "Can not copy {}, is a directory.".format(params[0])
    except FileNotFoundError:
        return "Can not copy {}, file does not exist.".format(params[0])

#execute program returns the error if occurred 
def execute(params):
    try:
        subprocess.call(params[0])
        return ""
    except PermissionError:
        return f"Can not call {params[0]}, permission denied."
    except IsADirectoryError:
        return "Can not call {}, is a directory.".format(params[0])
    except FileNotFoundError:
        return "Can not call {}, file does not exist.".format(params[0])
    
#take screen shot
def take_screenshot(params):
    try:
        image = screenshot()
        image.save(IMAGE_PATH)
        return ""
    except Exception as e:
        return "Error {}".format(e)

#try to read the image return the message followed by the protocol requirements.
#the message is composed of the image size and the image it self.
#return boolean for the success of the function.
def send_photo(params):
    try:
        image_size = os.path.getsize(IMAGE_PATH)
        message = protocol.create_msg(image_size)
        with open(IMAGE_PATH, 'rb') as file:
            bytes_read = file.read()
        message = message.encode() + bytes_read
        return True, message
    except Exception as e:
        return False, f"Error: {e}"
