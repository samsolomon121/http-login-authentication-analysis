
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class LoginHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        page = """
        <html>
        <head><title>Cybersecurity Login Lab</title></head>
        <body>
            <h2>My Test Login Page</h2>
            <form method="POST" action="/login">
                Username: <input name="username"><br><br>
                Password: <input name="password" type="password"><br><br>
                <button type="submit">Login</button>
            </form>
        </body>
        </html>
        """

        self.wfile.write(page.encode())

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode()
        details = parse_qs(data)

        print("Test login submitted:")
        print("Username:", details.get("username", [""])[0])
        print("Password:", details.get("password", [""])[0])

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Test login received successfully!")

server = HTTPServer(("127.0.0.1", 8000), LoginHandler)

print("Server running at http://127.0.0.1:8000")
server.serve_forever()
