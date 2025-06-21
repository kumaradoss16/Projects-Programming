from http.server import SimpleHTTPRequestHandler, HTTPServer
# Import the SimpleHTTPRequestHandler class and HTTPServer class from the http.server module.
# SimpleHTTPRequestHandler is used to handle HTTP requests, and HTTPServer sets up the server.

Port = 8080
# Define the port number on which the server will listen for incoming requests.
server_address = ("", Port)
# Create a tuple with an empty string as the hostname and the defined port number.
# An empty string for the hostname means the server will accept connections on all available network interfaces.

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
# Create an instance of HTTPServer with the specified server_address and request handler (SimpleHTTPRequestHandler).
# This sets up the server to use SimpleHTTPRequestHandler to handle incoming HTTP requests.

print(f"Serving at http://localhost:{Port}")
# Print a message to the console indicating the URL where the server is accessible.
# It uses the defined port number to complete the URL.

httpd.serve_forever()
# Start the server and enter an infinite loop, waiting and handling incoming HTTP requests.
# The server will continue running until manually stopped.
