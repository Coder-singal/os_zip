from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import time

def add(x, y):
    return x + y

def start_server():
    server = SimpleXMLRPCServer(("localhost", 8000), logRequests=False)
    server.register_function(add, "add")
    print("RPC Server running on port 8000...")
    server.serve_forever()

if __name__ == "__main__":
    # Start the server in a background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Give the server a moment to start
    time.sleep(1)

    # --- Client side ---
    # Connect to the server
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        # Call the remote "add" function
        result = proxy.add(5, 3)
        print(f"Client received result: 5 + 3 = {result}")