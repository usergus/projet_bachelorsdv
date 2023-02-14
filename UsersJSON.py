from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com'},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Doe', 'email': 'jane.doe@example.com'},
    {'id': 3, 'first_name': 'Bob', 'last_name': 'Smith', 'email': 'bob.smith@example.com'}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'})

@app.route('/users', methods=['POST'])
def add_user():
    user = request.json
    user['id'] = len(users) + 1
    users.append(user)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True, port=8080)