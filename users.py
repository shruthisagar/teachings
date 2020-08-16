from bson import ObjectId

from mongo_functions import MongoFunctions


def insert_user(data):
    if not data.get("email_id"):
        return "Email Missing"
    query = {"email_id": data.get("email_id")}
    email_found = MongoFunctions().find_one_doc('factory', 'users',
                                                query, {"name": 1})

    if email_found:
        email_found['_id'] = str(email_found['_id'])
        return email_found
    insert_result = MongoFunctions().insert_doc('factory', 'users', data)
    return "Inserted"


def update_user(_id, data):
    query = {"_id": ObjectId(_id)}
    MongoFunctions().update_one_doc('factory', 'users', query, data)


def find_user(query):
    result = MongoFunctions().find_one_doc('factory', 'users',
                                           query, {"_id": 0})
    return result
