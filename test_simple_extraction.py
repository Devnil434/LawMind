import requests
import json

# Test the clause extraction with a simpler document
def test_simple_extraction():
    # Simple test document
    simple_text = """
    CONFIDENTIALITY AGREEMENT
    
    This Confidentiality Agreement is made between TechCorp Inc. and John Smith on January 1, 2025.
    
    1. CONFIDENTIAL INFORMATION: All information shared between the parties.
    
    2. OBLIGATIONS: Both parties must keep information confidential.
    
    3. TERM: This agreement lasts for one year.
    """
    
    url = "http://localhost:8002/extract/"
    
    payload = {
        "text": simple_text
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print("Extraction Result:")
            print(json.dumps(result, indent=2))
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_simple_extraction()