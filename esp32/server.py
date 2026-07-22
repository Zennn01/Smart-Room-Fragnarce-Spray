import uasyncio as asyncio
import json
import api

# Content types for static files
CONTENT_TYPES = {
    "html": "text/html",
    "css": "text/css",
    "js": "application/javascript",
    "png": "image/png",
    "jpg": "image/jpeg",
    "ico": "image/x-icon"
}

def get_content_type(filename):
    ext = filename.split(".")[-1]
    return CONTENT_TYPES.get(ext, "text/plain")

async def send_response(writer, status_code, content_type, body):
    response = f"HTTP/1.1 {status_code} OK\r\nContent-Type: {content_type}\r\nConnection: close\r\n\r\n"
    await writer.awrite(response.encode('utf-8'))
    if type(body) == str:
        await writer.awrite(body.encode('utf-8'))
    else:
        await writer.awrite(body)
    await writer.aclose()

async def send_file(writer, filename):
    try:
        with open("data/" + filename, "rb") as f:
            content_type = get_content_type(filename)
            response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nConnection: close\r\n\r\n"
            await writer.awrite(response.encode('utf-8'))
            
            # Read and send in chunks
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                await writer.awrite(chunk)
    except Exception as e:
        await send_response(writer, 404, "text/plain", "404 Not Found")
    finally:
        await writer.aclose()

def parse_request(req_str):
    try:
        lines = req_str.split("\r\n")
        method, path, _ = lines[0].split(" ")
        
        # Parse body if POST
        body = ""
        if method == "POST":
            # find empty line separating headers and body
            for i, line in enumerate(lines):
                if line == "":
                    body = "\r\n".join(lines[i+1:])
                    break
                    
        return method, path, body
    except:
        return None, None, None

async def handle_client(reader, writer):
    try:
        request_line = await reader.read(1024)
        req_str = request_line.decode('utf-8')
        if not req_str:
            await writer.aclose()
            return
            
        method, path, body = parse_request(req_str)
        if not method:
            await writer.aclose()
            return
            
        print(f"Request: {method} {path}")
        
        # API Routes
        if path.startswith("/api/"):
            if method == "GET" and path == "/api/status":
                data = json.dumps(api.get_status())
                await send_response(writer, 200, "application/json", data)
                return
                
            elif method == "POST":
                try:
                    payload = json.loads(body) if body else {}
                except:
                    payload = {}
                    
                if path == "/api/spray":
                    success = await api.trigger_spray("Manual Spray")
                    await send_response(writer, 200, "application/json", json.dumps({"success": success}))
                    return
                elif path == "/api/mode":
                    api.state["mode"] = payload.get("mode", api.state["mode"])
                    await send_response(writer, 200, "application/json", json.dumps({"success": True}))
                    return
                elif path == "/api/duration":
                    api.state["duration"] = int(payload.get("duration", api.state["duration"]))
                    await send_response(writer, 200, "application/json", json.dumps({"success": True}))
                    return
                elif path == "/api/schedule":
                    api.state["schedule"]["start"] = payload.get("start", api.state["schedule"]["start"])
                    api.state["schedule"]["end"] = payload.get("end", api.state["schedule"]["end"])
                    api.state["schedule"]["interval"] = int(payload.get("interval", api.state["schedule"]["interval"]))
                    await send_response(writer, 200, "application/json", json.dumps({"success": True}))
                    return
                elif path == "/api/sync_time":
                    timestamp = payload.get("timestamp", 0)
                    if timestamp > 0:
                        api.update_time_offset(timestamp)
                    await send_response(writer, 200, "application/json", json.dumps({"success": True}))
                    return
                    
            await send_response(writer, 404, "application/json", json.dumps({"error": "Endpoint not found"}))
            return
            
        # Static file routing
        if method == "GET":
            if path == "/":
                path = "/index.html"
            
            # Remove leading slash
            filename = path[1:]
            await send_file(writer, filename)
            return
            
    except Exception as e:
        print("Server error:", e)
        try:
            await writer.aclose()
        except:
            pass

async def start_server():
    server = await asyncio.start_server(handle_client, "0.0.0.0", 80)
    print("Web server started on port 80")
    while True:
        await asyncio.sleep(3600)
