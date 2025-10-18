# 02 - HTTP: Fake Web Server

## Objective

Now that you have a working TCP listener, let's simulate a fake HTTP service. You'll build a simple Python server that:

- Listens on port 8080
- Accepts incoming HTTP requests
- Logs the full request data (headers, method, path, etc.)
- Responds with a basic HTTP 200 OK and a small HTML message

## What You Need to Do

Write a script ("fake_http.py") that:
- Uses "socket" to listen on "0.0.0.0:8080"
- Accepts multiple connections
- Reads the request using "recv()"
- Prints/logs the full request
- Sends a valid HTTP response back

Example log output:
```
[+] HTTP request from 192.168.1.10:53211
GET /index.html HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: curl/7.79.1
...
```

Example response:
```
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Welcome to my fake web server</h1>
```

## Requirements

- Do not use "http.server" or external libraries
- Support at least GET requests (no need to parse everything)
- Keep it simple and readable

## Tips

- After "accept()", call "recv(1024)" to get the request
- Use "client.sendall()" to send your response
- Close each connection after handling it

## Next Step

In "03-ssh/", you'll simulate an SSH server banner and capture data from connection attempts.
