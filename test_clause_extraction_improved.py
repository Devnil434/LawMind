import requests
import json

# Test the clause extraction endpoint with different document types
def test_clause_extraction():
    # Test cases with different document types
    test_cases = [
        {
            "name": "Simple Agreement",
            "text": """
            SERVICE AGREEMENT
            
            This Service Agreement ("Agreement") is made and entered into on January 1, 2025, by and between 
            ABC Corporation, a Delaware corporation ("Client"), and XYZ Solutions Inc., a California corporation ("Service Provider").
            
            1. SERVICES: Service Provider agrees to provide software development services to Client.
            
            2. TERM: This Agreement shall commence on January 1, 2025, and continue for a period of one (1) year, 
            unless terminated earlier in accordance with Section 5.
            
            3. PAYMENT: Client shall pay Service Provider a monthly fee of $5,000 for the services rendered.
            
            4. CONFIDENTIALITY: Both parties agree to maintain the confidentiality of any proprietary information 
            received during the term of this Agreement.
            
            5. TERMINATION: Either party may terminate this Agreement with thirty (30) days written notice.
            
            6. GOVERNING LAW: This Agreement shall be governed by the laws of the State of California.
            """
        },
        {
            "name": "Complex Contract",
            "text": """
            CONFIDENTIALITY AND NON-DISCLOSURE AGREEMENT
            
            This Confidentiality and Non-Disclosure Agreement ("Agreement") is entered into as of February 15, 2025, 
            by and between TechInnovate LLC ("Disclosing Party") and Global Ventures Group ("Receiving Party").
            
            WHEREAS, the parties desire to engage in discussions regarding a potential business relationship;
            
            NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:
            
            1. CONFIDENTIAL INFORMATION: "Confidential Information" includes all technical, business, financial, 
            and proprietary information disclosed by Disclosing Party to Receiving Party.
            
            2. OBLIGATIONS OF RECEIVING PARTY: Receiving Party agrees to (a) protect the confidentiality of 
            Confidential Information, (b) use such information only for evaluating the business relationship, 
            and (c) not disclose it to third parties without prior written consent.
            
            3. EXCLUSIONS: Information shall not be considered Confidential Information if it (a) is or becomes 
            publicly known, (b) was known to Receiving Party prior to disclosure, or (c) is independently 
            developed without reference to Disclosing Party's information.
            
            4. TERM AND TERMINATION: This Agreement shall remain in effect for two (2) years from the date of 
            disclosure of the first item of Confidential Information.
            
            5. RETURN OF MATERIALS: Upon termination or Disclosing Party's request, Receiving Party shall 
            promptly return all materials containing Confidential Information.
            
            6. REMEDIES: Receiving Party acknowledges that unauthorized disclosure may cause irreparable harm, 
            entitling Disclosing Party to seek injunctive relief.
            
            7. GOVERNING LAW: This Agreement shall be governed by the laws of the State of New York.
            
            IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.
            """
        }
    ]
    
    url = "http://localhost:8002/extract/"
    
    for test_case in test_cases:
        print(f"\n--- Testing: {test_case['name']} ---")
        
        payload = {
            "text": test_case["text"]
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
                print(f"- Parties: {result['extracted_data']['parties']}")
                print(f"- Effective Date: {result['extracted_data']['effective_date']}")
                print(f"- Termination Date: {result['extracted_data']['termination_date']}")
                print(f"- Number of Clauses: {len(result['extracted_data']['clauses'])}")
                
                # Show first few clauses
                for i, clause in enumerate(result['extracted_data']['clauses'][:3]):
                    print(f"  Clause {i+1}: {clause['title']} ({clause['type']})")
            else:
                print(f"Error: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_clause_extraction()