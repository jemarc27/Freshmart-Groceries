from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()

class PersonalInfo:
    def __init__(self, Name, Date_of_birth, Contact_number, Emergency_contact_number):
        self.Name = Name
        self.Date_of_birth = Date_of_birth
        self.Contact_number = Contact_number
        self.Emergency_contact_number = Emergency_contact_number

    def save(self):
        personal_info_data = {
            "Name": self.Name,
            "Date_of_birth": self.Date_of_birth,
            "Contact_number": self.Contact_number,
            "Emergency_contact_number": self.Emergency_contact_number
        }
        result = db.personal_info.insert_one(personal_info_data)
        return str(result.inserted_id)

    @staticmethod
    def get_all():
        return list(db.personal_info.find())

    @staticmethod
    def get_by_id(info_id):
        return db.personal_info.find_one({"_id": ObjectId(info_id)})

