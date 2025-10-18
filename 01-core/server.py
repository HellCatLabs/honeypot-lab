import socket

HOST = "0.0.0.0"
PORT = 2222

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[+] Listening on {HOST}:{PORT}")

        while True:
            try:
                client_socket, addr = s.accept()
                print(f"[+] Connection from {addr[0]}:{addr[1]}")
                client_socket.close()
            except Exception as e:
                print(f"[!] Error: {e}")

if __name__ == "__main__":
    start_server()