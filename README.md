# Bible Game App Deployment Guide

This guide provides step-by-step instructions to deploy the Bible Game App on a Linux server.

## Prerequisites

1. A Linux server with Python 3 installed.
2. Access to the server via SSH.
3. Basic knowledge of Linux commands.

## Deployment Steps

### 1. Clone the Repository

Log in to your server and clone the app repository:

```bash
git clone <repository-url> bible-app
cd bible-app
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

Run the database initialization script to set up the SQLite database:

```bash
python3 init_db.py
```

### 5. Run the App with Gunicorn

Install Gunicorn (if not already installed):

```bash
pip install gunicorn
```

Run the app using Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

The app will be accessible at `http://<server-ip>:8000`.

### 6. (Optional) Set Up a Reverse Proxy

For production, it is recommended to set up a reverse proxy (e.g., Nginx) to forward requests to Gunicorn. Refer to Nginx documentation for configuration details.

## Notes

- Ensure port 8000 is open in your server's firewall settings.
- Use a process manager like `systemd` or `supervisord` to keep the app running in the background.