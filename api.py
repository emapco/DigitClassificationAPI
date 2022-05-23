from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api

from digit_api import FileUploadClassifier, DataUploadClassifier

app = Flask(__name__, static_folder='static', static_url_path='/')
api = Api(app)
cors = CORS(app)

api.add_resource(FileUploadClassifier, '/api/file')
api.add_resource(DataUploadClassifier, '/api/data')


@app.route('/')
def main():
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.run(debug=True)
