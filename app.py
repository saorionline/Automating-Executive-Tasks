from flask import Flask, request, jsonify
from intelligence_engine import analyze_call

app = Flask(__name__)

@app.route('/gong-webhook', methods=['POST'])
def handle_gong_event():
    # This receives the real-time 'ping' from the internet
    data = request.json 
    
    # Extract data from the notification
    call_meta = data.get("meta", {"title": "Unknown", "client": "Unknown"})
    transcript = data.get("transcript", [])

    # Run our intelligence engine
    result = analyze_call(call_meta, transcript)
    
    print("✅ Real-time Analysis Complete. Alerting Executive...")
    return jsonify(result), 200

if __name__ == '__main__':
    # Start the local server on port 5000
    app.run(port=5000)