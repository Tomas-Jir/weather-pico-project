import network
import time
import ujson

def load_config():
    """Načte konfiguraci z CONFIGURATION.txt"""
    with open("CONFIGURATION.txt", "r") as f:
        return ujson.loads(f.read())

config = load_config()
SSID = config["wifi_ssid"]
PASSWORD = config["wifi_password"]

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def connect_wifi():
    """Připojí Pico W k WiFi, opakuje pokusy dokud se nepřipojí."""
    if wlan.isconnected():
        return True

    print("Connecting to WiFi...")
    wlan.connect(SSID)

    timeout = 20  # 20 sekund na připojení
    while timeout > 0:
        if wlan.isconnected():
            print("Connected:", wlan.ifconfig())
            return True
        time.sleep(1)
        timeout -= 1

    print("Failed to connect to WiFi")
    return False

def ensure_connection():
    """Zkontroluje připojení a v případě výpadku se znovu připojí."""
    if not wlan.isconnected():
        print("WiFi lost, reconnecting...")
        connect_wifi()

def get_ip():
    """Vrátí IP adresu zařízení."""
    if wlan.isconnected():
        return wlan.ifconfig()[0]
    return None
