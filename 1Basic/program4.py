# Write a python program to print the contents of a directory using the os module.Search online for the function which does that.  
import os

# Path of the directory you want to list
directory_path = input("/")

try:
    # os.listdir returns a list of all files and directories in the specified path
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The directory does not exist.")
except PermissionError:
    print("Error: You do not have permission to access this directory.")
except Exception as e:
    print("An error occurred:", e)


# How It Works
# Import the os module — this module lets you interact with the operating system.
# os.listdir(path) — returns a list of the names of all entries (files and subdirectories) in the given directory. If no path is provided, it lists the current working directory. 
# GeeksforGeeks
# Error handling — catches cases where the directory does not exist or permission is denied.