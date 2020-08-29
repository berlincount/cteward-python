#!/usr/bin/env python3

import argparse
import requests

# Commandline parsing plus defaults
parser = argparse.ArgumentParser()
parser.add_argument("--dest", "-b", help="set hostname/ip to test", default="localhost")
parser.add_argument("--port", "-p", help="set port to test", type=int, default=8080)
parser.add_argument("--read-token", "-r", help="set token to test read access", default="readtoken")
parser.add_argument("--full-token", "-f", help="set token to test full access", default="fulltoken")
parser.add_argument("--store", "-d", help="set store to test against", default=".")
args = parser.parse_args()

print(args)

#class CtewardStorageTxtSimple(BaseHTTPRequestHandler):
#    def do_GET(self):
#        if self.headers["Authorization"] != "Bearer %s" % (args.read_token) and \
#           self.headers["Authorization"] != "Bearer %s" % (args.full_token):
#          self.send_error(401, "Unauthorized")
#          return
#
#        self.send_response(200)
#        self.send_header("Content-type", "text/html")
#        self.end_headers()
#        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
#        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
#        self.wfile.write(bytes("<body>", "utf-8"))
#        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
#        self.wfile.write(bytes("</body></html>", "utf-8"))
#
#    def do_POST(self):
#        if self.headers["Authorization"] != "Bearer %s" % (args.full_token):
#          self.send_error(401, "Unauthorized")
#          return
#
#        print("HIT")


if __name__ == "__main__":
    print("cteward-tst-st testing STorage engine on http://%s:%s" % (args.dest, args.port))

    try:
        r = requests.get("http://%s:%s" %(args.dest, args.port))
        print(r)
        print(r.elapsed)
        print(r.encoding)
        print(r.status_code)
        print(r.reason)
        print(r.headers)
        print(r.text)
    except requests.ConnectionError:
        print("meh")

    print("cteward-tst-st testing done.")
