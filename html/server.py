from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
from urllib.request import urlopen
import mimetypes, os

class NotesRH(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.path = unquote(self.path)
        self.send_response(200)
        if self.path == "/index":
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write("<html><head><link rel=\"stylesheet\" href=\"retro.css\" /></head><body><ul>".encode())
            for file in os.listdir("./html/"):
                if file.endswith(".html"):
                    self.wfile.write(f"<li><a href=\"{'./html/'+file}\">{file[:-9]}</a></li>".encode())
            # for file in os.listdir("./mds/"):
            #     if file.endswith(".mds"):
            #         self.wfile.write(f"<li><a href=\"{'./mds/'+file}\">{file[:-4]} </a></li>".encode())
                self.wfile.write("</body></html>".encode())
        elif self.path[6:] in os.listdir("./html"):
            self.send_header("content-type", mimetypes.guess_type(self.path))
            self.end_headers()
            with open("." + self.path, "rb") as file:
                self.wfile.write(file.read())
        elif self.path.endswith("/retro.css"):
            self.send_header("content-type", "text/css")
            self.end_headers()
            # with open("./html/retro.css", "rb") as cssfile:
            #     self.wfile.write(cssfile.read())
            self.wfile.write(urlopen("https://notes.zortax.de/css/retro.css").read())
        elif self.path[5:] in os.listdir("./mds"):
            self.send_header("content-type", "text/html")
            self.end_headers()
            os.system(f"python ./compile_markdown.py \".{self.path}\" \"./html/{self.path[5:]}.html\"")
            with open("./html/" + self.path[5:]+".html", "rb") as file:
                self.wfile.write(file.read())

if __name__ == "__main__":
    with HTTPServer(("", 80), NotesRH) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()