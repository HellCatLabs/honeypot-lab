import socket

HOST = "0.0.0.0"
PORT = 8080

def start_http_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[+] HTTP honeypot listening on {HOST}:{PORT}")

        while True:
            try:
                client_socket, addr = s.accept()
                print(f"[+] HTTP request from {addr[0]}:{addr[1]}")
                request = client_socket.recv(1024).decode(errors='ignore')
                print(request.strip())

                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html\r\n"
                    "\r\n"
                    "<h1>Welcome to my fake web server</h1>"
                )
                client_socket.sendall(response.encode())
                client_socket.close()
            except Exception as e:
                print(f"[!] Error: {e}")

if __name__ == "__main__":
    start_http_server()
