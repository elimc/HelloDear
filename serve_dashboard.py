import http.server
import socketserver

PORT = 8080

try:
  class Handler(http.server.SimpleHTTPRequestHandler):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, directory="dashboard/dist", **kwargs)
  Handler.extensions_map.update({
        ".js": "application/javascript",
  });


  httpd = socketserver.TCPServer(("", PORT), Handler)

  print(f'Serving dashboard on http://localhost:{PORT}')
  httpd.serve_forever()
except:
  print("Unable to serve dashboard. Did you build it? Make sure to run `npm run build` in the dashboard directory first.")