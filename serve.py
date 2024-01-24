from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        # Handling POST request
        start_cpu_stress()
        return jsonify({'message': 'CPU stress started successfully'})

    elif request.method == 'GET':
        # Handling GET request
        private_ip = get_private_ip()
        return jsonify({'private_ip': private_ip})

def start_cpu_stress():
    # Start stress_cpu.py in a separate process
    subprocess.Popen(['python', 'stress_cpu.py'])

def get_private_ip():
    # Get private IP address using socket
    private_ip = socket.gethostbyname(socket.gethostname())
    return private_ip

if __name__ == "__main__":
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
