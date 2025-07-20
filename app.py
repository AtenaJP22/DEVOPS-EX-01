from http.server import BaseHTTPRequestHandler, HTTPServer
import random

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head>
            <style>
                body {
                    font-family: sans-serif;
                    background-color: #f5f5f5;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    padding-top: 30px;
                }
                h1 {
                    color: #2ca8d8;
                }
                .grid {
                    display: grid;
                    grid-template-columns: repeat(10, 40px);
                    gap: 5px;
                    margin-top: 20px;
                }
                .cell {
                    width: 40px;
                    height: 40px;
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <h1>Hello from Backend! <3 </h1>
            <div class="grid">
        """

        # Generate 100 colored blocks
        for _ in range(100):
            color = f"#{random.randint(0, 0xFFFFFF):06x}"
            html += f'<div class="cell" style="background-color: {color};"></div>'

        html += """
            </div>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("", 5055)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Running backend server on port 5055...")
    httpd.serve_forever()