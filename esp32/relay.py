import machine
import uasyncio as asyncio

# Relay pin (GPIO 26)
relay_pin = machine.Pin(26, machine.Pin.OUT)
relay_pin.value(0) # Default OFF (assume active HIGH, adjust if active LOW)

is_spraying = False

async def spray_async(duration_sec):
    global is_spraying
    if is_spraying:
        return False # Already spraying
    
    is_spraying = True
    relay_pin.value(1)
    print(f"Spraying for {duration_sec} seconds...")
    
    await asyncio.sleep(duration_sec)
    
    relay_pin.value(0)
    print("Spray finished.")
    is_spraying = False
    return True

def get_status():
    return "ON" if is_spraying else "OFF"
