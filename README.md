# honeypot-lab

🧲 A beginner-friendly lab to build your own Python honeypot from scratch (SSH & HTTP). Learn how to simulate fake services, capture incoming traffic, and log attacker behavior — step by step, with explanations and a full solution.

![honeypot-lab](./.github/banner.png)

## Disclaimer

This project is for **educational purposes only**.  
It is intended to help beginners understand how honeypots work and how attackers behave on a network.  
Do **not** expose this honeypot directly to the internet without proper containment (e.g., VM, Docker, firewall).  
Use responsibly and at your own risk.

## Lab Structure

Each part of the lab is designed to be done incrementally. You should go through the steps in order, and try to write the code yourself before looking at the correction.

```
00-intro/     → Introduction, objectives, and setup instructions  
01-core/      → Create a simple TCP socket listener in Python  
02-http/      → Build a fake HTTP server that logs all requests  
03-ssh/       → Simulate an SSH banner and capture incoming data  
04-log/       → Implement logging to file and structure output  
```

Each folder contains:
- A guided exercise (README + comments in code)
- Hints or partial implementations
- A complete working solution


## Bonus (optional)

A `Dockerfile` is included to run the honeypot safely inside a container.
To build and run the honeypot using Docker, use the following commands:
```
docker build -t honeypot-lab .
docker run -p 8080:8080 -p 2222:2222 honeypot-lab
```

## Feedback & Contributions

Feel free to open issues or PRs if you want to improve this lab, add more features, or suggest new educational topics!

Made with ☠️ by [HellcatLabs](https://github.com/hellcatlabs)
