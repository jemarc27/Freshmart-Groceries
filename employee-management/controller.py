from models import PersonalInfo
from bson import ObjectId

class EmployeeController:
    @staticmethod
    def create_employee(data):
        try:
            # Validate required fields
            required_fields = ["Name", "Date_of_birth", "Contact_Number", "Emergency_contact_number"]
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")

            # Create and save the employee
            employee = PersonalInfo(
                Name=data["Name"],
                Date_of_birth=data["Date_of_birth"],
                Contact_Number=data["Contact_Number"],
                Emergency_contact_number=data["Emergency_contact_number"]
            )
            employee.save()

            # Return the created employee data
            return {
                "Name": employee["Name"],
                "Date_of_birth": employee["Date_of_birth"],
                "Contact_Number": employee["Contact_Number"],
                "Emergency_contact_number": employee["Emergency_contact_number"]
            }
        except Exception as e:
            raise Exception(f"Error creating employee: {str(e)}")

    @staticmethod
    def get_employee_by_id(employee_id):
        try:
            # Convert string ID to ObjectId
            obj_id = ObjectId(employee_id)
            employee = PersonalInfo.get_by_id(obj_id)
            
            if employee:
                return {
                    "Name": employee["Name"],
                    "Date_of_birth": employee["Date_of_birth"],
                    "Contact_Number": employee["Contact_Number"],
                    "Emergency_contact_number": employee["Emergency_contact_number"]
                }
            return None
        except Exception as e:
            raise Exception(f"Error fetching employee: {str(e)}")

    @staticmethod
    def get_all_employees():
        try:
            employees = PersonalInfo.get_all()
            return [{
                "Name": emp["Name"],
                "Date_of_birth": emp["Date_of_birth"],
                "Contact_Number": emp["Contact_Number"],
                "Emergency_contact_number": emp["Emergency_contact_number"]
            } for emp in employees]
        except Exception as e:
            raise Exception(f"Error fetching employees: {str(e)}")
