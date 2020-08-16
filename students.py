from datetime import datetime
from mongo_functions import MongoFunctions

db = 'jit'
collection = 'students'


def add_student(data):
    if not {"name", "usn"}.issubset(data.keys()):
        return "mandatory keys missing"
    student_found = MongoFunctions().find_one_doc(db, collection, {"usn": data.get("usn")})
    if student_found:
        return "student by usn " + str(data['usn']) + " exists"

    data['inserted_time'] = datetime.utcnow()

    result = MongoFunctions().insert_doc(db, collection, data)
    if result:
        return "success"
    return "failure"


def find_student(name):
    result = MongoFunctions().find_one_doc(db, collection, {"name": name})
    if result:
        result['_id'] = str(result['_id'])
    return result
