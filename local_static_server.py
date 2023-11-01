from http.server import HTTPServer, BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/xml')
        self.send_header('Content-Disposition', 'attachment; filename="test-metadata.xml"')
        self.end_headers()

        # Open the file
        with open('/Users/sarah/test-metadata.xml', 'rb') as file:
            # Read the file and send the contents
            self.wfile.write(file.read())


myServer = HTTPServer(('localhost', 5678), MyServer)
myServer.serve_forever()
myServer.server_close()
