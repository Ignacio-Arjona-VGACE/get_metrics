from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.json
    code = data.get('code', '')
    try:
        result = eval(code)  # ⚠️ Solo para pruebas
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
