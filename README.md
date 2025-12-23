# Emprunt — Mortgage Simulator (Scaffold)

This repository contains a minimal scaffold for a Python mortgage simulation app with a simple web GUI (FastAPI + Jinja2) using `uvicorn` as the dev server. It includes a VS Code Dev Container so you can develop in a reproducible environment.

## Features
- FastAPI backend
- Simple HTML form UI (Jinja2 templates)
- `numpy` and `pandas` available for future numerical work
- Devcontainer configuration to run inside VS Code

## Quick start
1. Open this folder in VS Code and click **Reopen in Container** when prompted, or use the command palette: `Remote-Containers: Reopen in Container`.
2. In the container, install dependencies (if not already done):

   ```bash
   pip install -r requirements.txt
   ```

3. Run the dev server:

   ```bash
   uvicorn emprunt.app:app --reload --host 0.0.0.0 --port 8000
   ```

4. Open your browser to `http://localhost:8000` (port forwarded by devcontainer).

## Devcontainer
- To start, use the Command Palette and choose `Remote-Containers: Reopen in Container` (or click **Reopen in Container**).
- Port 8000 is forwarded; the dev server command is `uvicorn emprunt.app:app --reload --host 0.0.0.0 --port 8000`.
- Recommended VS Code extensions (installed automatically via devcontainer): `ms-python.python`, `ms-python.vscode-pylance`.

## Development
- Run tests: `pytest -q`
- Linting/formatting not yet configured — feel free to add tools you prefer.

---

This scaffold aims to give a minimal but working project structure; the mortgage math is intentionally simple for now. Contributions and improvements welcome.
