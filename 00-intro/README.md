# 00 - Introduction

## What is a Honeypot?

A **honeypot** is a deliberately exposed system or service that acts as a trap to detect, deflect, or study hacking attempts. It looks like a real server or service — but in reality, it's isolated and monitored.

In cybersecurity, honeypots are used to:
- Understand attacker behavior
- Collect indicators of compromise (IP, payloads, patterns)
- Slow down attackers or distract them
- Test intrusion detection systems (IDS)

In this lab, you'll build a **very simple honeypot in Python**, without external libraries, that:
- Listens on fake SSH (port 22) and HTTP (port 80)
- Accepts incoming connections
- Logs everything that happens


## Who is this lab for?

This lab is designed for **absolute beginners in cybersecurity and Python**. If you've never touched sockets or honeypots before, you're in the right place.

You'll learn:
- How TCP socket programming works
- How to simulate a fake service
- How to capture and log incoming data
- How to reason like a defender

## What you'll need

- Python 3.x installed
- Basic terminal usage
- A safe environment (VM or Docker recommended)

Optional:
- A text editor (VS Code, Sublime, etc.)
- Curiosity 👀

## Project Structure

We'll work step by step, with each part in its own folder:
- `01-core/` → basic TCP listener
- `02-http/` → fake HTTP service
- `03-ssh/` → fake SSH banner
- `04-log/` → basic logging system

You’ll be guided at each step with challenges, hints, and full corrections.

## Let’s go!

Move to `01-core/` and start coding your first TCP server in Python.

If you’re stuck at any point, check the hints or look at the solution file. Ready? 👇