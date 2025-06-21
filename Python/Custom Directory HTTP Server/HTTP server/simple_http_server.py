import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer


class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        # Pass directory and other arguments correctly to the base class
        self.directory = directory
        super().__init__(*args, **kwargs)  # This calls the parent class's __init__ method


def run_server(port, directory):
    # Change working directory to the specified directory
    os.chdir(directory)

    # Define server address and port
    server_address = ('', port)

    # Define the request handler using a lambda to include the directory argument
    handler = lambda *args: CustomHTTPRequestHandler(*args, directory=directory)

    # Create the HTTP server with the specified address and request handler
    httpd = HTTPServer(server_address, handler)

    print(f"Serving directory '{directory}' at http://localhost:{port}")

    # Start the server
    httpd.serve_forever()


if __name__ == "__main__":
    # Set the port and directory here
    PORT = 8000
    DIRECTORY = "/path/to/your/directory"  # Replace with your actual directory path

    # Check if the directory exists
    if not os.path.isdir(DIRECTORY):
        print(f"Directory {DIRECTORY} does not exist.")
        sys.exit(1)

    run_server(PORT, DIRECTORY)
