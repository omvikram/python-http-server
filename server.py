import http.server
import socketserver

PORT = 8088 ##You can choose your port which is available to you
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.01", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()