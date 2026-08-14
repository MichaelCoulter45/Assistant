# main.py
# imports
import subprocess






""" ## Current Known Bugs ##
1. XX user input isn't parsing correctly. Check the two command functions.
2. Script crashes when inputting an incorrect command or 'q' for missing values.
3. XX The only command now opens chrome despite naming firefox or others in objects[]
"""


user_verb = "None"
user_object = "None"
hotkey_quit = 'q'
# Settings
active = True

# Paths
PATH_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


verbs = ["open", "start", "launch"]
objects = ["google", "chrome", "firefox", "brave", "opera gx", "opera"]


def toggle_active():
    global active
    active = not active


def process_user_input(user_input, verbs=verbs, objects=objects):
    """ 
    The point of this function is to roll through the user's command to find the verb and object to dynamically
    call the correct command instead of hard-coding each possible command with if-statements.
    * This is currently assuming the user's command is specifically two words.
    """
    # The user's command is already normalized and split, so we can work with it now.
    if len(user_input) >= 2:
        for _ in range(len(verbs)):
            if user_input[0] == verbs[_]:
                user_verb = user_input[0]
            else:
                user_verb = "None"
                
        for _ in range(len(objects)):
            if user_input[1] == objects[_]:
                user_object = user_input[1]
            else:
                user_object = "None"
    else:
        print(f"Can you expand on '{user_input}'?")
    # end of function
    return user_verb, user_object


# commands
def commands(user_verb, user_object):
    if user_verb and user_object:
        if user_verb in verbs and user_object == "chrome":
            print(f"Executing: '{user_verb} {user_object}'\n")
            subprocess.Popen([PATH_CHROME])
        
        else:
            print(f"Error. Unknown command: '{user_verb} {user_object}'\n")
    else:
        print(f"Error. Unknown command: '{user_verb} {user_object}'\n")


def ask_for_command():
        print(f"What can I do for you today? [Enter 'Q' to quit.]")
        user_input = input()
        user_input = user_input.strip().lower().split()
        if user_input[0] == hotkey_quit and len(user_input) == 1:
            return toggle_active()
        user_verb, user_object = process_user_input(user_input)
        commands(user_verb, user_object)
        


# main()
def main():
    print(f"\nHello!")
    while active:
        ask_for_command()
    print(f"\nGoodbye!")
    print()
    #end of main()
if __name__ == "__main__":
    main()