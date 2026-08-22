#!/usr/bin/env python3
"""Static server for the poster folder + one POST endpoint the editor uses.

    POST /save?file=poster_2.html      body = full HTML

Only poster_*.html in this folder can be written. Every save first copies the
current file to .backups/<name>.<timestamp>.html, so nothing is ever lost.
HTML is served with no-store so edits show up on plain reload.
"""
import os, re, sys, time, json, shutil
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED = re.compile(r"^poster_\d+\.html$")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        if self.path.split("?")[0].endswith((".html", "/")):
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        if self.command == "POST" or "edit" in self.path:
            sys.stderr.write("%s %s\n" % (self.command, self.path))

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        u = urlparse(self.path)
        if u.path != "/save":
            return self._json(404, {"error": "unknown endpoint"})
        name = parse_qs(u.query).get("file", [""])[0]
        if not ALLOWED.match(name):
            return self._json(400, {"error": "only poster_N.html may be saved"})
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0 or length > 5_000_000:
            return self._json(400, {"error": "bad length"})
        html = self.rfile.read(length).decode("utf-8")
        if "<html" not in html[:400].lower() or "</html>" not in html[-200:].lower():
            return self._json(400, {"error": "body is not a whole HTML document"})
        target = os.path.join(ROOT, name)
        backups = os.path.join(ROOT, ".backups")
        os.makedirs(backups, exist_ok=True)
        if os.path.exists(target):
            stamp = time.strftime("%Y%m%d-%H%M%S")
            shutil.copy2(target, os.path.join(backups, f"{name[:-5]}.{stamp}.html"))
        tmp = target + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(html)
        os.replace(tmp, target)
        return self._json(200, {"ok": True, "file": name, "bytes": len(html)})


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8899
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"serving {ROOT} on http://localhost:{port}  (POST /save enabled)")
    srv.serve_forever()
