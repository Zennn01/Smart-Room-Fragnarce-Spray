import wifi
import server
import api
import uasyncio as asyncio

def start():
    print("Starting Smart Room Fragrance System...")
    
    # 1. Initialize WiFi AP
    wifi.connect()
    
    # 2. Get event loop
    loop = asyncio.get_event_loop()
    
    # 3. Create tasks
    loop.create_task(server.start_server())
    loop.create_task(api.auto_spray_loop())
    
    # 4. Run forever
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        import relay
        relay.relay_pin.value(0) # Ensure relay is off on exit

if __name__ == "__main__":
    start()
