# Contains port scanning functions (scan_port, scan range, etc.)

def scan_range(target, start_port, end_port):
        target = input("Enter target IP or hostname: ").strip()
        ports.scan_range(target, 1, 1024)

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.settimeout(0.5)

result = sock.connect_ex((target, port))

if result == 0:
    print(f"[+] Port {port} is OPEN")

sock.close()
