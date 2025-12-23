# Simple devcontainer for the Emprunt project
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.11

# Create a non-root user and workdir are already handled by the base image
WORKDIR /workspace

# Install project requirements (postCreateCommand will also run in devcontainer)
COPY requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# Optional: keep image small by cleaning cache
RUN pip cache purge || true
