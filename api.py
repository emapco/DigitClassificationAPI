from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api

from digit_api import FileUploadClassifier, DataUploadClassifier

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


@app.route('/')
def main():  # put application's code here
    return jsonify({
        'message': "Currently support single digit image "
                   "classification on route /digit/file and /digit/data."
    })


api.add_resource(FileUploadClassifier, '/api/file')
api.add_resource(DataUploadClassifier, '/api/data')

if __name__ == '__main__':
    app.run(debug=True)
