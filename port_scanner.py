import socket

print("--- Port Scanner ---")
target = input("Enter IP address (e.g., 127.0.0.1): ")

print(f"Scanning {target}...")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
        
    s.close()

print("Scanning finished.")
