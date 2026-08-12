# main.py
# imports
import subprocess






""" ## Current Known Bugs ##
1. user input isn't parsing correctly. Check the two command functions.
2. Script crashes when inputting an incorrect command or 'q' for missing values.
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


def process_user_input(user_verb, user_object, verbs=verbs, objects=objects):
    
    return user_verb, user_object


# commands
def commands(user_verb, user_object):
    if user_verb and user_object:
        user_verb = user_verb.strip().lower()
        user_object = user_object.strip().lower()
        
    
        if user_verb == "open" and user_object == "chrome":
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
        user_input = user_input.split()
        for _ in range(len(user_input)):
        # for _ in range(len(verbs)):
            if user_input[0] == verbs[_]:
                user_verb = user_input[0]
        # for _ in objects:
            if user_input[1] == objects[_]:
                user_object = user_input[1]
        
        commands(user_verb, user_object)
        


# main()
def main():
    print(f"\nHello!")
    while active:
        ask_for_command()
    print(f"Goodbye!")
    
    #end of main()
    print()











# if name == main
if __name__ == "__main__":
    main()