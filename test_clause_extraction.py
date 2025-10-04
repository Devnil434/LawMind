import requests
import json

# Test the clause extraction endpoint
def test_clause_extraction():
    # Sample legal document text
    sample_text = """
    CONFIDENTIALITY AGREEMENT
    
    This Confidentiality Agreement ("Agreement") is entered into on January 1, 2025, by and between 
    TechCorp Solutions Inc., a Delaware corporation ("Company"), and John Smith ("Recipient").
    
    1. CONFIDENTIAL INFORMATION: The term "Confidential Information" includes all technical and 
    business information disclosed by Company to Recipient, whether orally or in writing, that is 
    designated as confidential or that reasonably should be understood to be confidential given 
    the nature of the information and the circumstances of disclosure.
    
    2. OBLIGATIONS: Recipient agrees to (a) protect the confidentiality of the Confidential Information, 
    (b) not use the Confidential Information for any purpose other than the evaluation of a potential 
    business relationship with Company, and (c) not disclose the Confidential Information to any 
    third party without the prior written consent of Company.
    
    3. TERM: This Agreement shall remain in effect for a period of two (2) years from the date of 
    disclosure of the first item of Confidential Information, unless terminated earlier by either 
    party upon thirty (30) days written notice to the other party.
    
    4. RETURN OF MATERIALS: Upon termination of this Agreement or upon Company's request, Recipient 
    shall promptly return all Confidential Information in tangible form and all copies thereof, 
    and shall certify in writing that all such materials have been returned or destroyed.
    
    5. GOVERNING LAW: This Agreement shall be governed by and construed in accordance with the 
    laws of the State of Delaware without regard to its conflict of laws principles.
    
    IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.
    """
    
    url = "http://localhost:8002/extract/"
    
    payload = {
        "text": sample_text
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print("Clause Extraction Result:")
            print(json.dumps(result, indent=2))
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_clause_extraction()