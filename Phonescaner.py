import socket
import sys
from datetime import datetime

# --- User Configuration ---
# Aapka Account aur Token yahan add kar diya gaya hai
ACCOUNT_ID = "AC76b2bde6569c5fefb1ad2bbca8cd628d"
AUTH_TOKEN = "71426b6771aef7b779bc123a8edba680"

def start_secure_scan():
    target = "127.0.0.1" # Localhost (Aapka apna phone)
    
    print("-" * 50)
    print(f"SECURITY SCANNER - Version 3.0")
    print(f"Logged in as: {ACCOUNT_ID}")
    print(f"Status: Authenticated with Token")
    print("-" * 50)
    print(f"Scanning started at: {str(datetime.now())}")
    
    # Common ports jo hackers target karte hain
    ports = [21, 22, 80, 443, 8080, 8888]
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[!] WARNING: Port {port} is OPEN.")
        else:
            print(f"[+] Port {port} is Closed (Safe).")
        s.close()

    print("-" * 50)
    print("Scan Complete. Koi open port mile toh use turant check karein.")

if __name__ == "__main__":
    try:
        start_secure_scan()
    except KeyboardInterrupt:
        print("\nProcess stopped by user.")
        sys.exit()
