import shutil
import glob
import os
import subprocess
from pyautogui import screenshot

IMAGE_PATH = r'C:\Users\yonat\Documents\Yuval\devops\networking\network-socket-2\screen_server.jpg'

def dir(params):
    try:
        files = glob.glob(params[0])
        if len(files) == 0:
            return "There is not any file match the description." 
        return " ".join(files)
    except Exception as e:
        return "Error showing file is {} directory: {}.".format(params[0], e)
    
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
    
def take_screenshot(params):
    try:
        image = screenshot()
        image.save(IMAGE_PATH)
        return ""
    except Exception as e:
        return "Error {}".format(e)

def send_photo(params):
    try:
        image_size = os.path.getsize(IMAGE_PATH)
        message = str(len(str(image_size))).zfill(4) + str(image_size)
        with open(IMAGE_PATH, 'rb') as file:
            bytes_read = file.read()
            message = message.encode() + bytes_read
        return True, message
    except Exception as e:
        return False, f"Error: {e}"
