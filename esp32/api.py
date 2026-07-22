import time
import relay
import uasyncio as asyncio

state = {
    "device_name": "ESP32-SmartFragrance",
    "mode": "manual", # "manual" or "automatic"
    "duration": 3, # seconds
    "schedule": {
        "start": "08:00",
        "end": "20:00",
        "interval": 60 # minutes
    },
    "history": [],
    "last_auto_spray_time": 0 # timestamp of last auto spray
}

# Real time is kept by tracking a time offset since we rely on the browser to send us the current timestamp.
# We will use time.time() combined with an offset.
time_offset = 0

def update_time_offset(browser_timestamp_sec):
    global time_offset
    current_uptime = time.time()
    time_offset = browser_timestamp_sec - current_uptime

def get_current_timestamp():
    return int(time.time() + time_offset)

def format_time(timestamp):
    # MicroPython time.localtime() returns (year, month, mday, hour, minute, second, weekday, yearday)
    t = time.localtime(timestamp)
    return "{:02d}:{:02d}".format(t[3], t[4])

def format_date(timestamp):
    t = time.localtime(timestamp)
    return "{:04d}-{:02d}-{:02d}".format(t[0], t[1], t[2])

def add_history(mode, duration):
    now = get_current_timestamp()
    date_str = format_date(now)
    time_str = format_time(now)
    
    record = {
        "date": date_str,
        "time": time_str,
        "mode": mode,
        "duration": duration
    }
    
    state["history"].insert(0, record)
    if len(state["history"]) > 10:
        state["history"].pop()

async def trigger_spray(mode):
    if relay.is_spraying:
        return False
    duration = state["duration"]
    add_history(mode, duration)
    asyncio.create_task(relay.spray_async(duration))
    return True

def get_status():
    import network
    import os
    ap = network.WLAN(network.AP_IF)
    ip = ap.ifconfig()[0] if ap.active() else "Unknown"
    
    try:
        rssi = "N/A" # AP mode doesn't have an RSSI to a router
    except:
        rssi = "N/A"
        
    fw_version = os.uname().release
    
    return {
        "status": "Ready" if not relay.is_spraying else "Spraying",
        "connection": "WiFi Connected",
        "device_name": state["device_name"],
        "ip_address": ip,
        "rssi": rssi,
        "version": fw_version,
        "mode": state["mode"],
        "duration": state["duration"],
        "relay_status": relay.get_status(),
        "schedule": state["schedule"],
        "history": state["history"]
    }

async def auto_spray_loop():
    while True:
        await asyncio.sleep(60) # Check every minute
        
        if state["mode"] != "automatic":
            continue
            
        now = get_current_timestamp()
        t = time.localtime(now)
        current_hour = t[3]
        current_min = t[4]
        
        start_time = state["schedule"]["start"].split(":")
        end_time = state["schedule"]["end"].split(":")
        
        start_hour, start_min = int(start_time[0]), int(start_time[1])
        end_hour, end_min = int(end_time[0]), int(end_time[1])
        
        current_minutes = current_hour * 60 + current_min
        start_minutes = start_hour * 60 + start_min
        end_minutes = end_hour * 60 + end_min
        
        # Check if current time is within schedule
        if start_minutes <= current_minutes <= end_minutes:
            interval = state["schedule"]["interval"] * 60 # in seconds
            
            # If never sprayed, or interval has passed
            if state["last_auto_spray_time"] == 0 or (now - state["last_auto_spray_time"]) >= interval:
                success = await trigger_spray("Automatic Spray")
                if success:
                    state["last_auto_spray_time"] = now
