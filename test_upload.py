import requests
import time

print("Testing upload endpoint...")

# Test the upload endpoint
try:
    with open('contract2.txt', 'rb') as f:
        files = {'file': ('contract2.txt', f, 'text/plain')}
        print("Sending request to http://localhost:8002/upload/")
        response = requests.post('http://localhost:8002/upload/', files=files)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")