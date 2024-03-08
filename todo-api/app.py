from flask import Flask, jsonify, request
tasks = []
app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.get_json()
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task.get('id') == task_id]
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    task[0].update(request.get_json())
    return jsonify(task[0])

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task.get('id') == task_id]
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    tasks.remove(task[0])
    return jsonify({'message': 'Task deleted'})

"""
GET
POST
PUT
DELETE
"""
if __name__ =="__main__":
    app.run(debug=True)