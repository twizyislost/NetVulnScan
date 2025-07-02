# CLI script - user input, program entry

from scanner import ports

def main():
        target = input("Enter target IP or hostname: ").strip()
        ports.scan_range(target, 1, 1024)

if __name__ == "__main__":
    main()