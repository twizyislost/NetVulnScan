# NetVulnScan

**NetVulnScan** is a lightweight, modular network vulnerability scanner designed for educational and research purposes. This tool allows users to scan open ports, inspect network surfaces, and identify common exposures on a given host or subnet.

## Features
- Targeted TCP port scanning
- Clean CLI interface for rapid input
- Modular design to support:
- Python for orchestration
- Optional integration with C++, Go, Java, or Node.js for extended probing
- Designed to be extensible for CVE scanning, banner grabbing, and OS fingerprinting

## Project Goals
- Build an efficient scanning framework from scratch
- Learn and apply socket programming, subprocess handling, and network protocol analysis
- Write clean, testable, and scalable code
- Practice Git/GitHub workflow, including branching, pull requests, and commit hygiene

## Requirements
- [Python (3.10+)](https://www.python.org/downloads/)
- [rich](https://pypi.org/project/rich/)
- [scapy](https://pypi.org/project/scapy/)

## Install dependencies:
`pip install -r python/requirements.txt`

### Or manually:
`pip install rich scapy`

## Usage
`cd python`
`python main.py`

You will be prompted to enter a target IP or hostname. The scanner will then enumerate ports from 1 to 1024 (default range).

## Roadmap
- Add multi-threaded scanning
- Implement banner grabbing
- Integrate basic fingerprinting (TTL, TCP flags)
- Build CLI flags with argparse
- Export scan results to JSON or CSV

## Contributing
This project is maintained by a solo developer as a self-learning journey in networking and cybersecurity tooling. Code is written modularly to allow future contributions, plugin systems, or language-specific modules.

## License
MIT License — see LICENSE file for details.
Let me know if you'd like a version that includes CI/CD badges, links to GitHub issues, or even a diagram of the architecture using ASCII or Mermaid.
