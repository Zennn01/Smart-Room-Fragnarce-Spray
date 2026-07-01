# Smart Room Fragrance Spray Berbasis IoT untuk Anak Kost

## 1. Deskripsi Project

Smart Room Fragrance Spray adalah alat penyemprot pewangi ruangan otomatis berbasis IoT yang dibuat untuk kebutuhan anak kost. Alat ini dirancang agar pengguna dapat menyemprotkan pewangi ruangan secara otomatis melalui perangkat seperti HP atau laptop yang terhubung ke jaringan WiFi.

Berbeda dengan pengharum ruangan otomatis yang biasanya memakai kaleng aerosol atau gas, alat ini menggunakan cairan pewangi isi ulang. Cairan pewangi dapat ditaruh di dalam wadah atau botol kecil, lalu dipompa menggunakan pompa mini DC 5V menuju nozzle spray agar keluar dalam bentuk semprotan halus.

Project ini dibuat sebagai prototype awal yang sederhana, murah, dan aman karena menggunakan sumber daya USB 5V, bukan langsung dari listrik AC 220V.

---

## 2. Latar Belakang Ide

Anak kost biasanya membutuhkan ruangan yang nyaman, bersih, dan wangi. Namun, tidak semua anak kost memiliki alat pengharum ruangan otomatis karena kebanyakan produk yang tersedia di pasaran menggunakan aerosol, gas, atau refill khusus yang harganya bisa lebih mahal.

Dari masalah tersebut, dibuatlah ide alat Smart Room Fragrance Spray berbasis IoT dengan sistem cairan isi ulang. Dengan alat ini, pengguna dapat memakai cairan pewangi yang lebih fleksibel, seperti pewangi ruangan cair atau campuran pewangi dengan air, lalu alat akan menyemprotkannya secara otomatis menggunakan pompa mini.

Selain itu, alat ini juga dapat dikembangkan dengan fitur tambahan seperti jadwal semprot otomatis, kontrol melalui website, perintah suara, sensor cairan, dan riwayat penggunaan.

---

## 3. Tujuan Project

Tujuan dari project ini adalah:

1. Membuat alat penyemprot pewangi ruangan otomatis berbasis ESP32.
2. Membuat sistem pewangi ruangan yang tidak bergantung pada aerosol atau gas.
3. Membuat alat yang dapat dikontrol melalui HP atau laptop.
4. Menggunakan cairan pewangi isi ulang agar lebih hemat dan fleksibel.
5. Membuat prototype IoT sederhana yang cocok untuk kebutuhan anak kost.
6. Menggunakan sumber daya USB 5V agar lebih aman dan mudah digunakan.

---

## 4. Konsep Cara Kerja

Konsep utama alat ini adalah ESP32 menerima perintah dari pengguna, lalu mengaktifkan relay untuk menyalakan pompa mini. Pompa akan menarik cairan pewangi dari tangki atau botol kecil, kemudian mendorong cairan tersebut menuju nozzle spray. Setelah itu, cairan keluar dalam bentuk semprotan halus ke ruangan.

Alur sederhana:

```text
User membuka halaman kontrol dari HP/laptop
        ↓
User menekan tombol semprot
        ↓
ESP32 menerima perintah
        ↓
Relay aktif
        ↓
Pompa mini menyala
        ↓
Cairan pewangi ditarik dari botol
        ↓
Cairan keluar melalui nozzle spray
        ↓
Ruangan menjadi wangi
```

---

## 5. Nama Project

Nama project:

```text
Smart Room Fragrance Spray Berbasis IoT untuk Anak Kost
```

Nama alternatif:

```text
Smart Room Fragrance Spray Berbasis IoT dengan Sistem Pewangi Cair Isi Ulang
```

---

## 6. Keunggulan Ide

Keunggulan dari alat ini adalah:

1. Tidak menggunakan aerosol atau gas.
2. Menggunakan cairan pewangi isi ulang.
3. Lebih hemat karena cairan bisa dicampur air.
4. Cocok untuk kamar kost.
5. Aman untuk prototype karena menggunakan USB 5V.
6. Bisa dikontrol dari HP atau laptop.
7. Dapat dikembangkan dengan fitur IoT dan AI.
8. Komponen mudah dicari dan harganya murah.
9. Bisa menjadi project IoT sederhana namun bermanfaat.

---

