from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    if 'file' not in request.files:
        return jsonify({'error': 'Missing file'}), 400

    file = request.files['file']

    try:
        content = file.read().decode('utf-8')
        match = re.search(r'Espacio Workcafe\s*(\d+)\s*hora', content)
        if match:
            hours = int(match.group(1))
            return jsonify({'hours': hours})
        else:
            return jsonify({'error': 'Pattern not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)