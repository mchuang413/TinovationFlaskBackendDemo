from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return "Welcome to this demo Server!"

@app.route('/getData', methods=['GET'])
def get_data():
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)