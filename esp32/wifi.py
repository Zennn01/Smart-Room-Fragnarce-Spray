import network

def connect():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='SmartFragrance', password='12345678')
    
    # Configure IP
    ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))
    
    print('WiFi AP Active')
    print('IP Configuration:', ap.ifconfig())
    return ap
