import os

def main():
    filename = "testfile.txt"
    msg = "Hello from OS File System Call!"

    # --- Create and Write ---
    # O_CREAT: create if not exists, O_WRONLY: write-only, O_TRUNC: truncate file
    fd = os.open(filename, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o644)
    os.write(fd, msg.encode())   # encode string to bytes
    os.close(fd)

    # --- Read ---
    fd = os.open(filename, os.O_RDONLY)
    buffer = os.read(fd, 100)    # read up to 100 bytes
    print("Read from file:", buffer.decode())  # decode bytes to string
    os.close(fd)

if __name__ == "__main__":
    main()