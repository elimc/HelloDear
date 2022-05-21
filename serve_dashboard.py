from asyncio import subprocess
import http.server
import socketserver
from subprocess import Popen
from os.path import isdir
from os import system
import sys
import traceback
from multiprocessing import Pool

from serve_api import serve_api

API_PORT = 8000
API_LISTEN_ON = f"127.0.0.1:{API_PORT}"
DASHBOARD_PORT = 8080

if __name__ == '__main__':
  # Build dashboard.
  if not isdir("dashboard/dist"):
      print("Building dashboard...")
      try:
          system("cd dashboard && npm i && npm run build")
      except:
          print("Unable to build dashboard")
          sys.exit()
      else:
          print("Done building dashboard.")

  # Serve API.
  try:
      print("\nStarting API...")      
      pool = Pool()
      pool.map_async(serve_api, [API_LISTEN_ON])
  except:
      print("Unable to serve API.")
      print(
          "Did you run `pip install requirements.txt`? Make sure you restart your shell afterwards."
      )
      print(
          f"Make sure you don't already have something running on {API_LISTEN_ON}"
      )
      print("|----- Error Message -----|")
      traceback.print_exc()
      sys.exit()
  else:
      print(f"API started at http://{API_LISTEN_ON}")

  # Serve dashboard
  try:

      class Handler(http.server.SimpleHTTPRequestHandler):
          def __init__(self, *args, **kwargs):
              super().__init__(*args, directory="dashboard/dist", **kwargs)

      Handler.extensions_map.update(
          {
              ".js": "application/javascript",
          }
      )

      httpd = socketserver.TCPServer(("", DASHBOARD_PORT), Handler)

      print(f"\n\n>>>>> ----- Serving dashboard on http://localhost:{DASHBOARD_PORT}\n\n")
      httpd.serve_forever()
  except:
      print("Unable to serve dashboard.")
      print(
          f"Make sure you don't already have something running on http://localhost:{DASHBOARD_PORT}"
      )
