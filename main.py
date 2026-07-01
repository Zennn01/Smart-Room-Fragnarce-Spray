import network
import socket
import time
from machine import Pin

# =========================
# KONFIGURASI WIFI
# =========================
SSID = "NAMA_WIFI"
PASSWORD = "PASSWORD_WIFI"

# =========================
# KONFIGURASI PIN
# =========================
RELAY_PIN = 26
LED_PIN = 2

relay = Pin(RELAY_PIN, Pin.OUT)
led = Pin(LED_PIN, Pin.OUT)

# Banyak relay aktif ketika LOW.
# Kalau relay kamu kebalik, ubah bagian ini.
RELAY_ON = 0
RELAY_OFF = 1

relay.value(RELAY_OFF)
led.value(0)


# =========================
# FUNGSI KONEKSI WIFI
# =========================
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)

    print("Menghubungkan ke WiFi...")

    while not wifi.isconnected():
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

    ip = wifi.ifconfig()[0]
    print("WiFi terhubung")
    print("IP ESP32:", ip)

    led.value(1)
    return ip


# =========================
# FUNGSI SEMPROT
# =========================
def semprot(detik):
    print("Pompa aktif selama", detik, "detik")

    relay.value(RELAY_ON)
    led.value(1)

    time.sleep(detik)

    relay.value(RELAY_OFF)
    led.value(0)

    print("Pompa mati")


# =========================
# HALAMAN WEB
# =========================
def halaman_web():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Room Fragrance Spray</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef3f2;
                text-align: center;
                padding: 30px;
            }
            .card {
                background: white;
                padding: 25px;
                border-radius: 18px;
                max-width: 420px;
                margin: auto;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            h1 {
                color: #183B4E;
                font-size: 24px;
            }
            p {
                color: #555;
            }
            button {
                width: 100%;
                padding: 16px;
                margin: 10px 0;
                border: none;
                border-radius: 12px;
                background: #3D8D7A;
                color: white;
                font-size: 18px;
                cursor: pointer;
            }
            button:hover {
                background: #2f6f60;
            }
            .off {
                background: #444;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Smart Room Fragrance Spray</h1>
            <p>Kontrol semprot pewangi ruangan berbasis ESP32</p>

            <a href="/semprot1"><button>Semprot 1 Detik</button></a>
            <a href="/semprot2"><button>Semprot 2 Detik</button></a>
            <a href="/semprot3"><button>Semprot 3 Detik</button></a>
            <a href="/mati"><button class="off">Matikan Pompa</button></a>

            <p>Status: alat aktif</p>
        </div>
    </body>
    </html>
    """
    return html


# =========================
# PROGRAM UTAMA
# =========================
ip = connect_wifi()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 80))
server.listen(5)

print("Web server aktif")
print("Buka di browser: http://" + ip)

while True:
    conn, addr = server.accept()
    print("Terhubung dari:", addr)

    request = conn.recv(1024)
    request = str(request)

    print("Request:", request)

    if "/semprot1" in request:
        semprot(1)

    elif "/semprot2" in request:
        semprot(2)

    elif "/semprot3" in request:
        semprot(3)

    elif "/mati" in request:
        relay.value(RELAY_OFF)
        led.value(0)
        print("Pompa dimatikan manual")

    response = halaman_web()

    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-Type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()
