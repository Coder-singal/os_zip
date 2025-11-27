import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
result = proxy.add_numbers(10, 5)
print("Sum =", result)
