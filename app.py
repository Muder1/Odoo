from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# Serve HTML, CSS, JS files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    new_entry = request.get_json()

    # Read existing data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new entry
    data.append(new_entry)

    # Save back to file
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    return jsonify({'message': 'Data saved successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
