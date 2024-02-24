# Imports the libraries necessary for the script
import sys
import os

# Initializes initial variables tool for which tool the user wants to use and interface, for printing out the tool menu
tool = 0
interface = r'''

___________.__              .__    __________                   __               __              ___________                        _____  
\_   _____/|__| ____ _____  |  |   \______   \_______  ____    |__| ____   _____/  |_            \__    ___/___ _____    _____     /  |  | 
 |    __)  |  |/    \\__  \ |  |    |     ___/\_  __ \/  _ \   |  |/ __ \_/ ___\   __\   ______    |    |_/ __ \\__  \  /     \   /   |  |_
 |     \   |  |   |  \/ __ \|  |__  |    |     |  | \(  <_> )  |  \  ___/\  \___|  |    /_____/    |    |\  ___/ / __ \|  Y Y  \ /    ^   /
 \___  /   |__|___|  (____  /____/  |____|     |__|   \____/\__|  |\___  >\___  >__|               |____| \___  >____  /__|_|  / \____   | 
     \/            \/     \/                               \______|    \/     \/                              \/     \/      \/       |__| 

Enter one of the following numbers at anytime to swap to that function
1. Generate a password
2. Encrypt text
3. Decrypt text
4. Quit program
'''

# Function to swap program to correct tool
def tool_selection():
    global tool

    while True:
        tool = input("Test Which tool would you like to use? Input 1-3 to select. Input 4 to quit. ")
        if tool.isdecimal() != True:
            print(f"{tool} is not a valid option. Please input 1, 2, 3, or 4.")
        elif int(tool) >= 5:
            print(f"{tool} is not a valid option. Please input 1, 2, 3, or 4.")
        else:
            tool = int(tool)
            break

    if tool == 1:
        os.system("cls")
        print(interface)
        print("You've selected our Password Generator tool!")

    elif tool == 2:
        os.system("cls")
        print(interface)
        print("You've selected our Encryption tool!")
    
    elif tool == 3:
        os.system("cls")
        print(interface)
        print("You've selected our Decryption tool!")

    elif tool == 4:
        os.system("cls")
        print("Thank you for trying out our program!")
        sys.exit



# Prints the interface for the first-time tool selection
print(interface)

# Calls the function to select the tool
tool_selection()
