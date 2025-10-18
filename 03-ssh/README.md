# 03 - SSH: Fake SSH Banner

## Objective

In this step, you'll simulate a fake SSH server. The goal is to make your honeypot appear like a real SSH service to attackers or scanning tools.

## What You Need to Do

Write a script ("fake_ssh.py") that:
- Listens on a port (suggested: 2222)
- Accepts incoming TCP connections
- Sends a standard SSH banner like:
  "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3"
- Receives any data sent by the client
- Logs the source IP, port, and any data received

Example output:
```
[+] SSH connection from 192.168.1.55:60322
Received: SSH-2.0-AnyScanner\r\n
```

## Requirements

- Use the "socket" module only
- Keep the server running in a loop
- Log connections and received data
- Do not actually implement SSH protocol (this is just a trap)

## Tips

- After "accept()", use "send()" to push the banner
- Clients might disconnect quickly — handle errors
- Log everything to console or a file for later review

## Next Step

In "04-log/", you'll add structured logging to file for both SSH and HTTP honeypot servers.
