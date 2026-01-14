import json
"""
# 1. MOCK DATA: This simulates the JSON data you would get from the Gong API
mock_gong_call = {
    "call_id": "98765",
    "transcript": [
        {"speaker": "Sales Rep", "text": "Hi Mr. Smith, thanks for joining. I wanted to discuss our pricing tiers."},
        {"speaker": "Client", "text": "The pricing looks high. We also use DocuSign currently, does this integrate?"},
        {"speaker": "Sales Rep", "text": "Yes, we integrate with DocuSign. I will send you the technical spec by Friday."},
        {"speaker": "Client", "text": "Great. Let's schedule a follow-up for next Tuesday at 10 AM."}
    ]
}

def analyze_call_data(call_data):
    print(f"--- Analyzing Call ID: {call_data['call_id']} ---")
    
    transcript = call_data['transcript']
    
    # 2. KEYWORD TRACKING (The 'Revenue Intelligence' part)
    # Executives want to know if competitors or specific tools were mentioned.
    competitors = ["DocuSign", "PandaDoc", "AdobeSign"]
    found_competitors = []

    # 3. ACTION ITEM EXTRACTION
    # We look for 'trigger words' like 'send', 'schedule', or 'Friday'
    action_items = []
    
    for entry in transcript:
        text = entry['text']
        
        # Check for competitors
        for c in competitors:
            if c.lower() in text.lower():
                found_competitors.append(c)
        
        # Simple logic to find commitments
        if "will" in text or "schedule" in text:
            action_items.append(f"{entry['speaker']}: {text}")

    # 4. OUTPUT THE "EXECUTIVE BRIEF"
    print(f"\nCOMPETITORS MENTIONED: {list(set(found_competitors))}")
    print("\nPROPOSED ACTION ITEMS:")
    for item in action_items:
        print(f"- {item}")

# Run the simulation
analyze_call_data(mock_gong_call)
"""
def analyze_call(call_metadata, transcript):
    """
    Simulates AI analysis of a sales call for an Executive.
    """
    print(f"\n[AI ANALYSIS] Processing Call: {call_metadata['title']}")
    
    # 1. Competitor Tracking
    competitors = ["Salesforce", "DocuSign", "Zoom"]
    mentions = [c for c in competitors if c.lower() in str(transcript).lower()]
    
    # 2. Action Item Extraction (Looking for commitment words)
    action_items = []
    for entry in transcript:
        if any(word in entry['text'].lower() for word in ["will send", "schedule", "follow up"]):
            action_items.append(f"{entry['speaker']}: {entry['text']}")

    # 3. Executive Summary
    summary = {
        "status": "Success",
        "client": call_metadata['client'],
        "competitors_flagged": mentions,
        "task_list": action_items
    }
    return summary

# --- Mock Data for Testing ---
if __name__ == "__main__":
    mock_meta = {"title": "Q1 Strategy Sync", "client": "Acme Corp"}
    mock_transcript = [
        {"speaker": "Sales Rep", "text": "I will send the PandaDoc contract tonight."},
        {"speaker": "Client", "text": "We are also looking at Salesforce for our CRM."}
    ]
    print(json.dumps(analyze_call(mock_meta, mock_transcript), indent=2))