## 7. Daftar Alat dan Komponen

Berikut alat dan komponen yang digunakan:

| No | Nama Alat                                                             |     Harga |
| -- | --------------------------------------------------------------------- | --------: |
| 1  | ESP32-S3 DevKitC-1 N16R8 Type-C dengan PSRAM 16MB                     | Rp100.000 |
| 2  | Purifier Water Pump Diaphragm Self-Priming DC 5V Dinamo 130           |  Rp16.000 |
| 3  | SPRAYER SET MIST NOZZLE ABU ABU SPRINKLER                             |     Rp920 |
| 4  | Selang silikon kecil                                                  |  Rp10.000 |
| 5  | Tangki cairan kecil / botol bekas                                     |       Rp0 |
| 6  | Relay 5V 4 Channel Module High / Low Level Trigger Opto Isolation 4CH |     Rp400 |
| 7  | Female to Female Kabel Jumper                                         |  Rp15.000 |
| 8  | Kabel USB                                                             |   Rp6.000 |
| 9  | Adaptor HP 5V 2A                                                      |  Rp20.000 |
| 10 | Breadboard untuk uji coba awal                                        |         - |

Total biaya sementara:

```text
Rp168.320
```

Catatan: Harga dapat berubah sesuai toko dan ongkos kirim. Untuk tangki cairan, sementara dapat menggunakan botol kecil terlebih dahulu agar lebih hemat.

---

## 8. Fungsi Setiap Komponen

### 1. ESP32-S3 DevKitC-1

ESP32-S3 berfungsi sebagai otak utama dari alat. Board ini akan menerima perintah dari pengguna melalui jaringan WiFi, lalu mengontrol relay untuk menyalakan atau mematikan pompa.

Fungsi ESP32:

```text
- Menghubungkan alat ke WiFi
- Menjalankan program utama
- Membuat halaman kontrol sederhana
- Mengontrol relay
- Mengatur durasi pompa menyala
```

---

### 2. Pompa Mini DC 5V

Pompa mini digunakan untuk menarik cairan pewangi dari botol atau tangki kecil, lalu mendorongnya ke nozzle spray.

Fungsi pompa:

```text
- Menarik cairan dari tangki
- Mengalirkan cairan melalui selang
- Mendorong cairan menuju nozzle
```

Pompa yang digunakan adalah jenis diaphragm self-priming DC 5V, sehingga cocok untuk cairan dan dapat bekerja menggunakan adaptor USB 5V.

---

### 3. Mist Nozzle Sprayer

Nozzle berfungsi sebagai ujung keluarnya cairan. Komponen ini membantu membuat cairan keluar dalam bentuk semprotan yang lebih halus.

Fungsi nozzle:

```text
- Mengubah aliran cairan menjadi semprotan
- Menyebarkan pewangi ke udara
- Membuat hasil semprot lebih rapi
```

---

### 4. Selang Silikon Kecil

Selang digunakan sebagai jalur cairan dari botol ke pompa, lalu dari pompa ke nozzle.

Alur selang:

```text
Botol cairan → Pompa → Nozzle
```

---

### 5. Botol atau Tangki Cairan

Botol digunakan sebagai tempat penyimpanan cairan pewangi. Pada prototype awal, botol bekas kecil bisa digunakan terlebih dahulu agar lebih hemat.

Isi cairan dapat berupa:

```text
- Air + pewangi ruangan cair
- Air + bibit parfum laundry
- Air + essential oil khusus diffuser
```

Catatan: Jangan menggunakan cairan yang terlalu kental karena dapat membuat selang, pompa, atau nozzle cepat kotor dan mampet.

---

### 6. Relay 5V 4 Channel

Relay digunakan sebagai saklar elektronik untuk menghidupkan dan mematikan pompa. ESP32 tidak disarankan langsung menyalakan pompa dari pin GPIO, sehingga relay digunakan sebagai penghubung.

Fungsi relay:

```text
- Menerima sinyal dari ESP32
- Menyalakan pompa
- Mematikan pompa
- Melindungi ESP32 dari beban pompa secara langsung
```

Relay 4 channel sebenarnya lebih dari cukup karena prototype awal hanya membutuhkan 1 channel untuk pompa. Sisa channel dapat dipakai untuk pengembangan, misalnya kipas kecil, LED, atau fitur tambahan lain.

---

