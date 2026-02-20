# \# Weather Station - Raspberry Pi Pico W

# 

# Projekt meteostanice postavený na platformě Raspberry Pi Pico W. Program zjišťuje aktuální geologickou polohu podle veřejné IP adresy, stahuje data o počasí přes OpenWeatherMap API a zobrazuje je spolu s aktuálním časem (synchronizovaným přes NTP) na LCD displeji.

# 

# \## Funkcionalita

# \- Automatické připojení k WiFi po startu i při výpadku.

# \- Získání polohy (město, souřadnice) přes IP API.

# \- Aktuální počasí aktualizované každých 10 minut.

# \- Zobrazení času ve formátu `HH:MM:SS`.

# \- Ošetření chyb při výpadku API nebo sítě.

# 

# \## Hardwarové zapojení

# \- \*\*Zařízení:\*\* Raspberry Pi Pico W

# \- \*\*Displej:\*\* LCD 16x2 s I2C převodníkem

# \- \*\*Zapojení pinů:\*\*

# &nbsp; - VCC -> 3.3V (nebo 5V podle typu LCD)

# &nbsp; - GND -> GND

# &nbsp; - SDA -> GP0 (pin 1)

# &nbsp; - SCL -> GP1 (pin 2)

# 

# \## Instalace a zprovoznění

# 1\. Zkopírujte (klonujte) tento repozitář do svého počítače.

# 2\. Nahrajte soubory `main.py`, `wifi.py`, `weather.py`, `lcd.py` a `CONFIGURATION.txt` do Raspberry Pi Pico W (např. pomocí prostředí Thonny).

# 3\. \*\*Důležité:\*\* Ujistěte se, že máte v kořenovém adresáři soubor `.gitignore`, aby se váš `CONFIGURATION.txt` nedostal na veřejný GitHub.

# 

# \## Konfigurace

# Program využívá soubor `CONFIGURATION.txt` ve formátu JSON pro uložení citlivých údajů. Před spuštěním upravte tento soubor:

# 

# ```json

# {

# &nbsp;   "wifi\_ssid": "VASE\_WIFI\_NAZEV",

# &nbsp;   "wifi\_password": "VASE\_HESLO",

# &nbsp;   "api\_key": "VAS\_OPENWEATHER\_API\_KLIC"

# }

