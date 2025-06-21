#!/usr/bin/env python3
"""
Simple HTTP API using Python's http.server module.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom request handler for the simple API."""

    def do_GET(self):
        """Handle GET requests to different endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Run the API server on port 8000."""
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
