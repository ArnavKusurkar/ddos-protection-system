# Distributed Denial-of-Service (DDoS) Protection System

## Overview
This project is a custom Distributed Denial-of-Service (DDoS) Protection System built in Python using Scapy and Flask. It monitors network traffic in real-time, detects potential DDoS attacks, and provides a web dashboard for alerts.

## Features
- Real-time traffic monitoring and analysis.
- Detection of DDoS attack patterns.
- Automated mitigation techniques (e.g., IP blocking).
- Web dashboard for viewing alerts.
- Detailed logging of detected incidents.

## Setup Instructions
Open your web browser and navigate to http://127.0.0.1:5000 to view real-time alerts after starting your server
**Clone the repository**:
   ```bash
   git clone https://github.com/ArnavKusurkar/ddos-protection-system.git
   cd ddos-protection-system
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   python app.py


