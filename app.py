# Implement a flask server application

from flask import Flask, jsonify
from flask_restful import Api, Resource
import json
import os

app = Flask(__name__)

api = Api(app)

# Define the path to the data file
data_file = os.path.join(os.path.dirname(__file__), 'data.json')

# Define the data class
class Data(Resource):
    def get(self):
        with open(data_file, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    
api.add_resource(Data, '/data')

# The default route to the server
@app.route('/')
def index():
    with open(data_file, 'r') as f:
            data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

