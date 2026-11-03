# เซิร์ฟเวอร์ทดสอบ: ส่งหัวข้อ COOP/COEP ที่ Stockfish แบบ Multithreaded ต้องใช้
# วิธีใช้: python serve.py แล้วเปิด http://localhost:8000/chess-online.html
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

ThreadingHTTPServer(("", 8000), H).serve_forever()
