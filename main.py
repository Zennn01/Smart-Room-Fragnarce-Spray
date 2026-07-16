import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None  # tetap bisa dijalankan untuk keperluan demo tampilan


APP_NAME = "Smart Spray Controller"
BG = "#EEF3F2"
CARD = "#FFFFFF"
NAVY = "#183B4E"
GREEN = "#3D8D7A"
GREEN_HOVER = "#2f6f60"
GREY = "#555555"
DANGER = "#B4654A"

# Kredensial sederhana untuk sistem login (sesuai materi autentikasi)
VALID_USERNAME = "admin"
VALID_PASSWORD = "kost123"


class SmartSprayApp(tk.Tk):
    def __init__(self, demo=False):
        super().__init__()
        self.demo = demo
        self.title(APP_NAME)
        self.geometry("560x640")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.esp32_ip = tk.StringVar(value="192.168.1.25" if demo else "")
        self.connected = tk.BooleanVar(value=demo)
        self.schedule_active = tk.BooleanVar(value=False)
        self.schedule_interval = tk.StringVar(value="15 menit")
        self.history = []

        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (LoginFrame, DashboardFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        if demo:
            self._load_demo_data()
            self.show_frame(DashboardFrame)
        else:
            self.show_frame(LoginFrame)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        if frame_class is DashboardFrame:
            frame.refresh()

    def _load_demo_data(self):
        now = datetime.now()
        self.history = [
            ("08:12:03", "Semprot 2 detik"),
            ("08:45:10", "Semprot 1 detik"),
            ("10:00:00", "Jadwal otomatis - Semprot 2 detik"),
            ("12:30:44", "Matikan pompa (manual)"),
        ]

    # ---------------- Komunikasi ke ESP32 ----------------
    def kirim_perintah(self, endpoint):
        """Mengirim HTTP GET ke ESP32, mis. /semprot1, /semprot2, /semprot3, /mati"""
        ip = self.esp32_ip.get().strip()
        if not ip:
            messagebox.showwarning(APP_NAME, "Alamat IP ESP32 belum diisi.")
            return

        label_map = {
            "/semprot1": "Semprot 1 detik",
            "/semprot2": "Semprot 2 detik",
            "/semprot3": "Semprot 3 detik",
            "/mati": "Matikan pompa (manual)",
        }
        aksi = label_map.get(endpoint, endpoint)

        def worker():
            ok = self.demo  # dalam mode demo anggap selalu berhasil
            if requests is not None and not self.demo:
                try:
                    requests.get(f"http://{ip}{endpoint}", timeout=3)
                    ok = True
                except Exception:
                    ok = False
            timestamp = datetime.now().strftime("%H:%M:%S")
            if ok:
                self.history.insert(0, (timestamp, aksi))
            else:
                self.history.insert(0, (timestamp, f"Gagal mengirim: {aksi}"))
            self.after(0, lambda: self.frames[DashboardFrame].refresh())

        threading.Thread(target=worker, daemon=True).start()


class LoginFrame(tk.Frame):
    def __init__(self, parent, app: SmartSprayApp):
        super().__init__(parent, bg=BG)
        self.app = app

        card = tk.Frame(self, bg=CARD, padx=35, pady=35, highlightbackground="#dddddd", highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="🌸", font=("Arial", 32), bg=CARD).pack(pady=(0, 4))
        tk.Label(card, text=APP_NAME, font=("Arial", 18, "bold"), fg=NAVY, bg=CARD).pack()
        tk.Label(card, text="Kontrol Smart Room Fragrance Spray dari Laptop",
                 font=("Arial", 10), fg=GREY, bg=CARD).pack(pady=(0, 20))

        tk.Label(card, text="Username", font=("Arial", 10), bg=CARD, anchor="w").pack(fill="x")
        self.username_entry = ttk.Entry(card, width=30)
        self.username_entry.pack(pady=(2, 12))

        tk.Label(card, text="Password", font=("Arial", 10), bg=CARD, anchor="w").pack(fill="x")
        self.password_entry = ttk.Entry(card, width=30, show="*")
        self.password_entry.pack(pady=(2, 4))

        self.error_label = tk.Label(card, text="", font=("Arial", 9), fg=DANGER, bg=CARD)
        self.error_label.pack(pady=(0, 10))

        login_btn = tk.Button(card, text="Masuk", font=("Arial", 11, "bold"), bg=GREEN, fg="white",
                               activebackground=GREEN_HOVER, activeforeground="white",
                               relief="flat", width=26, pady=8, command=self.do_login)
        login_btn.pack()

        tk.Label(card, text="Default: admin / kost123", font=("Arial", 8), fg="#999999", bg=CARD).pack(pady=(10, 0))

    def do_login(self):
        u = self.username_entry.get().strip()
        p = self.password_entry.get().strip()
        if u == VALID_USERNAME and p == VALID_PASSWORD:
            self.error_label.config(text="")
            self.app.show_frame(DashboardFrame)
        else:
            self.error_label.config(text="Username atau password salah.")


class DashboardFrame(tk.Frame):
    def __init__(self, parent, app: SmartSprayApp):
        super().__init__(parent, bg=BG)
        self.app = app

        header = tk.Frame(self, bg=NAVY, height=70)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text=APP_NAME, font=("Arial", 15, "bold"), fg="white", bg=NAVY).pack(side="left", padx=18)
        self.clock_label = tk.Label(header, text="--:--:--", font=("Consolas", 15, "bold"), fg="white", bg=NAVY)
        self.clock_label.pack(side="right", padx=18)
        self.update_clock()

        body = tk.Frame(self, bg=BG, padx=18, pady=14)
        body.pack(fill="both", expand=True)

        # Panel koneksi
        conn_card = tk.LabelFrame(body, text=" Koneksi Perangkat ", font=("Arial", 10, "bold"),
                                   bg=CARD, fg=NAVY, padx=12, pady=10)
        conn_card.pack(fill="x", pady=(0, 10))
        row = tk.Frame(conn_card, bg=CARD)
        row.pack(fill="x")
        tk.Label(row, text="IP ESP32:", bg=CARD, font=("Arial", 9)).pack(side="left")
        self.ip_entry = ttk.Entry(row, textvariable=self.app.esp32_ip, width=18)
        self.ip_entry.pack(side="left", padx=6)
        tk.Button(row, text="Sambungkan", bg=NAVY, fg="white", relief="flat",
                  font=("Arial", 9), command=self.connect).pack(side="left", padx=6)
        self.status_dot = tk.Label(row, text="●", font=("Arial", 12),
                                    fg=(GREEN if self.app.connected.get() else DANGER), bg=CARD)
        self.status_dot.pack(side="right")
        self.status_text = tk.Label(row, text=("Terhubung" if self.app.connected.get() else "Belum terhubung"),
                                     bg=CARD, font=("Arial", 9))
        self.status_text.pack(side="right", padx=(0, 6))

        # Panel kontrol semprot
        ctrl_card = tk.LabelFrame(body, text=" Kontrol Semprot ", font=("Arial", 10, "bold"),
                                   bg=CARD, fg=NAVY, padx=12, pady=10)
        ctrl_card.pack(fill="x", pady=(0, 10))
        btn_row = tk.Frame(ctrl_card, bg=CARD)
        btn_row.pack(fill="x")
        for label, ep in [("Semprot 1s", "/semprot1"), ("Semprot 2s", "/semprot2"), ("Semprot 3s", "/semprot3")]:
            tk.Button(btn_row, text=label, bg=GREEN, fg="white", relief="flat", font=("Arial", 9, "bold"),
                      width=12, pady=8, command=lambda e=ep: self.app.kirim_perintah(e)).pack(side="left", padx=4)
        tk.Button(ctrl_card, text="Matikan Pompa", bg="#444444", fg="white", relief="flat",
                  font=("Arial", 9, "bold"), pady=8, command=lambda: self.app.kirim_perintah("/mati")).pack(
            fill="x", pady=(8, 0))

        # Panel jadwal otomatis
        sched_card = tk.LabelFrame(body, text=" Jadwal Otomatis ", font=("Arial", 10, "bold"),
                                    bg=CARD, fg=NAVY, padx=12, pady=10)
        sched_card.pack(fill="x", pady=(0, 10))
        srow = tk.Frame(sched_card, bg=CARD)
        srow.pack(fill="x")
        tk.Checkbutton(srow, text="Aktifkan", variable=self.app.schedule_active, bg=CARD,
                        font=("Arial", 9)).pack(side="left")
        tk.Label(srow, text="Interval:", bg=CARD, font=("Arial", 9)).pack(side="left", padx=(12, 4))
        ttk.Combobox(srow, textvariable=self.app.schedule_interval, width=10, state="readonly",
                     values=["5 menit", "10 menit", "15 menit", "30 menit", "60 menit"]).pack(side="left")

        # Panel riwayat
        hist_card = tk.LabelFrame(body, text=" Riwayat Penyemprotan ", font=("Arial", 10, "bold"),
                                   bg=CARD, fg=NAVY, padx=12, pady=10)
        hist_card.pack(fill="both", expand=True)
        columns = ("waktu", "aksi")
        self.tree = ttk.Treeview(hist_card, columns=columns, show="headings", height=8)
        self.tree.heading("waktu", text="Waktu")
        self.tree.heading("aksi", text="Aksi")
        self.tree.column("waktu", width=90, anchor="center")
        self.tree.column("aksi", width=280, anchor="w")
        self.tree.pack(fill="both", expand=True)

        tk.Button(body, text="Keluar (Logout)", bg=BG, fg=GREY, relief="flat",
                  font=("Arial", 8, "underline"), command=self.logout).pack(anchor="e", pady=(8, 0))

    def connect(self):
        ip = self.app.esp32_ip.get().strip()
        if ip:
            self.app.connected.set(True)
            self.status_dot.config(fg=GREEN)
            self.status_text.config(text="Terhubung")
        else:
            messagebox.showwarning(APP_NAME, "Isi alamat IP ESP32 terlebih dahulu.")

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for waktu, aksi in self.app.history:
            self.tree.insert("", "end", values=(waktu, aksi))

    def update_clock(self):
        self.clock_label.config(text=datetime.now().strftime("%H:%M:%S"))
        self.after(1000, self.update_clock)

    def logout(self):
        self.app.show_frame(LoginFrame)


if __name__ == "__main__":
    demo_mode = "--demo" in sys.argv
    app = SmartSprayApp(demo=demo_mode)
    app.mainloop()
