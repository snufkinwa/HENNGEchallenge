"""
Author: Janay Harris
This script makes an HTTP POST request with JSON data and TOTP authentication.
Steps:
1. Construct JSON body with:
 - GitHub URL of solution
 - Contact email
 - Solution language
2. Generate TOTP password:
 - Use email + 'HDECHALLENGE003' as secret
 - Apply HMAC-SHA-512 hash
 - Generate 10-digit password
3. Send POST request with:
 - JSON Content-Type header
 - Basic authentication using email and TOTP
Rules:
- Must use HTTP Basic Authentication
- Must use RFC6238 TOTP
- Must use 30-second time step
- Must use HMAC-SHA-512
## Sample Input (JSON)
{
  "github_url": "https://gist.github.com/hennge/b859bd12e7a7fb418141",
  "contact_email": "ninja@example.com",
  "solution_language": "python"
}
## Sample Output
HTTP/1.1 200 OK
{"message":"Congratulations! You have achieved mission 3"}
"""
import hmac
import struct
import time
import requests
import json
import hashlib

def generate_totp(secret, time_step=30, digits=10, hash_algorithm=hashlib.sha512):
    # Get current timestamp and calculate number of time steps
    timestamp = int(time.time())
    time_steps = timestamp // time_step
    
    # Convert time steps to byte string
    msg = struct.pack('>Q', time_steps)
    
    # Calculate HMAC using SHA-512
    secret_bytes = secret.encode('utf-8')
    h = hmac.new(secret_bytes, msg, hash_algorithm).digest()
    
    # Generate TOTP value
    offset = h[-1] & 0x0f
    binary = struct.unpack('>L', h[offset:offset + 4])[0] & 0x7fffffff
    totp = str(binary)[-digits:]
    
    # Pad with zeros if necessary
    return totp.zfill(digits)

def main():
    # Data
    email = "***"
    data = {
        "github_url": "https://gist.github.com/snufkinwa/62815c2b58d5208eab6b684487965cfd",
        "contact_email": email,
        "solution_language": "python"
    }
    
    # Generate TOTP with correct secret
    secret = email + "HENNGECHALLENGE003"
    totp = generate_totp(secret)
    
    # Make request
    url = "https://api.challenge.hennge.com/challenges/003"
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*"
    }
    
    try:
        response = requests.post(
            url,
            json=data,
            headers=headers,
            auth=(email, totp)  
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

if __name__ == "__main__":
    main()
