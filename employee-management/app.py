# app.py

from flask import Flask, jsonify, request
from controller import EmployeeController

app = Flask(__name__)
controller = EmployeeController()

# Create a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    employee_info = request.get_json()
    added_employee = controller.add_employee(employee_info)
    return jsonify(added_employee), 201

# Get a specific employee by ID
@app.route('/employees/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = controller.get_employee(employee_id)
    if employee:
        return jsonify(employee)
    return jsonify({"message": "Employee not found"}), 404

# Get all employees
@app.route('/employees', methods=['GET'])
def get_all_employees():
    employees = controller.get_all_employees()
    return jsonify(employees)

# Update an employee's details
@app.route('/employees/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    updated_info = request.get_json()
    return jsonify(controller.update_employee(employee_id, updated_info))

# Delete an employee
@app.route('/employees/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    return jsonify(controller.delete_employee(employee_id))

if __name__ == "__main__":
    app.run(debug=True)
