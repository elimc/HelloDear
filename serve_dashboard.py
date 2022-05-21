from asyncio import subprocess
import http.server
import socketserver
from subprocess import Popen, run
from os.path import isdir
import sys

API_PORT = 8000
DASHBOARD_PORT = 8080

print("Don't forget to run `npm run build` first...")
try:
  Popen(f'waitress-serve --port={API_PORT} --host=localhost api.app:app')
except:
  print("Unable to serve API.")
  print(f"Make sure you don't already have something running on http://localhost:{API_PORT}")
  sys.exit()

# Serve dashboard
try:
  class Handler(http.server.SimpleHTTPRequestHandler):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, directory="dashboard/dist", **kwargs)
  Handler.extensions_map.update({
        ".js": "application/javascript",
  })


  httpd = socketserver.TCPServer(("", DASHBOARD_PORT), Handler)

  print(f'\n\n>>>>> ----- Serving dashboard on http://localhost:{DASHBOARD_PORT}\n\n')
  httpd.serve_forever()
except:
  print("Unable to serve dashboard.")
  print(f"Make sure you don't already have something running on http://localhost:{DASHBOARD_PORT}")