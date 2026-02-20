import time
import machine
import wifi
import weather
from lcd import Lcd_i2c

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = Lcd_i2c(i2c)

print("Starting system...")
lcd.clear()
lcd.write("Connecting WiFi")

wifi.connect_wifi()

while True:
    wifi.ensure_connection()

    if not wifi.wlan.isconnected():
        lcd.clear()
        lcd.write("WiFi Lost!")
        time.sleep(5)
        continue

    location, data = weather.get_weather_with_location()

    if location:
        # 2. Výpis na LCD místo do printu
        lcd.clear()
        lcd.set_cursor(0, 0) # První řádek
        lcd.write(location["city"])
        
        if data:
            lcd.set_cursor(0, 1) # Druhý řádek
            lcd.write(f"T:{data['temp']}C {data['description'][:10]}")
    else:
        lcd.clear()
        lcd.write("Error: No Data")

    # V zadání máš kontrolovat každých 10 minut (600 s)
    time.sleep(600)