### 7. Kabel Jumper Female to Female

Kabel jumper digunakan untuk menghubungkan ESP32 ke relay dan komponen lainnya.

Contoh koneksi:

```text
GPIO ESP32 → IN Relay
GND ESP32 → GND Relay
5V/VIN ESP32 → VCC Relay
```

---

### 8. Kabel USB

Kabel USB digunakan untuk:

```text
- Memberi daya ke ESP32
- Mengupload program ke ESP32
- Menghubungkan ESP32 ke laptop saat proses testing
```

---

### 9. Adaptor HP 5V 2A

Adaptor HP digunakan sebagai sumber daya utama alat. Output 5V 2A cukup untuk menyalakan ESP32 dan pompa mini 5V.

Kelebihan menggunakan adaptor USB:

```text
- Lebih aman
- Mudah digunakan
- Tidak perlu langsung menyentuh listrik 220V
- Cocok untuk prototype awal
```

---

### 10. Breadboard

Breadboard digunakan untuk merakit dan menguji rangkaian sementara sebelum dibuat lebih rapi.

Fungsi breadboard:

```text
- Memudahkan uji coba rangkaian
- Tidak perlu solder di awal
- Cocok untuk prototype
```

---

## 9. Rancangan Alur Hardware

Alur daya listrik:

```text
Adaptor HP 5V 2A
        ↓
ESP32
        ↓
Relay 5V
        ↓
Pompa Mini 5V
```

Alur cairan:

```text
Botol cairan pewangi
        ↓
Selang silikon
        ↓
Pompa mini 5V
        ↓
Selang silikon
        ↓
Mist nozzle
        ↓
Semprotan pewangi
```

Alur kontrol:

```text
HP / Laptop
        ↓
WiFi
        ↓
ESP32
        ↓
Relay aktif
        ↓
Pompa menyala
        ↓
Pewangi keluar
```

---

## 10. Rancangan Pin ESP32

Contoh pin yang digunakan:

| Komponen         | Pin ESP32 | Keterangan       |
| ---------------- | --------- | ---------------- |
| Relay IN1        | GPIO 26   | Mengontrol pompa |
| Relay VCC        | 5V / VIN  | Daya relay       |
| Relay GND        | GND       | Ground           |
| LED bawaan ESP32 | GPIO 2    | Indikator status |

Catatan: Pin dapat disesuaikan lagi tergantung board ESP32 yang digunakan.

---

## 11. Rancangan Koneksi Relay dan Pompa

Koneksi ESP32 ke relay:

```text
ESP32 GPIO 26 → IN1 Relay
ESP32 GND     → GND Relay
ESP32 5V/VIN  → VCC Relay
```

Koneksi relay ke pompa:

```text
Positif adaptor 5V → COM Relay
NO Relay           → Positif Pompa
Negatif Pompa      → Negatif adaptor 5V
```

Penjelasan:

```text
- COM adalah jalur masuk daya ke relay.
- NO adalah Normally Open, artinya pompa mati saat relay tidak aktif.
- Saat relay aktif, COM dan NO tersambung sehingga pompa menyala.
```

---

## 12. Software yang Digunakan

Software yang dapat digunakan:

```text
- MicroPython
- Thonny IDE
- Firmware MicroPython untuk ESP32
```

Alasan menggunakan MicroPython:

```text
- Sintaks mirip Python
- Lebih mudah dipahami untuk pemula
- Cocok untuk prototype IoT
- Dapat digunakan untuk mengontrol pin ESP32
- Bisa dikembangkan ke sistem berbasis web/API
```

Selain MicroPython, alat ini juga bisa dibuat menggunakan Arduino IDE dengan bahasa C++. Namun, untuk prototype awal, MicroPython lebih mudah digunakan.

---

## 13. Fitur Awal Prototype

Fitur awal yang akan dibuat:

```text
1. ESP32 terhubung ke WiFi
2. ESP32 membuat halaman web sederhana
3. User membuka IP ESP32 dari browser
4. User menekan tombol semprot
5. Relay menyala
6. Pompa aktif beberapa detik
7. Cairan keluar melalui nozzle
8. Pompa mati otomatis
```

Tombol yang tersedia pada halaman web:

```text
- Semprot 1 detik
- Semprot 2 detik
- Semprot 3 detik
- Matikan pompa
```

---

## 14. Contoh Program MicroPython

