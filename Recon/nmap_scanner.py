import subprocess

target = input("Enter target IP (use scanme.nmap.org to test): ")
print("Scanning", target, "...")
result = subprocess.run(['nmap', '-sV', '-T4', target], capture_output=True, text=True)
print(result.stdout)

# ╔══════════════════════════════════════════════════════════╗
#   Smart Nmap Scanner – Week 1 Tool (save as nmap_scanner.py)
#   CompTIA Security+ certified | AI-ready ethical hacking
# ╚══════════════════════════════════════════════════════════╝

import subprocess
import sys
import time

print("""
   █▀▄▀█ █▀█ █▄░█ █▀▄▀█ █▀█ █▄░█ █▀▀ █▀█
   █░▀░█ █▄█ █░▀█ █░▀░█ █▄█ █░▀█ ██▄ █▄█  v1.0
""")

# Legal banner – always show this
print("⚠️  ONLY scan targets you own or have written permission for!")
print("   Example legal target → scanme.nmap.org (allowed by Nmap.org)\n")

target = input("Enter target IP or domain (e.g. scanme.nmap.org): ").strip()

if not target:
    print("No target entered. Exiting.")
    sys.exit()

print(f"\nStarting aggressive scan on {target}...")
print("This may take 1–3 minutes...\n")
time.sleep(2)

# The actual Nmap command (fast + version detection + OS guess)
command = [
    "nmap",
    "-sS",        # SYN scan (stealthy)
    "-sV",        # Version detection
    "-O",         # OS detection
    "-T4",        # Faster timing
    "-A",         # Aggressive (scripts, traceroute, etc.)
    "--open",     # Only show open ports
    target
]

try:
    result = subprocess.run(command, capture_output=True, text=True, timeout=600)
    
    print("═" * 60)
    print("SCAN COMPLETE – RESULTS")
    print("═" * 60)
    print(result.stdout)
    
    # Save report automatically
    filename = f"nmap_report_{target}_{time.strftime('%Y%m%d-%H%M')}.txt"
    with open(filename, "w") as f:
        f.write(result.stdout)
    print(f"\nReport saved as → {filename}")

except KeyboardInterrupt:
    print("\nScan cancelled by user.")
except Exception as e:
    print(f"Error: {e}")
    print("Tip: Make sure Nmap is installed → https://nmap.org/download.html")

print("\nDone! Share this repo and start charging for scans ")
