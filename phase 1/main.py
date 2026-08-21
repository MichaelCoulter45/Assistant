# main.py
import subprocess
import shutil
import os
from pathlib import Path



""" ## Current Known Bugs ##
1. XX user input isn't parsing correctly. Check the two command functions.
2. XX Script crashes when inputting an incorrect command or 'q' for missing values.
3. XX The only command now opens chrome despite naming firefox or others in objects[]
4. Currently only hard coded objects are supported. Fix it to make dynamic.
"""
###
""" 
Things to do:
1. Make it so only the first word in user_input is the verb, and the rest is the object.
2. Update process_user_input(). 
"""



hotkey_quit = 'q'

# Settings
active = True

# Paths
PATH_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


verbs = ["open", "start", "launch"]
# objects = ["google", "chrome", "firefox", "brave", "opera gx", "opera"]

###############
def toggle_active():
    global active
    active = not active
###############


# Finding Apps and opening them.
def process_user_input(user_input, verbs=verbs):
    """ 
    The point of this function is to roll through the user's command to find the verb and object to dynamically
    call the correct command instead of hard-coding each possible command with if-statements.
    * This is currently assuming the user's command is specifically two words.
    """
    user_object = ""
    # The user's command is already normalized and split, so we can work with it now.
    if len(user_input) >= 2:
        if user_input[0] in verbs:
            user_verb = user_input[0]
        
        # All other words in user's input is the object.
        for word in user_input:
            user_object += word + " "
        
    else:
        print(f"Can you expand on {user_input}?\n")
        user_verb, user_object = None, None
        return user_verb, user_object
    # end of function
    return user_verb, user_object[len(user_verb):].strip()


def find_application(user_object): #### Currently searches entire drive. Takes too long...
    """Finds the application the user is looking to open."""
    path = shutil.which(user_object)
    if path:
        return path
    
    home_dir = Path.home()
    search_likely_directories = [r"C:\Program Files", 
                                 r"C:\Program Files (x86)", 
                                 fr"{home_dir}\AppData\Local", 
                                 r"C:\\",
                                 ]
    user_object = user_object + ".exe"
    
    # Search loop using 
    for word in search_likely_directories:
        for root, dirs, files in os.walk(word):
            if user_object in files:
                path = os.path.join(root, user_object)
                return path
    
    
    # Search likely locations first:
    # # C:\Program Files
    # for root, dirs, files in os.walk(r"C:\Program Files"): 
    #     if user_object in files:
    #         path = os.path.join(root, user_object)
    #         return path
    
    # # C:\Program Files (x86)
    # for root, dirs, files in os.walk(r"C:\Program Files (x86)"): 
    #     if user_object in files:
    #         path = os.path.join(root, user_object)
    #         return path
    
    # # ...\Appdata\Local
    # for root, dirs, files in os.walk(f"{home_dir}"+"\AppData\Local"): # <-------------------- This line
    #     if user_object in files:
    #         path = os.path.join(root, user_object)
    #         return path
    
    # # Last Resort: Walk the whole C:\ drive to find the target.
    # for root, dirs, files in os.walk(r"C:\\"):
    #     if user_object in files:
    #         path = os.path.join(root, user_object)
    #         return path
    return path


def ask_for_command():
        print(f"What can I do for you today? [Enter 'Q' to quit.]")
        user_input = input()
        user_input = user_input.strip().split()
        
        if user_input[0] == hotkey_quit and len(user_input) == 1:
            return toggle_active()
        
        user_verb, user_object = process_user_input(user_input)
        commands(user_verb, user_object)
        


def commands(user_verb, user_object):
    if user_verb and user_object:
        # if user_verb in verbs and user_object == "chrome":
        print(f"Executing: '{user_verb} {user_object}'\n")
        target_app = find_application(user_object)
        if target_app:
            print(target_app)
            subprocess.Popen([target_app])
        else:
            print(f"Cannot find {user_object}.\n")
    else:
        print(f"Error: Unknown command: '{user_verb} {user_object}'\n")
####################
# main()
def main():
    print(f"\nHello!")
    while active:
        ask_for_command()
    print(f"\nGoodbye!\n")
    # Debugging
    # print("Shutil: ", shutil.which("chrome.exe"))
    # print("Shutil: ", shutil.which("python.exe"))

    #end of main()
if __name__ == "__main__":
    main()