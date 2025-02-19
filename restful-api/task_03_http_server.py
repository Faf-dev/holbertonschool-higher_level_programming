#!/usr/bin/python3
"""
Create a simple API
"""
import json
import http.server


class My_class(http.server.BaseHTTPRequestHandler):
    """
    My_class : inherits from BaseHTTPRequestHandler class.
    """
    def do_GET(self):
        """
        Handle some GET requests
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))


def run(server_class=http.server.HTTPServer, handler_class=My_class):
    """
    Start an HTTP server with port 8000
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
