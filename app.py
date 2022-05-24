from flask import Flask
from flask_cors import CORS
from flask_restful import Api

import digit_api

app = Flask(__name__, static_folder='static', static_url_path='/')
api = Api(app)
cors = CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",
            "https://ecortes.me",
        ],
        "methods": [
            "POST",
            "OPTIONS",
        ],
    }
})

api.add_resource(digit_api.FileUploadClassifier, '/api/file')
api.add_resource(digit_api.DataUploadClassifier, '/api/data')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.run()
