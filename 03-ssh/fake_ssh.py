


import socket

HOST = "0.0.0.0"
PORT = 2222
BANNER = "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n"

def start_ssh_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[+] SSH honeypot listening on {HOST}:{PORT}")

        while True:
            try:
                client_socket, addr = s.accept()
                print(f"[+] SSH connection from {addr[0]}:{addr[1]}")
                client_socket.send(BANNER.encode())

                data = client_socket.recv(1024).decode(errors='ignore')
                if data:
                    print(f"Received: {data.strip()}")

                client_socket.close()
            except Exception as e:
                print(f"[!] Error: {e}")

if __name__ == "__main__":
    start_ssh_honeypot()