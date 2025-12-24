# Deployment Guide: Google Cloud Run

Follow these steps to deploy **Emprunt** to the internet.

## 1. Prerequisites
- A Google Cloud Platform (GCP) account.
- The `gcloud` CLI installed ([Install Link](https://cloud.google.com/sdk/docs/install)).

## 2. One-Time Setup
Run these commands in your terminal to authenticate and prepare your project:

```bash
# Authenticate with Google Cloud
gcloud auth login

# Set your project ID (replace YOUR_PROJECT_ID)
gcloud config set project YOUR_PROJECT_ID

# Enable the required APIs
gcloud services enable run.googleapis.com containerregistry.googleapis.com
```

## 3. Deploy
Run this single command from the root of your project:

```bash
gcloud run deploy emprunt-app \
  --source . \
  --region europe-west1 \
  --allow-unauthenticated
```

- `--source .`: Automatically builds the Docker image and pushes it to Google Artifact Registry.
- `--region`: You can change `europe-west1` to a region closer to you (e.g., `us-central1`).
- `--allow-unauthenticated`: Makes the app public.

## 4. Troubleshooting
- **Port Error**: Cloud Run expects the app to listen on the `$PORT` environment variable. Our `Dockerfile` is already configured for this.
- **Image Size**: If deployment is slow, check `.dockerignore` to ensure large files aren't being uploaded.

Your app will be available at a URL like `https://emprunt-app-xyz.a.run.app`.
