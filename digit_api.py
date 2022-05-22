import base64
import binascii
import pickle

import cv2
import numpy as np
from flask import jsonify, request
from flask_restful import Resource


class DigitClassifier(Resource):
    @staticmethod
    def unpickle_model(file_name):
        with open(file_name, 'rb') as file:
            model = pickle.load(file)
        return model

    # initialize models as class attributes
    k_neighbors_model = unpickle_model(
        'kneighbors_digit_model.dat')
    random_forest_model = unpickle_model(
        'randomforest_digit_model.dat')

    @staticmethod
    def predict(model, img_arr):
        # make predictions and return the results
        pred = model.predict(img_arr)[0]
        pred_prob = model.predict_proba(img_arr)[0].round(2)
        return int(pred), pred_prob.tolist()

    @staticmethod
    def preprocess_img(img_str):
        img_arr = np.fromstring(img_str, np.uint8)
        img_arr = cv2.imdecode(img_arr, flags=cv2.IMREAD_GRAYSCALE)
        # invert BW since model trained with mainly black (0) data
        if np.average(img_arr) > 127.5:
            img_arr = cv2.bitwise_not(img_arr)
        # create rectangle containing the digit and crop it
        coords = cv2.findNonZero(img_arr)
        x, y, w, h = cv2.boundingRect(coords)
        margin = 20
        x0 = 0 if x < margin else x - margin
        y0 = 0 if y < margin else y - margin
        cropped_img_arr = img_arr[y0:y+h+margin, x0:x+w+margin]
        # resize: model trained on 1x784 (28x28) features
        img_arr = cv2.resize(cropped_img_arr, (28, 28))
        # reshape from 28x28 to 1x784
        img_arr = img_arr.reshape(img_arr.shape[0] * img_arr.shape[1])
        img_arr = img_arr / 255  # scale from [0, 255] to [0, 1]
        return np.array([img_arr])

    @classmethod
    def create_models_response(cls, img_byte_str):
        img_arr = cls.preprocess_img(img_byte_str)
        random_forest_pred, random_forest_proba = \
            cls.predict(
                cls.random_forest_model,
                img_arr,
            )
        k_neighbors_pred, k_neighbors_proba = \
            cls.predict(
                cls.k_neighbors_model,
                img_arr,
            )
        return jsonify({
            'models': [
                {
                    'name': 'K Neighbors',
                    'prediction': k_neighbors_pred,
                    'probabilities': {
                        i: v for (i, v) in enumerate(k_neighbors_proba)
                    }
                },
                {
                    'name': 'Random Forest',
                    'prediction': random_forest_pred,
                    'probabilities': {
                        i: v for (i, v) in enumerate(random_forest_proba)
                    }
                },
            ]
        })


class FileUploadClassifier(DigitClassifier):
    def __init__(self):
        super().__init__()

    def post(self):
        # check if the post request has the image part
        if 'image' not in request.files:
            return jsonify({'message': 'No file provided'})

        file = request.files['image']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return jsonify({'message': 'No selected file'})
        if file:
            img_byte_str = file.read()
            return self.create_models_response(img_byte_str)
        return jsonify({'message': 'No form image file was given'})


class DataUploadClassifier(DigitClassifier):
    def __init__(self):
        super().__init__()

    def post(self):
        _, data = request.data.decode().split(',', 1)
        try:
            img_byte_str = base64.b64decode(data)
            return self.create_models_response(img_byte_str)
        except binascii.Error:
            return jsonify({'message': 'Invalid data provided.'})
