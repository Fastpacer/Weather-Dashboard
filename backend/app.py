from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import requests
from backend.external_apis import get_current_weather , get_forecast_weather
from backend.crud import init_db, save_query
from backend.crud import get_all_queries
from backend.crud import clear_all_queries
from backend.export_utils import export_as_json, export_as_csv
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app= FastAPI()

# Insert this immediately after app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],            # allow all origins, or list your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="./frontend", html=True), name="frontend")

init_db()

@app.get("/")
def read_root():
    return {"message": "Weather API is up and running"}

@app.get("/weather")
def weather(location: str):
    result = get_current_weather(location)
    save_query(location, "current", result)
    return result

@app.get("/forecast")
def forecast(location: str):
    result = get_forecast_weather(location)
    save_query(location, "forecast", result)
    return result

@app.get("/history")
def history():
    return {"history": get_all_queries()}

@app.get("/clear")
def clear_history():
    clear_all_queries()
    return {"message": "All weather query history has been cleared."}

@app.get("/export")
def export_data(format: str = "json"):
    format = format.lower()
    if format == "json":
        return export_as_json()
    elif format == "csv":
        return export_as_csv()
    
