<p align="center">
  <img src="./assets/phoenix_flame.svg" width="400" alt="PHOENIX Toolkit Banner" />
</p>


Advanced Reconnaissance and Vulnerability Scanning Toolkit

---

## Overview

PHOENIX is a lightweight and extensible reconnaissance framework designed for efficient target enumeration and surface mapping. It automates the process of discovering subdomains, identifying live hosts, scanning open ports, and organizing results for further analysis.

---

## Capabilities

- Subdomain enumeration using multiple sources
- Live host detection and filtering
- Port scanning on discovered assets
- Structured output for easy analysis
- Modular design for adding custom checks

---

## Installation

```bash
git clone https://github.com/yourusername/phoenix.git
cd phoenix
chmod +x phoenix.sh
```

---

## Usage

```bash
./phoenix.sh target.com
```

---

## Output Structure

```
output/
└── target.com/
    ├── subdomains.txt
    ├── live_hosts.txt
    ├── ports.txt
    └── scan_results.txt
```

---

## Dependencies

Ensure the following tools are installed and available in your PATH:

- subfinder
- assetfinder
- httpx
- nmap

### Example Installation (Kali Linux)

```bash
sudo apt update
sudo apt install -y nmap
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/tomnomnom/assetfinder@latest
```

---

## Workflow

1. Enumerate subdomains from multiple sources
2. Merge and deduplicate results
3. Probe for active/live hosts
4. Scan for open ports
5. Store and organize results for review

---

## Customization

PHOENIX is designed to be easily extendable. You can:

- Add new enumeration tools
- Integrate vulnerability scanners
- Modify scanning depth and speed
- Customize output formats

---

## Disclaimer

This tool is intended for authorized security testing and educational purposes only. The user is responsible for complying with applicable laws and regulations.

---
