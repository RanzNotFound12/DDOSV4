DDOS.py - High Performance Layer 4 Attack Tool

> A fast, lightweight, and highly customizable L4 denial-of-service simulation tool.




---

Overview

DDOS.py is a command-line based Layer 4 attack tool designed to simulate high-intensity TCP/UDP packet floods towards a target IP or hostname. Intended for educational, research, and stress-testing environments, this script provides rapid packet generation and real-time attack visualization directly in your terminal.

> Note: Use responsibly. Authorized testing only.




---

Features

Multi-threaded packet sending

UDP & TCP flood modes

Real-time progress and log output

Custom target & port configuration

Terminal-based attack dashboard



---

Usage

python ddos.py

Input Parameters:

Target: IP address or domain (e.g., 192.168.1.1 or example.com)

Port: Destination port (default: 80)

Packets/Second: (optional) Define intensity

Duration: Time in seconds



---

Example

Target IP: 104.21.89.11
Port      : 443
Threads   : 100
Duration  : 60s
Protocol  : UDP

[INFO] Resolving target...
[SUCCESS] Target resolved to 104.21.89.11
[ATTACK] Sending packets...
[SENT] 500000 packets sent | Avg speed: 8,200 pps
[STATUS] Target seems unstable...
[COMPLETE] Attack finished after 60 seconds.


---

Installation

Ensure Python 3.x is installed:

git clone https://github.com/yourname/ddoscik
cd ddoscik
pip install -r requirements.txt
python ddos.py


---

Legal Disclaimer

This script is intended only for educational purposes and authorized security testing.
Do NOT use this tool against websites, servers, or networks without explicit permission.

We are not responsible for any misuse or damages caused by this tool.


---

Author
Ranzy
