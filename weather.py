import urequests
import time
import ujson

def load_config():
    """Načte API klíč z CONFIGURATION.txt"""
    with open("CONFIGURATION.txt", "r") as f:
        return ujson.loads(f.read())

config = load_config()
API_KEY = config["api_key"]

# --- API URLS ---
IP_API_URL = "http://208.95.112.1/json/"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_location():
    """
    Získá geolokaci podle veřejné IP.
    Vrací dict: {lat, lon, city, country}
    """
    try:
        response = urequests.get(IP_API_URL)
        data = response.json()
        response.close()

        if data.get("status") != "success":
            print("IP API returned error:", data)
            return None

        return {
            "lat": data["lat"],
            "lon": data["lon"],
            "city": data["city"],
            "country": data["country"]
        }

    except Exception as e:
        print("Error fetching location:", e)
        return None


def get_weather(lat, lon):
    """
    Získá počasí z OpenWeatherMap.
    Vrací dict s teplotou, popisem, vlhkostí atd.
    """
    try:
        url = f"{WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=cz"
        response = urequests.get(url)
        data = response.json()
        response.close()

        # Ověření, že API vrátilo validní data
        if "main" not in data or "weather" not in data:
            print("Invalid weather data:", data)
            return None

        return {
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind": data["wind"]["speed"]
        }

    except Exception as e:
        print("Error fetching weather:", e)
        return None


def get_weather_with_location():
    """
    Kombinovaná funkce:
    - zjistí lokaci
    - stáhne počasí
    Vrací tuple (location, weather)
    """
    location = get_location()
    if not location:
        return None, None

    weather = get_weather(location["lat"], location["lon"])
    return location, weather
