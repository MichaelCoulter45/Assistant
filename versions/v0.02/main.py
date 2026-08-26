# main.py
import subprocess
import shutil
import os
from functools import lru_cache
from pathlib import Path



""" ## Current Known Bugs ##
1. XX user input isn't parsing correctly. Check the two command functions.
2. XX Script crashes when inputting an incorrect command or 'q' for missing values.
3. XX The only command now opens chrome despite naming firefox or others in objects[]
4. XX Currently only hard coded objects are supported. Fix it to make dynamic.
5. Caching is vulnerable to becoming stale if the file is moved, uninstalled, or reinstalled.
"""
###
""" ## Things to do: ##
1. XX Make it so only the first word in user_input is the verb, and the rest is the object.
2. XX Update process_user_input(). 
3. Improve Cache application-path validation.
4. Add any and all drives to the search.
5. Add option to target search a drive/directory.
6. Add more likely directories.
7. Replace lru_cache with a saved to disk cache system.
8. Add layer to Caching system in-case the cache path is no longer existing. ie) reinstall a program
9. Make a safe guard for when the user inputs nothing or " ", where user_input[0] doesn't exist.

... After enabling speak to text, Add "Hey Jarvis, ..." for the program to listen to the command, ignoring everything else to prevent accidental commands. 
"""


# Hotkeys
hotkey_quit = 'q'

# Settings
active = True
verbs = ["open", "start", "launch"]
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
    user_verb, user_object = "", ""
    # The user's command is already normalized and split, so we can work with it now.
    if len(user_input) >= 2:
        if user_input[0] in verbs:
            user_verb = user_input[0]
        
            # All other words in user's input is the object.
            for word in user_input:
                if user_verb != word:
                    user_object.join(word + " ")
        
    else:
        print(f"Can you expand on {user_input}?\n")
        user_verb, user_object = None, None
        return user_verb, user_object
    # end of function
    return user_verb, user_object.strip()



@lru_cache
def find_application(user_object):
    """Searches some likely directories first, then the whole C drive."""
    path = shutil.which(user_object)
    user_object = user_object + ".exe"
    home_dir = Path.home()
    likely_directories = [r"C:\Program Files (x86)", 
                            r"C:\Program Files",
                            f"{home_dir}"
                            ]
    # Search loop using likely directories and then the whole drive
    # if cache is stale or doesn't exist:
    for directory in likely_directories:
        if path:
            break
        for root, dirs, files in os.walk(directory):
            # print(root, dirs, files) # Debugging
            if user_object in files:
                path = os.path.join(root, user_object)
                break
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
            print(target_app) # Debugging
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
    
    #end of main()
if __name__ == "__main__":
    main()
