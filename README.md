# 🚀 Revenue Intelligence Automation (Mock-up)

This project is a high-level "Revenue Intelligence" prototype designed for Executive support. It simulates a system that listens for real-time webhooks (from platforms like Gong or PandaDoc), analyzes call transcripts for competitor mentions and action items, and prepares the data for Executive review.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** Flask (Web Server)
* **Tunneling:** ngrok Python SDK (Automated Tunneling)
* **Environment:** Virtual Environments (venv) for dependency isolation

---

## 🏗️ Project Structure
```text
.
├── .venv/               # Isolated Python environment (do not upload)
├── .gitignore           # Tells Git to ignore .venv and cache files
├── app.py               # Main Flask server with integrated ngrok SDK
├── intelligence_engine.py # Logic for parsing transcripts and extracting data
└── requirements.txt     # Project dependencies (Flask, ngrok)


🚀 Getting Started
1. Setup the Environment
Clone the repository and create your virtual environment:

```PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
2. Configure ngrok
Ensure you have your ngrok Authtoken ready. In app.py, the tunnel is managed programmatically:
```
```Python

ngrok.forward(5000, authtoken="YOUR_AUTHTOKEN_HERE")

```

3. Launch the Server
```PowerShell

python app.py

```
Upon startup, the console will print your Public Webhook URL (e.g., https://random-id.ngrok-free.app).

🧪 Testing the Integration
To simulate a real-time event from a service like Gong, use the following PowerShell command. Replace the Uri with your active ngrok URL:

```PowerShell

$body = @{
    meta = @{ title = "Project Alpha Close"; client = "Tesla" }
    transcript = @( @{ speaker = "Rep"; text = "I will send the contract tonight." } )
}

Invoke-RestMethod -Method Post `
  -Uri "[https://YOUR-URL.ngrok-free.app/gong-webhook](https://YOUR-URL.ngrok-free.app/gong-webhook)" `
  -ContentType "application/json" `
  -Body ($body | ConvertTo-Json)

```

📊 Monitoring
You can monitor all real-time traffic and inspect JSON payloads by visiting the local ngrok dashboard: URL: http://127.0.0.1:4040
```
🛡️ Security Note
The .venv directory and sensitive API keys should never be committed to version control. This project uses a .gitignore to ensure environment isolation.


---

### Why this README matters for your career:
When you show this to a hiring manager, it demonstrates **Technical Writing** skills. You aren't just saying "I can code"; you are showing you can build a system that *others* can understand and use.



**Would you like me to help you draft a "Project Summary" paragraph you can add to your LinkedIn or Portfolio to describe this specific project?**