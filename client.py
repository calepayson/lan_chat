import socket

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (localhost on port 12345)
sock.connect(('127.0.0.1', 12345))

# Send some data
sock.sendall(b"Hello, server!")

# Close the connection
sock.close()

