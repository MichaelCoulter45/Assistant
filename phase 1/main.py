# main.py
# imports
import subprocess






""" ## Current Known Bugs ##
1. XX user input isn't parsing correctly. Check the two command functions.
2. Script crashes when inputting an incorrect command or 'q' for missing values.
3. The only command now opens chrome despite naming firefox or others in objects[]
"""




# Settings
active = True

# Paths
PATH_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

user_verb = "None"
user_object = "None"
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
    for _ in range(len(verbs)):
        if user_input[0] == verbs[_]:
            user_verb = user_input[0]
        if user_input[1] == objects[_]:
            user_object = user_input[1]
    # end of function
    return user_verb, user_object


# commands
def commands(user_verb, user_object):
    if user_verb and user_object:
        
    
        if user_verb in verbs and user_object in objects:
            print(f"Executing: '{user_verb} {user_object}'\n")
            subprocess.Popen([PATH_CHROME])
        elif user_verb == "q":
            return toggle_active()
        else:
            print(f"Error. Unknown command: '{user_verb} {user_object}'\n")
    else:
        print(f"Error. Unknown command: '{user_verb} {user_object}'\n")


def ask_for_command():
        print(f"What can I do for you today? [Enter 'Q' to quit.]")
        user_input = input()
        user_input = user_input.strip().lower().split()
        user_verb, user_object = process_user_input(user_input)
        commands(user_verb, user_object)
        


# main()
def main():
    print(f"\nHello!")
    while active:
        ask_for_command()
    print(f"\nGoodbye!")
    
    #end of main()
    print()











# if name == main
if __name__ == "__main__":
    main()