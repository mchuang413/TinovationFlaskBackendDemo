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

@app.route('/setData', methods=['POST'])
def set_data():
    try:
        data = "Hello World!"
        with open('data.txt', 'w') as file:
            file.write(data)
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/updateData', methods=['PUT'])
def update_data():
    try :
        data = "Hello World! Updated"
        with open('data.txt', 'w') as file:
            file.write(data)
            return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/deleteData', methods=['DELETE'])
def delete_data():
    try:
        with open('data.txt', 'w') as file:
            file.write('')
        return jsonify({"content": "Data deleted!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getJsonData', methods=['GET'])
def get_json_data():
    try:
        with open('data.json', 'r') as file:
            data = file.read()
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/setJsonData', methods=['POST'])
def set_json_data():
    try:
        data = {"name": "John Doe", "age": 30}
        with open('data.json', 'w') as file:
            file.write(str(data))
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/updateJsonData', methods=['PUT'])
def update_json_data():
    try:
        data = {"name": "John Doe", "age": 30, "city": "New York"}
        with open('data.json', 'w') as file:
            file.write(str(data))
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/deleteJsonData', methods=['DELETE'])
def delete_json_data():
    try:
        with open('data.json', 'w') as file:
            file.write('')
        return jsonify({"content": "Data deleted!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/getJsonData', methods=['GET'])
def get_json_data():
    try:
        with open('data.json', 'r') as file:
            data = file.read()
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/setJsonData', methods=['POST'])
def set_json_data():
    try:
        data = {"name": "John Doe", "age": 30}
        with open('data.json', 'w') as file:
            file.write(str(data))
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/updateJsonData', methods=['PUT'])
def update_json_data():
    try:
        data = {"name": "John Doe", "age": 30, "city": "New York"}
        with open('data.json', 'w') as file:
            file.write(str(data))
        return jsonify({"content": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)