
from flask import Flask, request
from students import *
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/insert_student", methods=['POST', 'GET'])
def insert_student():
    return add_student(request.json)


@app.route("/find", methods=["GET"])
def find_student_by_name():
    return find_student(request.args.get("name"))


if __name__ == "__main__":
    app.run(debug=True)
