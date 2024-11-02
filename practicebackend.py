from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Backend Demo!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    response = {
        'message': 'Data received!',
        'received_data': new_data
    }
    return jsonify(response), 201

@app.route('/api/data', methods=['PUT'])
def put_data():
    updated_data = request.json
    response = {
        'message': 'Data updated!',
        'updated_data': updated_data
    }
    return jsonify(response)

@app.route('/api/data', methods=['DELETE'])
def delete_data():
    response = {
        'message': 'Data deleted!'
    }
    return jsonify(response)

@app.route('/api/data', methods=['DELETE'])
def delete_data():
    response = {
        'message': 'Data deleted!'
    }
    return jsonify(response)

@app.route('/api/data', methods=['PATCH'])
def patch_data():
    updated_data = request.json
    response = {
        'message': 'Data patched!',
        'updated_data': updated_data
    }
    return jsonify(response)

@app.route('/api/data', methods=['OPTIONS'])
def options_data():
    response = {
        'message': 'Data options!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
