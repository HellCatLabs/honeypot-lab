import socket
import threading
import datetime

LOG_FILE = "honeypot.log"

def log_event(event_type, addr, data=""):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] [{event_type}] {addr[0]}:{addr[1]} - {data.strip()}\n")
    print(f"[{timestamp}] [{event_type}] {addr[0]}:{addr[1]} - {data.strip()}")

def handle_ssh_client(client_socket, addr):
    try:
        banner = "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n"
        client_socket.send(banner.encode())
        data = client_socket.recv(1024).decode(errors="ignore")
        log_event("SSH", addr, data)
    except Exception as e:
        log_event("SSH", addr, f"Error: {e}")
    finally:
        client_socket.close()

def handle_http_client(client_socket, addr):
    try:
        data = client_socket.recv(1024).decode(errors="ignore")
        log_event("HTTP", addr, data)
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<h1>Welcome to my fake web server</h1>"
        )
        client_socket.sendall(response.encode())
    except Exception as e:
        log_event("HTTP", addr, f"Error: {e}")
    finally:
        client_socket.close()

def start_server(port, handler, label):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        s.listen(5)
        print(f"[+] {label} honeypot listening on port {port}")
        while True:
            client_socket, addr = s.accept()
            threading.Thread(target=handler, args=(client_socket, addr)).start()

if __name__ == "__main__":
    threading.Thread(target=start_server, args=(2222, handle_ssh_client, "SSH"), daemon=True).start()
    threading.Thread(target=start_server, args=(8080, handle_http_client, "HTTP"), daemon=True).start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[!] Honeypot stopped.")