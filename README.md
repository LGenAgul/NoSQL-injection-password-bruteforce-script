# NoSQL Injection Password Bruteforce Script

This script performs a dictionary-based brute force attack to exploit a NoSQL injection vulnerability on a web application. By iterating through a set of characters, it systematically attempts to discover the correct password for a given username.

## Features
- Leverages **NoSQL injection** to bypass authentication mechanisms.
- Dynamically builds the password character by character.
- Provides a real-time and user-friendly output of the progress.
- Stops as soon as the correct password is found.

## Prerequisites
- Python 3.x installed on your system.
- `requests` library for making HTTP requests.

Install the `requests` library using pip if not already installed:
```bash
pip install requests
```
## USAGE
python brute.py <USERNAME>
