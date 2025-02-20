# controller.py

from employee_data import EmployeeData

class EmployeeController:
    def __init__(self):
        self.employee_data = EmployeeData()

    def add_employee(self, employee_info):
        self.employee_data.add(employee_info)
        return employee_info

    def get_employee(self, employee_id):
        return self.employee_data.get(employee_id)

    def get_all_employees(self):
        return self.employee_data.get_all()

    def update_employee(self, employee_id, updated_info):
        if self.employee_data.update(employee_id, updated_info):
            return {"message": "Employee updated successfully"}
        return {"message": "Employee not found"}, 404

    def delete_employee(self, employee_id):
        if self.employee_data.delete(employee_id):
            return {"message": "Employee deleted successfully"}
        return {"message": "Employee not found"}, 404
