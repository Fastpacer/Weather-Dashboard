import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("✅ external_apis.py loaded")
print(f"API KEY being used: {OPENWEATHER_API_KEY}")

def get_current_weather(location: str):
    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    print("📨 Request Params:", params)

    try:
        print(f"\n📡 Fetching weather for: {location}")
        response = requests.get(BASE_URL, params=params)
        print("🌐 Request URL:", response.url)
        print("📦 Status Code:", response.status_code)

        response.raise_for_status()

        data = response.json()
        print("🧾 Parsed JSON:", data)

        # Check if the required keys exist
        if "main" in data and "weather" in data and isinstance(data["weather"], list):
            weather_info = {
                "location": data.get("name", "Unknown"),
                "temperature": data["main"].get("temp"),
                "description": data["weather"][0].get("description"),
                "icon": data["weather"][0].get("icon")
            }
            return weather_info
        else:
            print("❗ Missing expected keys in JSON.")
            return {"location": location, "error": "Unexpected response format"}

    except requests.exceptions.HTTPError as http_err:
        print("❌ HTTP error:", http_err)
        return {"location": location, "error": f"HTTP error: {http_err}"}

    except Exception as e:
        print("❌ General exception:", e)
        return {"location": location, "error": "Could not fetch weather data"}


def get_forecast_weather(location: str):
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        print(f"\n📡 Fetching 5-day forecast for: {location}")
        response = requests.get(forecast_url, params=params)
        print("🌐 Forecast URL:", response.url)
        print("📦 Status Code:", response.status_code)
        response.raise_for_status()

        data = response.json()
        print("🧾 Forecast JSON received")

        # Extract daily summaries (every 8th item = ~24 hours)
        forecasts = []
        for i in range(0, len(data["list"]), 8):
            entry = data["list"][i]
            forecasts.append({
                "date": entry["dt_txt"].split(" ")[0],
                "temperature": entry["main"]["temp"],
                "description": entry["weather"][0]["description"],
                "icon": entry["weather"][0]["icon"]
            })

        return {
            "location": data["city"]["name"],
            "forecasts": forecasts
        }

    except Exception as e:
        print("❌ Forecast error:", e)
        return {"location": location, "error": "Could not fetch forecast data"}

   
