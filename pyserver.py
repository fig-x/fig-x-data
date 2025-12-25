import http.server, socketserver
class CORS(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    def do_OPTIONS(self):
        self.send_response(204); self.end_headers()

PORT=8081
with socketserver.TCPServer(("", PORT), CORS) as httpd:
    print(f"Serving with CORS on http://localhost:{PORT}")
    httpd.serve_forever()
PY
