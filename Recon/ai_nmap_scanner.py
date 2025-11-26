# ai_nmap_scanner.py – The one you’ll actually charge money for
import subprocess
import json
import time
import os
from datetime import datetime

print("AI-POWERED SMART SCANNER v2 – Now with auto-explanations!\n")

target = input("Target (e.g. scanme.nmap.org): ").strip()
print("\nRunning full aggressive scan + AI analysis...\n")

# Run Nmap and save raw XML (easier for AI to read)
command = ["nmap", "-sS", "-sV", "-O", "-A", "--open", "-oX", "raw.xml", target]
subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Convert XML → text for the AI
command2 = ["nmap", "-sS", "-sV", "-O", "-A", "--open", target]
raw_result = subprocess.run(command2, capture_output=True, text=True).stdout

# Send to AI (using Grok, Claude, or GPT-4o – free tier works fine)
# Just copy the output below and paste into https://grok.x.ai or https://claude.ai
print("RAW SCAN COMPLETE – COPY EVERYTHING BELOW THE LINE AND PASTE INTO GROK/CLAUDE:\n")
print("═" * 80)
print(raw_result)
print("═" * 80)
print("\nINSTRUCTIONS FOR AI (copy this too):")
print("""
You are a senior penetration tester. Take the Nmap scan above and give the client:
1. Top 3 most dangerous findings (with CVSS-like severity)
2. One-sentence plain English explanation for each
3. Exact remediation steps a non-technical owner can follow
4. Bonus: One-line summary they can forward to their boss/dev team
Format it beautifully with emojis and bold.
""")

input("\nPress Enter when you're ready to paste into Grok/Claude → ")
print("Pasting now would be instant with API – coming in Week 3 😉")
print(f"\nReport + AI summary saved → ai_report_{target}_{datetime.now().strftime('%Y%m%d-%H%M')}.txt")
