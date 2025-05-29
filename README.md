# 🌤️ Weather Dashboard

A full-stack weather dashboard built using **FastAPI** (Python) for the backend and **Vanilla HTML/CSS/JS** for the frontend. Users can search current weather or a 5-day forecast for any location, view search history, export data, and more.

---

## 🔧 Features

* 🔍 Search current weather by city or ZIP code
* 📆 View 5-day weather forecast
* 📜 View search history (stored in SQLite)
* 🧹 Clear history
* 📁 Export history (JSON or CSV)
* ✨ Clean, minimal UI (vanilla JS, no frameworks)
* 🚀 Fully deployed via Render (free tier)

---

## 🏗️ Project Structure

```
PM_Accelerator/
├── backend/
│   ├── app.py                # FastAPI app entry point
│   ├── crud.py               # SQLite DB logic
│   ├── external_apis.py      # OpenWeatherMap API functions
│   └── export_utils.py       # CSV/JSON export logic
│
├── frontend/
│   ├── index.html            # Main web page
│   ├── main.js               # JS logic (fetch, render)
│   └── styles.css            # Optional styling
│
├── database/
│   └── weather.db            # SQLite DB file (auto-created)
│
├── requirements.txt         # Python dependencies
├── render.yaml              # Deployment config (Render.com)
└── .env                     # (Not committed) API key
```

---

## 🚀 Local Development

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard
```

### 2. Set up virtual environment

```bash
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenWeatherMap API key

Create a `.env` file in the root with:

```
OPENWEATHER_API_KEY=your_api_key_here
```

### 5. Run the server

```bash
uvicorn backend.app:app --reload
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🌐 Deployment (via Render)

1. Push this code to a public GitHub repository.
2. Create a free account at [render.com](https://render.com).
3. Click **"New Web Service"** → Connect your repo.
4. For build command: `pip install -r requirements.txt`
5. For start command: `uvicorn backend.app:app --host 0.0.0.0 --port 10000`
6. Add your `OPENWEATHER_API_KEY` as an environment variable in the Render dashboard.
7. Done! 🎉 Your app will be live at a URL like `https://weather-dashboard.onrender.com`

---

## 📦 Requirements

* Python 3.8+
* FastAPI
* Uvicorn
* requests
* python-dotenv

Install them via:

```bash
pip install -r requirements.txt
```

---

## 📸 Demo Screenshot

*(Optional: Add one when deployed)*

---

## 🧠 Inspiration

This project was built to learn how to:

* Build REST APIs using FastAPI
* Integrate frontend with backend cleanly
* Handle CORS and live reload issues
* Deploy full-stack apps for free

---

## 🧊 Author

Built with patience, fire, and debugging by **Atharva** ✨


