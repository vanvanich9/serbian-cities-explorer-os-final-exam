# Serbian Cities Explorer

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize Database

```bash
python init_db.py
```
- **Make sure PostgreSQL is running on your system before initializing the database**


### 3. Run the Application

```bash
gunicorn main:app --bind :8000 --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

## Access the Application

Open your browser and navigate to:
- **Main Page**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Project Structure

```
├── main.py              # FastAPI application
├── database.py          # Database models
├── init_db.py           # Init database
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── templates/           # HTML templates
│   ├── index.html       # Main page template
│   └── city_detail.html # City detail page template
└── static/              # Static files
    └── images/          # City images and SVG placeholders
```
