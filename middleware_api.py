from flask import Flask, jsonify
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app) 

# VM1 API URL
VM1_URL = "http://192.168.29.51:6000/get_data"

@app.route('/fetch_vm1_data')
def fetch_vm1_data():
    print("[Host Machine] Received request from VM2. Fetching data from VM1...")
    response = requests.get(VM1_URL)
    print("[Host Machine] Data received from VM1:", response.json())  # Fetch data from VM1 API
    return jsonify(response.json())  # Return data to VM2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs on port 5000
