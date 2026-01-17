import ngrok
import os
from flask import Flask, request, jsonify
from intelligence_engine import analyze_call

app = Flask(__name__)
'''
# 1. SETUP THE TUNNEL DIRECTLY IN CODE

def setup_ngrok():
# Replace 'YOUR_AUTHTOKEN' with your actual token
    # In a real job, you'd use an environment variable for this!
    session = ngrok.SessionBuilder().authtoken("38DSJLiLybU9c7QKnx9yV4M6yHn_2tUR2qYpmWm6ZWMqiNUvs").connect()
    
    # This creates the HTTP tunnel
    tunnel = session.http_endpoint().listen()
    
    print(f"🚀 Public URL: {tunnel.url()}")
    return tunnel
''' 
# 1. SIMPLE FORWARDING SETUP
# This is the easiest way to use the SDK with Flask
def start_ngrok():
    # Replace the token with yours (keep it in quotes)
    # The .forward() method handles the event loop issues for you
    listener = ngrok.forward(5000, authtoken="38DSJLiLybU9c7QKnx9yV4M6yHn_2tUR2qYpmWm6ZWMqiNUvs")
    print(f"🚀 SUCCESS: Your Public Webhook URL is: {listener.url()}") 

@app.route('/gong-webhook', methods=['POST'])
def handle_webhook():
    # This receives the real-time 'ping' from the internet
    data = request.get_json(silent=True) 
    if not data:
        return jsonify({"error": "Bad Request"}), 400
    # Extract data from the notification
    # Logic: Log the event
    print(f"[*] Analysis Triggered for: {data.get('meta', {}).get('client', 'Unknown Client')}")
    return jsonify({"status": "Success"}), 200

if __name__ == '__main__':
    '''
    # Start the tunnel first
    ngrok_tunnel = setup_ngrok()
    
    # Start Flask
    try:
        app.run(port=5000)
    except KeyboardInterrupt:
        print("Stopping server...")
    '''
    # Start the tunnel
    start_ngrok()
    
    # Start the Flask server
    app.run(port=5000)