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
        'kneighbors_model.dat')
    random_forest_model = unpickle_model(
        'randomforest_model.dat')

    @staticmethod
    def predict(model, img_arr):
        pred = model.predict(img_arr)[0]
        pred_prob = model.predict_proba(img_arr)[0].round(2)
        return int(pred), pred_prob.tolist()

    @staticmethod
    def crop_and_center_img(img_arr):
        """
        The models were trained with squared images with the digit centered.
        So the rectangle defined by boundingRect is unsatisfactory.
        Thus, we define the center in the x and y direction. Then define the
        square as the max of either the width and height plus a margin so the digit
        isn't touch the edge in the direction of the max width or height.
        :param img_arr: np.array
        :return: cropped image array
        """
        coords = cv2.findNonZero(img_arr)
        x, y, w, h = cv2.boundingRect(coords)
        margin = 150
        # purpose: crop image into a square with the digit in the center
        half_max_coord_plus_margin = (max([w, h]) + margin) // 2
        center_x = x + w // 2
        center_y = y + h // 2
        x0 = max([0, center_x - half_max_coord_plus_margin])
        y0 = max([0, center_y - half_max_coord_plus_margin])
        xf = center_x + half_max_coord_plus_margin
        yf = center_y + half_max_coord_plus_margin
        return img_arr[y0:yf, x0:xf]

    @classmethod
    def preprocess_img(cls, img_str):
        """
        Convert byte string to image array then make it mainly black
        and then resize and reshape it into a 1d array of length 784.
        :param img_str: byte object as str
        :return: image array is the first element of the return array since
        model was trained on array containing image arrays.
        """
        img_arr = np.fromstring(img_str, np.uint8)
        img_arr = cv2.imdecode(img_arr, flags=cv2.IMREAD_GRAYSCALE)
        # invert BW since model trained with mainly black (0) data
        if np.average(img_arr) > 127.5:
            img_arr = cv2.bitwise_not(img_arr)
        # resize cropped image: model trained on 1x784 (28x28) features
        img_arr = cv2.resize(cls.crop_and_center_img(img_arr), (28, 28))
        # img_arr = img_arr / 255  # scale from [0, 255] to [0, 1]
        # reshape from 28x28 to 1x784
        img_arr = img_arr.reshape(img_arr.shape[0] * img_arr.shape[1])
        return np.array([img_arr])

    @classmethod
    def create_models_response(cls, img_byte_str):
        """
        Preprocess the img data then gets prediction results and returns
        a formatted json string
        :param img_byte_str:
        :return: jsonify response
        """
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
    def post(self):
        try:
            # remove base64 header is present
            # 'data:image/png;base64,'
            _, data = request.data.decode().split(',', 1)
        except ValueError:
            data = request.data.decode()  # no header

        try:
            img_byte_str = base64.b64decode(data)
            if img_byte_str == b'':
                raise ValueError  # no data provided
            return self.create_models_response(img_byte_str)
        except (binascii.Error, ValueError):
            return jsonify({'message': 'Invalid data provided.'})
