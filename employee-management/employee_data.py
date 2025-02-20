# employee_data.py

class EmployeeData:
    def __init__(self):
        self.employees = {}

    def add(self, employee_info):
        self.employees[employee_info["Employee ID"]] = employee_info

    def get(self, employee_id):
        return self.employees.get(employee_id, None)

    def get_all(self):
        return list(self.employees.values())

    def update(self, employee_id, updated_info):
        if employee_id in self.employees:
            self.employees[employee_id].update(updated_info)
            return True
        return False

    def delete(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False