File utama:

```text
main.py
```

Kode program:

```python
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
```

---

## 15. Cara Menjalankan Program

Langkah umum menjalankan program:

```text
1. Install Thonny IDE di laptop.
2. Flash firmware MicroPython ke ESP32.
3. Hubungkan ESP32 ke laptop menggunakan kabel USB.
4. Buka Thonny IDE.
5. Pilih interpreter MicroPython ESP32.
6. Buat file main.py.
7. Masukkan kode program ke main.py.
8. Ganti NAMA_WIFI dan PASSWORD_WIFI.
9. Upload file main.py ke ESP32.
10. Jalankan ESP32.
11. Lihat IP ESP32 pada serial monitor.
12. Buka IP tersebut di browser HP atau laptop.
13. Tekan tombol semprot.
```

---

## 16. Contoh Penggunaan

Contoh penggunaan alat:

```text
1. Isi botol dengan campuran air dan pewangi cair.
2. Sambungkan selang dari botol ke pompa.
3. Sambungkan selang dari pompa ke nozzle.
4. Hubungkan ESP32 ke adaptor USB 5V 2A.
5. Tunggu ESP32 terhubung ke WiFi.
6. Buka alamat IP ESP32 di browser.
7. Tekan tombol "Semprot 2 Detik".
8. Pompa menyala dan pewangi keluar dari nozzle.
9. Pompa mati otomatis setelah 2 detik.
```

---

## 17. Campuran Cairan Pewangi

Untuk prototype awal, campuran cairan jangan terlalu kental.

Contoh campuran:

```text
Air bersih 90%
Pewangi cair 10%
```

Atau:

```text
Air bersih 95%
Essential oil / bibit parfum 5%
```

Catatan:

```text
- Jangan terlalu banyak pewangi.
- Jangan gunakan cairan terlalu kental.
- Bersihkan selang dan nozzle secara berkala.
- Jika nozzle mampet, kurangi kekentalan cairan.
```

---

## 18. Batasan Prototype

Batasan pada prototype awal:

```text
1. Belum menggunakan sensor level cairan.
2. Belum menggunakan casing permanen.
3. Belum menggunakan baterai rechargeable.
4. Kontrol masih melalui halaman web sederhana.
5. Belum menggunakan perintah suara langsung.
6. Belum ada database untuk menyimpan riwayat semprot.
```

---

## 19. Rencana Pengembangan

Project ini dapat dikembangkan dengan fitur:

```text
1. Jadwal semprot otomatis.
2. Sensor cairan hampir habis.
3. Kontrol melalui aplikasi mobile.
4. Perintah suara menggunakan HP.
5. Integrasi AI untuk perintah natural language.
6. Mode hemat cairan.
7. Riwayat penggunaan.
8. Notifikasi ke HP.
9. Casing custom menggunakan akrilik atau 3D print.
10. Power supply menggunakan baterai rechargeable atau powerbank.
```

Contoh pengembangan AI:

```text
User berkata: "Bikin kamar lebih wangi"
        ↓
Perintah diproses di HP / server
        ↓
HP / server mengirim perintah ke ESP32
        ↓
ESP32 menyalakan pompa
        ↓
Alat menyemprotkan pewangi
```

Pada konsep ini, AI tidak dijalankan langsung di ESP32 karena ESP32 memiliki keterbatasan memori dan performa. ESP32 lebih cocok menjadi alat eksekusi, sedangkan AI atau perintah suara dapat diproses melalui HP, laptop, atau server.

---

## 20. Kesimpulan

Smart Room Fragrance Spray Berbasis IoT untuk Anak Kost adalah alat penyemprot pewangi ruangan otomatis yang menggunakan ESP32, pompa mini 5V, relay, dan nozzle spray. Alat ini dibuat untuk memberikan solusi pewangi ruangan yang lebih fleksibel, murah, dan mudah digunakan.

Project ini cocok untuk anak kost karena menggunakan cairan isi ulang, tidak memakai aerosol atau gas, serta dapat dikontrol melalui HP atau laptop. Dengan sumber daya USB 5V, alat ini juga lebih aman untuk prototype awal.

Secara keseluruhan, project ini memiliki potensi untuk dikembangkan menjadi alat IoT yang lebih lengkap dengan fitur jadwal otomatis, sensor cairan, perintah suara, dan integrasi AI.
