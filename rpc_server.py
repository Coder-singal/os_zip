from xmlrpc.server import SimpleXMLRPCServer
def add_numbers(a, b):
    return a + b
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add_numbers, "add_numbers")
print("Server is ready...")
server.serve_forever()
