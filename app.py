from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    if 'file' not in request.files or 'column' not in request.form:
        return jsonify({'error': 'Missing file or column name'}), 400

    file = request.files['file']
    column_name = request.form['column']

    try:
        df = pd.read_excel(file)
        if column_name not in df.columns:
            return jsonify({'error': f'Column "{column_name}" not found in Excel file'}), 400

        mean_value = df[column_name].mean()
        return jsonify({'mean': mean_value})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)