import markdown
import os
import shelve

from flask import Flask, g
from flask_restful import Resource, Api, reqparse

#Create instance of flask and create the API
app = Flask(__name__)
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present the README.md file as a html page"""

    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


class EmployeeList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return {'message': 'Success', 'data': devices}, 200

    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('role', required=True)
        parser.add_argument('tel_number', required=True)

        args = parser.parse_args()

        shelf = get_db()

        if (args['identifier'] in shelf):
            return {'message':'Forbidden - Employee already exists', 'data':shelf[args['identifier']]}, 403

        shelf[args['identifier']] = args

        return {'message': 'Employee registered', 'data': args}, 201


class Employee(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message':'Employee not found', 'data':{}}, 404

        return {'message':'Employee found', 'data':shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'Device not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204

    def put(self, identifier):

        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'Device not found', 'data': {}}, 404

        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('role', required=True)
        parser.add_argument('tel_number', required=True)

        args = parser.parse_args()


        shelf[identifier] = args

        return {'message': 'Employee updated', 'data': args}, 201






api.add_resource(EmployeeList, '/employee')
api.add_resource(Employee, '/employee/<string:identifier>')
