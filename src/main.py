import time
import wifi
import weather

print("Starting system...")
wifi.connect_wifi()

while True:
    wifi.ensure_connection()

    # Pokud není připojeno, nepokračuj
    if not wifi.wlan.isconnected():
        print("Still not connected, retrying in 5 seconds...")
        time.sleep(5)
        continue

    print("\n--- Getting location ---")
    location, data = weather.get_weather_with_location()

    if location:
        print("Location:", location["city"], location["country"])
    else:
        print("Failed to get location")

    if data:
        print("Temperature:", data["temp"], "°C")
    else:
        print("Failed to get weather data")

    time.sleep(10)
