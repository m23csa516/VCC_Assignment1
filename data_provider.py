from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    data = {"message": "Data from VM1!", "status": "Success"}
    print("[VM1] Data request received. Sending response:", data)  # Print when API is hit
    return jsonify(data)

if __name__ == '__main__':
    print("[VM1] API Server is starting on port 6000...")
    app.run(host='0.0.0.0', port=6000)
