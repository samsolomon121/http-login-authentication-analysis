
# HTTP Login Authentication and Network Traffic Analysis Using Wireshark

## Project Overview
This beginner-level cybersecurity project demonstrates how HTTP login authentication works and how network traffic can be captured and analysed using Wireshark.

## Objective
To understand how login credentials are transmitted over an unencrypted HTTP connection and identify the security risks through packet analysis.

## Tools Used
- Python
- HTML
- Wireshark
- Google Chrome

## Project Implementation
1. Created a test login webpage using Python.
2. Hosted the webpage on a local HTTP server.
3. Submitted fake login credentials.
4. Captured network traffic using Wireshark.
5. Identified HTTP GET and POST requests.
6. Used Follow TCP Stream to inspect the submitted form data.
7. Observed that the test credentials were visible in plaintext.

## Key Finding
The experiment demonstrated that login credentials transmitted over an unencrypted HTTP connection can be exposed through packet analysis.

## Learning Outcomes
- Understanding HTTP GET and POST requests.
- Learning how browsers communicate with web servers.
- Capturing and analysing network packets.
- Understanding the importance of HTTPS and TLS encryption.
- Using Wireshark display filters and Follow TCP Stream.

## Project Structure
- `app.py` - Python login application.
- `Screenshots/` - Screenshots of the experiment.
- `Evidence/` - Captured network traffic file.
- `Documentation/` - Project overview and notes.

## Disclaimer
This experiment was conducted locally using fake credentials for educational purposes.
