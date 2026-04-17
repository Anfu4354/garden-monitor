from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
  try:
    data = request.json
    print("Received:", data)

    # Save to file
    with open("/home/pi/garden-monitor/data/garden_current.json", "w") as f:
      json.dump(data, f)

    return jsonify({"status": "ok"})

  except Exception as e:
    print("Error:", e) 
    return jsonify({"status": "error"})

@app.route('/')
def home():
  return "server is running"

app.run(host='0.0.0.0', port=5000)
