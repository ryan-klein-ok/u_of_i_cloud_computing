from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        start_cpu_stress()
        return jsonify({'message': 'CPU stress started successfully'})

    elif request.method == 'GET':
        private_ip = get_private_ip()
        return jsonify({'private_ip': private_ip})

def start_cpu_stress():
    subprocess.Popen(['python', 'stress_cpu.py'])

def get_private_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    return private_ip

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
