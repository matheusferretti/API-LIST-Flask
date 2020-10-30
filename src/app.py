from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # this is how we get the data from request
    request_body = json.loads(request.data)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return 'something'
    return jsonify(todos), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)