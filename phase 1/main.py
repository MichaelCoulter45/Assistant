# main.py
# imports
import subprocess

# Paths
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


verbs = ["open", "start", "launch"]
objects = ["google", "chrome", "firefox", "brave", "opera gx", "opera"]


# commands
def commands(user_input):
    if user_input.strip().lower() == "open chrome":
        print(f"Executing: {user_input}")
        subprocess.run([chrome_path])
    else:
        print(f"Error. Unknown command.")
        

def ask_for_command():
        print(f"What can I do for you today?")
        commands(user_input=input())
        


# main()
def main():
    print(f"\nHello!")
    ask_for_command()
    
    #end of main()
    print()











# if name == main
if __name__ == "__main__":
    main()