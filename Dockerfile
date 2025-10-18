# Use a minimal Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the honeypot files
COPY ./04-log/final-server.py ./

# Expose the ports used by the honeypot
EXPOSE 8080 2222

# Default command
CMD ["python3", "final-server.py"]