# main.py
import subprocess
import shutil
import os


""" ## Current Known Bugs ##
1. XX user input isn't parsing correctly. Check the two command functions.
2. XX Script crashes when inputting an incorrect command or 'q' for missing values.
3. XX The only command now opens chrome despite naming firefox or others in objects[]
"""

hotkey_quit = 'q'

# Settings
active = True

# Paths
PATH_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


verbs = ["open", "start", "launch"]
objects = ["google", "chrome", "firefox", "brave", "opera gx", "opera"]

###############
def toggle_active():
    global active
    active = not active
###############


# Finding Apps and opening them.
def process_user_input(user_input, verbs=verbs, objects=objects):
    """ 
    The point of this function is to roll through the user's command to find the verb and object to dynamically
    call the correct command instead of hard-coding each possible command with if-statements.
    * This is currently assuming the user's command is specifically two words.
    """
    # The user's command is already normalized and split, so we can work with it now.
    if len(user_input) >= 2:
        if user_input[0] in verbs:
            user_verb = user_input[0]
        if user_input[1] in objects:
            user_object = user_input[1]
    else:
        print(f"Can you expand on {user_input}?\n")
        user_verb, user_object = None, None
        return user_verb, user_object
    # end of function
    return user_verb, user_object


def commands(user_verb, user_object):
    if user_verb and user_object:
        if user_verb in verbs and user_object == "chrome":
            print(f"Executing: '{user_verb} {user_object}'\n")
            target_app = find_application(user_object)
            subprocess.Popen([target_app])
        
        else:
            print(f"Error: Unknown command: '{user_verb} {user_object}'\n")


def find_application(user_object): #### Currently searches entire drive. Takes too long...
    """Finds the application the user is looking to open."""
    path = shutil.which(user_object)
    if path:
        return path
    else:
        for root, dirs, files in os.walk("C://"):
            if user_object in files:
                path = os.path.join(root, user_object)
                return path
    return None
        

def ask_for_command():
        print(f"What can I do for you today? [Enter 'Q' to quit.]")
        user_input = input()
        user_input = user_input.strip().lower().split()
        
        if user_input[0] == hotkey_quit and len(user_input) == 1:
            return toggle_active()
        
        user_verb, user_object = process_user_input(user_input)
        commands(user_verb, user_object)
        

####################
# main()
def main():
    print(f"\nHello!")
    while active:
        ask_for_command()
    print(f"\nGoodbye!\n")
    # Debugging
    print("Shutil: ", shutil.which("chrome.exe"))
    print("Shutil: ", shutil.which("python.exe"))

    #end of main()
if __name__ == "__main__":
    main()