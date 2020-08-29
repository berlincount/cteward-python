#!/usr/bin/env python3

import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer

# Commandline parsing plus defaults
parser = argparse.ArgumentParser()
parser.add_argument("--bind", "-b", help="set hostname/ip to serve on", default="localhost")
parser.add_argument("--port", "-p", help="set port to serve on", type=int, default=8080)
parser.add_argument("--read-token", "-r", help="set token to allow read access", default="readtoken")
parser.add_argument("--full-token", "-f", help="set token to allow full access", default="fulltoken")
parser.add_argument("--directory", "-d", help="set directory to server data from", default=".")
args = parser.parse_args()

print(args)

class CtewardStorageTxtSimple(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.headers["Authorization"] != "Bearer %s" % (args.read_token) and \
           self.headers["Authorization"] != "Bearer %s" % (args.full_token):
          self.send_error(401, "Unauthorized")
          return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        if self.headers["Authorization"] != "Bearer %s" % (args.full_token):
          self.send_error(401, "Unauthorized")
          return

        print("HIT")


if __name__ == "__main__":
    webServer = HTTPServer((args.bind, args.port), CtewardStorageTxtSimple)
    print("cteward-st-simple-txt started on http://%s:%s from %s" % (args.bind, args.port, args.directory))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("cteward-st-simple-txt stopped.")
