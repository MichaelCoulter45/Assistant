# main.py
# imports
import subprocess






""" ## Current Known Bugs ##
1. user input isn't parsing correctly. Check the two command functions.
"""




# Settings
active = True

# Paths
PATH_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


verbs = ["open", "start", "launch"]
objects = ["google", "chrome", "firefox", "brave", "opera gx", "opera"]


def toggle_active():
    global active
    active = not active


# commands
def commands(user_verb, user_object):
    user_verb = user_verb.strip().lower()
    user_object = user_object.strip().lower()
    
    for _ in range(len(verbs)):
        if user_verb == verbs[_] and user_object == "chrome":
            print(f"Executing: '{user_verb} {user_object}'\n")
            subprocess.Popen([PATH_CHROME])
        elif user_verb == "q":
            toggle_active()
        else:
            print(f"Error. Unknown command: '{user_verb} {user_object}'\n")
        


def ask_for_command():
        print(f"What can I do for you today? [Enter 'Q' to quit.]")
        user_input = input()
        user_input = user_input.split()
        for _ in range(len(verbs)):
            if user_input[0] == verbs[_]:
                user_verb = user_input[0]
        for _ in objects:
            if user_input[1] == objects:
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