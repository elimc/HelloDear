from asyncio import subprocess
import http.server
import socketserver
from subprocess import Popen
from os.path import isdir
from os import system
import sys
import traceback

API_PORT = 8000
DASHBOARD_PORT = 8080

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
    Popen(f"waitress-serve --port={API_PORT} --host=localhost api.app:app")
except:  
    print("Unable to serve API.")
    print("Did you run `pip install requirements.txt`?")
    print(
        f"Make sure you don't already have something running on http://localhost:{API_PORT}"
    )
    print("|----- Error Message -----|")
    traceback.print_exc()
    sys.exit()

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
