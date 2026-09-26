"""Run the standalone prototype with caching disabled during design review."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()


if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    handler = partial(PreviewHandler, directory=str(root))
    server = ThreadingHTTPServer(('0.0.0.0', 4173), handler)
    print('Oktravel preview: http://localhost:4173', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
