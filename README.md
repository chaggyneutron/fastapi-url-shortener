 🚀 FastAPI URL Shortener — DevOps Project
URL shortener backend built with FastAPI, fully containerized with Docker, tested with pytest, and deployed on a Kubernetes cluster.
The CI pipeline automatically builds and pushes Docker images to GitHub Container Registry (GHCR) using GitHub Actions.

🧰 Tech Stack
# Backend

Python 3.12

FastAPI

SQLModel

SQLite

Uvicorn

# DevOps

Docker

GitHub Actions

GitHub Container Registry (GHCR)

Kubernetes (Minikube)

kubectl

✨ Features

🔗 Create short URLs from long ones

🔁 Redirect from short URL to original URL

📈 Track click count

🩺 /health endpoint for probes and monitoring

📄 Automatic API docs available at /docs (Swagger UI)

🧪 Full test suite with pytest

🐳 Dockerized application

⚙️ CI pipeline: test → build → push image

☸️ Kubernetes deployment with:

# 2 replicas

# Liveness & Readiness probes

# NodePort service for external access

