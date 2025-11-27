import os

# File creation and writing
fp = open("example.txt", "w")

if fp is None:
    print("Error opening file!")
else:
    fp.write("Hello, File System in Python!\n")
    fp.close()

# File reading
fp = open("example.txt", "r")
buffer = fp.readline()
print("File Content:", buffer)
fp.close()

# Rename file
if os.path.exists("example_renamed.txt"):
    os.remove("example_renamed.txt")

os.rename("example.txt", "example_renamed.txt")
print("File renamed successfully.")

# Create a folder
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Folder created successfully.")

# Delete the file
os.remove("example_renamed.txt")
print("File deleted successfully.")
