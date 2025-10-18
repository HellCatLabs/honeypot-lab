# 01 - Core: Basic TCP Listener

## Objective

In this step, you'll build the foundation of your honeypot: a simple TCP server written in Python that listens for incoming connections on a given port.

## What You Need to Do

Write a script (`server.py`) that:
- Creates a TCP socket
- Binds to all interfaces (`0.0.0.0`) and a port like `2222`
- Listens for incoming connections
- Accepts multiple connections in a loop
- Logs the source IP and port of each client that connects

Example output:
```
[+] Connection from 192.168.1.42:50432
```

## Requirements

- Use the built-in `socket` module
- Handle errors gracefully if the client disconnects early
- Keep the server running until interrupted manually

## Tips

- Use `socket.AF_INET` and `socket.SOCK_STREAM` to create a TCP socket
- `bind()` it to `('0.0.0.0', 2222)`
- Call `listen()` to start listening for connections
- Use `accept()` inside a `while True:` loop to handle clients
- Log the client IP and port using `addr = client_socket.getpeername()`

## Next Step

Once your server works and logs incoming connections, move on to `02-http/` to build a fake HTTP service.
