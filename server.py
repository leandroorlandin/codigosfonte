import http.server
import socketserver

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Content-Type", "text/plain")
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Servidor ativo na porta", PORT)
    httpd.serve_forever()



# import http.server
# import socketserver

# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Servidor rodando na porta {PORT}")
#     httpd.serve_forever()
